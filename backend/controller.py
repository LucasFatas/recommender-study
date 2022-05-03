import json

from flask import Flask, request, jsonify
from service import add_user, add_answers
from psychology import calculations
from spotify import get_access_token, get_top_songs, AuthorizationException
import json

app = Flask(__name__)


# Beginning of endpoint methods

# Connection between frontend and backend test
@app.route("/")
def mainConnection():
    return "Connection is working"


# Get answers and save them into the database.
@app.route("/saveAnswer", methods=["POST"])
def save_answer():
    data = request.get_json()

    # Calculations for the personality and values.
    # TODO: implement value and personality calculations
    #values, personalities = calculations(answers)

    # TODO: store answers into our database
    answers = []

    for index, answer in enumerate(data['personality_answers']):
        answers.append((data['user'], index, answer))

    for index, answer in enumerate(data['value_answers']):
        answers.append((data['user'], len(data['personality_answers']) + index, answer))

    add_answers(answers)

    # Process successful, return results for frontend to show to the user.
    #return jsonify(values=values, personalities=personalities)
    return "It Works"


@app.route('/callback')
def spotifyLogIn():
    try:
        access_token = get_access_token(request.args['code'])
        songs = json.dumps(get_top_songs(access_token))
        add_user(1) # Batch Number hardcoded for now
        # add_songs(songs)
        return songs
    except AuthorizationException as e:
        response = jsonify({'message': str(e)})
        return response, 401


if __name__ == "__main__":
    app.run(debug=True, port=3000)
