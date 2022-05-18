import json

from flask import request, redirect, Blueprint, jsonify

from src.Entities.Match import Match
from src.Entities.PlaylistRating import PlaylistRating
from src.Entities.SongRating import SongRating
from src.Services.QuestionnaireService import add_user, get_personality, get_songs,get_value
from src.Services.database_config import DatabaseException
from src.Services.SongService import get_top_songs, add_top_songs, add_playlist_ratings, add_song_ratings
from src.spotify import get_access_token, get_top_songs_api, AuthorizationException, InvalidAccountException
from src.Computation.matching import match

songs = Blueprint('spotify', __name__)
frontend_url = "http://www.localhost.com/3000"


@songs.route('/songs/get')
def retrieve_top_songs():
    try:
        data = request.get_json(force=True)

        # Given the user id, retrieve top songs from database.
        top_songs = get_top_songs(data['userId'])

        # Return JSON object with such a song list.
        return jsonify(songs=[song.__dict__ for song in top_songs])
    except DatabaseException as e:
        # Exception handling in case there is a database error.
        return redirect(frontend_url + "/error/database")


@songs.route('/match')
def match_user():
    data = request.get_json(force=True)
    userId = data['user']

    try:
        # Add the newly formatted answers to our database.
        # values = get_value(userId)
        personality = get_personality(userId)
        values = {1,1,1,1,1,1}

        # Find IDs of the users more similar to the given user id
        val_user, pers_user, random_user = match(userId, values, personality, 1, data['metric'])

        # TODO: Return ID of the matched users as well
        lst = [Match(val_user, get_top_songs(val_user)), Match(pers_user, get_top_songs(pers_user)), Match(random_user, get_top_songs(random_user))]

        # Format song list into a jsonifiable object
        #
        jsonifiable = []
        for single_match in lst:
            matched = {"user_id": single_match.userId, "songs" : [song.__dict__ for song in single_match.songs]}

            jsonifiable.append(matched)

        return jsonify(match=jsonifiable)

    except DatabaseException as e:
        # Exception handling in case there is an error.
        response = jsonify({'message': str(e)})
        return response, 502


@songs.route('/ratings/add', methods=["POST"])
def save_ratings():
    try:
        data = request.get_json(force=True)

        # Retrieve the user id from the user.
        userId = data['userId']

        # Add song ratings into our database.
        # In order to do that, we need to format the data retrieved. We use a helper Entity SongRating
        # SongRating(user id, matched user, spotify preview url, rating)
        songRatings = []
        for songRating in data['songRatings']:
            songRatings.append(SongRating(userId, songRating['matchedUserId'], songRating['spotify_url'],
                                          songRating['rating']))
        add_song_ratings(songRatings),

        # Add playlist ratings into our database.
        # In order to do that, we need to format the data retrieved. We use a helper Entity PlaylistRating
        # PlaylistRating(user id, matched user, spotify preview url, rating)
        playlistRatings = []
        for playlistRating in data['playlistRatings']:
            playlistRatings.append(PlaylistRating(userId, playlistRating['matchedUserId'], playlistRating['rating']))

        add_playlist_ratings(playlistRatings)

        # Everything has been successfully stored, return success message.
        return jsonify("Success")
    except DatabaseException as e:
        # Exception handling in case there is a database error.
        return redirect(frontend_url + "/error/database")


# Handle the Spotify login and access code retrieval.
@songs.route('/callback')
def spotify_log_in():
    try:
        # Retrieve the access token after user is logged in.
        access_token = get_access_token(request.args['code'])

        # Find top songs of the user.
        top_songs = get_top_songs_api(access_token)

        # Store the user in the database.
        userId = add_user(1)  # Batch Number hardcoded for now

        # Store top songs into our database.
        add_top_songs(userId, top_songs)

        # Redirect to first page of the questionnaire
        return redirect(frontend_url + "/page1?userID = " + str(userId), 200)

    except AuthorizationException as e:
        # Exception handling in case there is an authorization error.
        return redirect(frontend_url + "/error/login")

    except InvalidAccountException as e:
        # Exception handling in case there is an Invalid account error.
        return redirect(frontend_url + "/error/invalid_account")

    except DatabaseException as e:
        # Exception handling in case there is a database error.
        return redirect(frontend_url + "/error/database")
