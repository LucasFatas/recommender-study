import json

from flask import request, redirect, Blueprint, jsonify

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
        top_songs = get_top_songs(data['userId'])
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
        values = get_value(userId)
        personality = get_personality(userId)

        val_user, pers_user, random_user = match(userId, values, personality, 1, data['metric'])

        # TODO: Return ID of the matched users as well
        lst = [get_top_songs(val_user), get_top_songs(pers_user), get_top_songs(random_user)]

        jsonifiable = []
        matched = []
        for match_list in lst:
            for song in match_list:
                matched.append(song.__dict__)
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
        userId = data['userId']
        songRatings = []
        for songRating in data['songRatings']:
            songRatings.append(SongRating(userId, songRating['matchedUserId'], songRating['spotify_url'],
                                          songRating['rating']))
        add_song_ratings(songRatings),

        playlistRatings = []
        for playlistRating in data['playlistRatings']:
            playlistRatings.append(PlaylistRating(userId, playlistRating['matchedUserId'], playlistRating['rating']))

        add_playlist_ratings(playlistRatings)
        return jsonify("Success")
    except DatabaseException as e:
        # Exception handling in case there is a database error.
        response = jsonify({'message': str(e)})
        return response, 502


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

        add_top_songs(userId, top_songs)

        # Redirect to first page of the questionnaire
        return redirect(frontend_url + "/questionnaire/page1?userID = " + str(userId), 302)

    except AuthorizationException as e:
        # Exception handling in case there is an authorization error.
        return redirect(frontend_url + "/error/login")

    except InvalidAccountException as e:
        # Exception handling in case there is an authorization error.
        return redirect(frontend_url + "/error/invalid_account")

    except DatabaseException as e:
        # Exception handling in case there is a database error.
        return redirect(frontend_url + "/error/database")
