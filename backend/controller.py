import json

from flask import Flask, request, jsonify
from service import store
from psychology import calculations
from spotify import get_access_token, get_top_songs
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
    variable_name = request.get_json()
    user_id, val_answers, pers_answers, spoti = variable_name['user'], variable_name['val_answers'], \
                                                variable_name['pers_answers'], variable_name['spoti']

    # Calculations for the personality and values.
    # TODO: implement value and personality calculations
    values, personalities = calculations(val_answers, pers_answers)

    # Store all of the data gathered into our database.
    # TODO: store all data into our database
    store(user_id, val_answers, pers_answers, values, personalities, spoti)

    # Process successful, return results for frontend to show to the user.
    return jsonify(values=values, personalities=personalities)


@app.route('/callback')
def spotifyLogIn():
    access_token = get_access_token(request.args['code'])
    return json.dumps(get_top_songs(access_token))


if __name__ == "__main__":
    app.run(debug=True, port=3000)
