from flask import request, jsonify, Blueprint

from src.Computation.psychology import calculations
from src.Services.database_config import DatabaseException
from src.Services.database_config import open_connection
from src.Services.QuestionnaireService import add_answers, add_personality, add_value


questionnaire = Blueprint("questionnaire", __name__)
db, cursor, database = open_connection()


# Get answers and save them into the database.
@questionnaire.route("/answer/add", methods=["POST"])
def save_answer():
    data = request.get_json(force=True)

    # Format answers retrieved from frontend into our database format to store the data.
    # Format: user, question number, answer.
    answers = []

    # Personality answers formatting
    for index, answer in enumerate(data['personality_answers']):
        answers.append((data['user'], index, answer))

    # Value answers formatting
    for index, answer in enumerate(data['value_answers']):
        answers.append((data['user'], len(data['personality_answers']) + index, answer))

    try:
        # Add the newly formatted answers to our database.
        add_answers(answers, db, cursor, database)
    except DatabaseException as e:
        # Exception handling in case there is an error.
        response = jsonify({'message': str(e)})
        return response, 502

    # Calculate value and personality scores.
    value, personality = calculations(data['value_answers'], data['personality_answers'])
    add_personality(data['user'], personality, db, cursor, database)
    add_value(data['user'], value, db, cursor, database)

    # Process successful, return results for frontend to show to the user.
    return jsonify(values=value, personalities=personality)
