import json

from flask import Flask, request, jsonify
from service import store_answers, store_calculations
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
    user_id, val_answers, pers_answers = variable_name['user'], variable_name['val_answers'], variable_name['pers_answers']

    # Calculations for the personality and values.
    # TODO: implement value and personality calculations
    values, personalities = calculations(val_answers, pers_answers)

    # Store the data gathered about the participant into our database.
    # TODO: store data into our database
    store_answers(user_id, val_answers, pers_answers)

    # Store the data copmuted about the participant's personality into our database.
    # TODO: store data into our database
    store_calculations(user_id, values, personalities)


    # Process successful, return results for frontend to show to the user.
    return jsonify(values=values, personalities=personalities)


if __name__ == "__main__":
    app.run(debug=True)
