import json

from flask import request, redirect, Blueprint

from src.Entities.SongRating import SongRating
from src.Services.QuestionnaireService import add_user
from src.Services.database_config import DatabaseException
from src.Services.SongService import get_top_songs, add_top_songs, add_playlist_ratings, add_song_ratings
from src.spotify import get_access_token, get_top_songs_api, AuthorizationException, InvalidAccountException

songs = Blueprint('songs', __name__)
frontend_url = "http://www.localhost.com/3000"


@songs.route('/songs/get')
def retrieve_top_songs():
    try:
        data = request.get_json(force=True)
        top_songs = get_top_songs(data['userId'])
        return json.dumps(top_songs)
    except DatabaseException as e:
        # Exception handling in case there is a database error.
        return redirect(frontend_url + "/error/database")

@app.route('match')
def match_user():
    data = request.get_json(force=True)
    userId = data['user']

    try:
        # Add the newly formatted answers to our database.
        values = get_value(userId)
        personality = get_personality(userId)

        val_user, pers_user, random_user = match(userId, values, personality, data['metric'])

        lst = [get_songs[val_user], get_songs[pers_user], get_songs[random_user]]

        # TODO return list as a json
        return

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
        for playlistRatings in data['playlistRatings']:
            playlistRatings.append(SongRating(userId, playlistRatings['matchedUserId'], playlistRatings['rating']))

        add_playlist_ratings(playlistRatings)
        return "Success"
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

        add_top_songs(userId, top_songs)

        # Redirect to first page of the questionnaire
        return redirect(frontend_url + "/page1?userID = " + str(userId), 200)

    except AuthorizationException as e:
        # Exception handling in case there is an authorization error.
        return redirect(frontend_url + "/error/login")

    except InvalidAccountException as e:
        # Exception handling in case there is an authorization error.
        return redirect(frontend_url + "/error/invalid_account")

    except DatabaseException as e:
        # Exception handling in case there is a database error.
        return redirect(frontend_url + "/error/database")
