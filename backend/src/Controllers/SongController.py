from flask import request, redirect, Blueprint, jsonify
from dotenv import load_dotenv
from src.Entities.Match import Match
from src.Entities.PlaylistRating import PlaylistRating
from src.Entities.SongRating import SongRating
from src.Services.database_config import open_connection
from src.Services.FeedbackService import add_feedback_questions, add_open_feedback
from src.Services.QuestionnaireService import add_user, get_personality, get_value
from src.Services.database_config import DatabaseException
from src.Services.SongService import get_top_songs, add_top_songs, add_playlist_ratings, add_song_ratings
from src.spotify import get_access_token, get_top_songs_api, AuthorizationException, InvalidAccountException
from src.Computation.matching import match
import os

load_dotenv()

songs = Blueprint('spotify', __name__)
frontend_url = os.getenv('FRONTEND_URL')
db, cursor, database = open_connection()


class BatchException(Exception):
    pass


@songs.route('/songs/get')
def retrieve_top_songs():
    """
    Retrieves the top songs of a given user
    :except DatabaseException: if there is a problem while fetching the data
    :return: 5 top songs of a user
    """
    try:
        userId = request.args['userId']

        # Given the user id, retrieve top songs from database.
        top_songs = get_top_songs(userId, db, cursor, database)

        # Return JSON object with such a song list.
        return jsonify(songs=[song.__dict__ for song in top_songs])
    except DatabaseException as e:
        print(e)
        # Exception handling in case there is a database error.
        return redirect(os.getenv('FRONTEND_URL') + "/error/database")


@songs.route('/match')
def match_user():
    """
    Retrieves the matches of a given user: the userIds of the matches and their top songs
    :except DatabaseException: if there is a problem while fetching the data from the database
    :return: 5 top songs of a user.
    """
    req = request.args
    userId = req['userId']

    try:
        # Add the newly formatted answers to our database.
        values = get_value(userId, db, cursor, database)
        personality = get_personality(userId, db, cursor, database)

        batch = os.getenv("BATCH")
        if batch == str(2):
            batch = 1
        elif batch == str(1):
            raise BatchException("Not in the right batch to do matching.")

        # Find IDs of the users more similar to the given user id
        val_user, pers_user, random_user = match(userId, values, personality, batch, os.environ.get("METRIC"))

        lst = [Match(val_user, get_top_songs(val_user, db, cursor, database)),
               Match(pers_user, get_top_songs(pers_user, db, cursor, database)),
               Match(random_user, get_top_songs(random_user, db, cursor, database))]

        # Format song list into a jsonifiable object
        data = []
        for single_match in lst:
            matched = {"user_id": single_match.userId, "songs": [song.__dict__ for song in single_match.songs]}

            data.append(matched)
        return jsonify(match=data)
    except DatabaseException as e:
        # Exception handling in case there is an error.
        response = jsonify({'message': str(e)})
        return response, 502
    except BatchException as e:
        print(e)
        response = jsonify({'message': str(e)})
        return response, 500


@songs.route('/ratings/add', methods=["POST"])
def save_ratings():
    """
   Stores the ratings of a given user once he has provided all the feedback about his recommendations
   :except DatabaseException: if there is a problem while storing the data in the database
   :return: Success message
    """
    try:
        data = request.get_json(force=True)

        ratings = [data['values'], data['personality'], data['random']]

        # Retrieve the user id from the user.
        userId = data['userId']

        # Add song ratings into our database.
        # In order to do that, we need to format the data retrieved. We use a helper Entity SongRating:
        # SongRating(user id, matched user, spotify preview url, rating)

        for rating in ratings:
            songRatings = []

            matchedUserId = rating["matchedUserId"]

            for i, songRating in enumerate(rating["songsRatings"]):
                if songRating != 0:
                    songRatings.append(SongRating(userId, matchedUserId, rating["songUrls"][i], songRating, i + 1))

            add_song_ratings(songRatings, db, cursor, database)

            add_playlist_ratings(PlaylistRating(userId, matchedUserId, rating["playlistRating"]),
                                 db, cursor, database)

            if rating["comment"] != "":
                add_open_feedback(userId, matchedUserId, rating["comment"], db, cursor, database)

            add_feedback_questions(userId, matchedUserId, rating["questionFeedback"], db, cursor, database)

        # Everything has been successfully stored, return success message.
        return jsonify("Success")
    except DatabaseException as e:
        # Exception handling in case there is a database error.
        response = jsonify({'message': str(e)})
        return response, 502


@songs.route('/callback')
def spotify_log_in():
    """
    Handle the Spotify API communication: stores a new user and his top songs into the database
    :except AuthorizationException: if there is a problem while logging in the Spotify account
    :except InvalidAccountException: if there is a problem with the amount of top songs of the user
    :except DatabaseException: if there is a problem while storing the data in the database
    :return: redirect to start of the questionnaire on the frontend.
    """
    try:
        # Retrieve the access token after user is logged in.
        access_token = get_access_token(request.args['code'])

        # Find top songs of the user.
        top_songs = get_top_songs_api(access_token)

        # Store the user in the database.
        batch_number = os.getenv('BATCH')
        userId = add_user(batch_number, db, cursor, database)

        # Store top songs into our database.
        add_top_songs(userId, top_songs, db, cursor, database)

        # Redirect to first page of the questionnaire
        return redirect(frontend_url + "/introduction?userID=" + str(userId), 302)

    except AuthorizationException as e:
        print(e)
        # Exception handling in case there is an authorization error.
        return redirect(frontend_url + "/error/login")

    except InvalidAccountException as e:
        print(e)
        # Exception handling in case there is an Invalid account error.
        # Happens when a user has less than 5 top songs in his Spotify account
        return redirect(frontend_url + "/error/invalid_account")

    except DatabaseException as e:
        print(e)
        # Exception handling in case there is a database error.
        return redirect(frontend_url + "/error/database")
