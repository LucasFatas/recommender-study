import json

from flask import Flask, request, jsonify
from service import store
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
    variable_name = request.get_json()
    user_id, answers, batch = variable_name['user'], variable_name['answers'], variable_name['batch']

    # Calculations for the personality and values.
    # TODO: implement value and personality calculations
    #values, personalities = calculations(answers)

    # Store the data gathered about the participant into our database.
    # TODO: store user into DB
    store_user(user_id, 4, 2, batch)

    # TODO: store answers into our database
    store_answer(user_id, answers, 1)


    # Process successful, return results for frontend to show to the user.
    #return jsonify(values=values, personalities=personalities)
    return "It Works"


@app.route('/callback')
def spotifyLogIn():
    try:
        access_token = get_access_token(request.args['code'])
        return json.dumps(get_top_songs(access_token))
    except AuthorizationException as e:
        response = jsonify({'message': str(e)})
        return response, 401


if __name__ == "__main__":
    app.run(debug=True, port=3000)
