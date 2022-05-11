from flask import Flask, request, jsonify, redirect
from src.service import add_user, add_answers, DatabaseException
from src.psychology import calculations
from src.spotify import get_access_token, get_top_songs, AuthorizationException
import json
from flask_cors import CORS
from werkzeug.wrappers.response import Response

app = Flask(__name__)
CORS(app)

frontend_url = "http://www.localhost.com/3000"


# Beginning of endpoint methods
# Spoof endpoint to test connection.
@app.route("/")
def main_connection():
    return "Connection is working"


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


# Handle the Spotify login and access code retrieval.
@app.route('/callback')
def spotify_log_in():
    try:
        # Retrieve the access token after user is logged in.
        access_token = get_access_token(request.args['code'])

        # Find top songs of the user.
        songs = json.dumps(get_top_songs(access_token))

        # Store the user in the database.
        userId = add_user(1)  # Batch Number hardcoded for now

        # TODO: add songs to the database. (according to user)
        # add_songs(songs)
        return redirect(frontend_url + "/page1?userID = " + userId, 200)

    except AuthorizationException as e:
        # Exception handling in case there is an authorization error.
        response = Response(str(e))
        return redirect(frontend_url + "/error/login")

    except DatabaseException as e:
        # Exception handling in case there is a database error.
        response = Response(str(e))
        return redirect(frontend_url + "/error/database")


def create_app():
    with open('../config.json', 'r') as f:
        config = json.load(f)
    app.run(debug=True, port=config['port'])


if __name__ == "__main__":
    create_app()

