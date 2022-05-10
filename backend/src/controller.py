from flask import Flask, request, jsonify, redirect
from src.service import add_user, add_answers, DatabaseException, get_top_songs, add_top_songs, add_playlist_ratings, add_song_ratings
from src.psychology import calculations
from src.spotify import get_access_token, get_top_songs_api, AuthorizationException
import json
from flask_cors import CORS
from src.Entities.SongRating import SongRating
from src.Entities.PlaylistRating import PlaylistRating

from werkzeug.wrappers import Response

app = Flask(__name__)
CORS(app)

frontend_url = "http://www.localhost.com/3000"


# Beginning of endpoint methods
# Spoof endpoint to test connection.
@app.route("/", methods=["GET"])
def main_connection():
    return jsonify(response="Connection is working")


# Get answers and save them into the database.
@app.route("/saveAnswer", methods=["POST"])
def save_answer():
    data = request.get_json(force=True)

    # Calculations for the personality and values.
    # TODO: implement value and personality calculations
    # values, personalities = calculations(answers)

    # TODO: store answers into our database
    answers = []

    # Format answers retrieved from frontend into our database format.
    # Format: UserId, question number, answer.

    # Personality answers formatting
    for index, answer in enumerate(data['personality_answers']):
        answers.append((data['user'], index, answer))

    # Value answers formatting
    for index, answer in enumerate(data['value_answers']):
        answers.append((data['user'], len(data['personality_answers']) + index, answer))

    try:
        # Add the newly formatted answers to our database.
        add_answers(answers)
    except DatabaseException as e:
        # Exception handling in case there is an error.
        response = jsonify({'message': str(e)})
        return response, 502

    # Calculate value and personality scores.
    value, personality = calculations(data['value_answers'], data['personality_answers'])

    # Process successful, return results for frontend to show to the user.
    return jsonify(values=value, personalities=personality)


@app.route('/songs/get')
def retrieve_top_songs():
    try:
        data = request.get_json(force=True)
        top_songs = get_top_songs(data['userId'])
        return json.dumps(top_songs)
    except DatabaseException as e:
        # Exception handling in case there is a database error.
        return redirect(frontend_url + "/error/database")


@app.route('/ratings/add', methods=["POST"])
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
@app.route('/callback')
def spotify_log_in():
    try:
        # Retrieve the access token after user is logged in.
        access_token = get_access_token(request.args['code'])

        # Find top songs of the user.
        songs = get_top_songs_api(access_token)

        # Store the user in the database.
        userId = add_user(1)  # Batch Number hardcoded for now

        add_top_songs(userId, songs)

        # Redirect to first page of the questionnaire
        return redirect(frontend_url + "/page1?userID = " + str(userId), 200)

    except AuthorizationException as e:
        # Exception handling in case there is an authorization error.
        return redirect(frontend_url + "/error/login")

    except DatabaseException as e:
        # Exception handling in case there is a database error.
        return redirect(frontend_url + "/error/database")


def create_app():
    with open('../config.json', 'r') as f:
        config = json.load(f)
    app.run(debug=True, port=config['port'])


if __name__ == "__main__":
    create_app()


