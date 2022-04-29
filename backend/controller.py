import json

from flask import Flask, request, jsonify
from service import store
from psychology import calculations

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

    # TODO: implement value and personality calculations
    values, personalities = calculations(val_answers, pers_answers)

    # TODO: store all data into our database
    store(user_id, val_answers, pers_answers, values, personalities, spoti)

    return jsonify(user_id=user_id, val_answers=val_answers, pers_answers=pers_answers, spoti=spoti)


if __name__ == "__main__":
    app.run(debug=True)
