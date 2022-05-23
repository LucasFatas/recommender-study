from flask import request, jsonify, Blueprint

from src.Computation.psychology import calculations
from src.Services.database_config import DatabaseException

from src.Services.QuestionnaireService import add_answers, add_value, add_personality

questionnaire = Blueprint("questionnaire", __name__)


# Get answers and save them into the database.
@questionnaire.route("/answer/add", methods=["POST"])
def save_answer():
    data = request.get_json(force=True)

    # Format answers retrieved from frontend into our database format to store the data.
    # Format: UserId, question number, answer.
    answers = []

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

    add_value(data['user'], value)

    add_personality(data['user'], personality)

    # Process successful, return results for frontend to show to the user.
    return jsonify(values=value, personalities=personality)
