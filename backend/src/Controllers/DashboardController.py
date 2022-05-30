import io, csv
import os

from flask import request, Blueprint, jsonify, make_response
from src.Services.DashboardService import get_all_scores, get_all_answers, get_all_songs
from dotenv import load_dotenv
import jwt

from src.spotify import AuthorizationException

dashboard = Blueprint('dashboard', __name__)


# Method that gets all the users of a certain batch and their questionnaire scores
# Parameters: batch number
# Returns: a list of tuples containing userId and their scores
@dashboard.route("/scores", methods=["POST"])
def retrieve_scores():
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException:
        response = jsonify({'message': "Incorrect Token"})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

    batchId = request.get_json(force=True)['batchId']

    scores = get_all_scores(batchId)

    data = io.StringIO()
    writer = csv.writer(data)
    column_names = ("UserID", "Openness", "Honesty", "Emotionality", "Extroversion", "Agreeableness", "Conscientiousness",
                   "Stimulation", "SelfDirection", "Universalism", "Benevolence", "Tradition", "Conformity", "SecurityVal",
                   "PowerVal", "Achievement", "Hedonism")
    writer.writerow(column_names)
    for row in scores:
        writer.writerow(row)

    output = make_response(data.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output


# Method that gets all the answers of users of a certain batch
# Parameters: batch number
# Returns: a list of tuples containing userId, question number, answer
@dashboard.route("/answers", methods=["POST"])
def retrieve_answers():
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException:
        response = jsonify({'message': "Incorrect Token"})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

    batchId = request.get_json(force=True)['batchId']

    scores = get_all_answers(batchId)

    data = io.StringIO()
    writer = csv.writer(data)
    column_names = ("UserId", "QuestionNumber", "Answer")
    writer.writerow(column_names)
    for row in scores:
        writer.writerow(row)

    output = make_response(data.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output


# Method that gets all the songs of users of a certain batch
# Parameters: batch number
# Returns: a csv of tuples containing userId, spotify_url
@dashboard.route("/songs", methods=["POST"])
def retrieve_songs_from_batch():
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException:
        response = jsonify({'message': "Incorrect Token"})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

    batchId = request.get_json(force=True)['batchId']

    scores = get_all_songs(batchId)

    data = io.StringIO()
    writer = csv.writer(data)
    column_names = ("UserId", "SpotifyUrl")
    writer.writerow(column_names)
    for row in scores:
        writer.writerow(row)

    output = make_response(data.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output


# Method that creates the JWT token of the researcher
# Parameters: username, password
# Returns: jwt token
@dashboard.route("/login", methods=["POST"])
def create_token():
    data = request.get_json(force=True)
    load_dotenv()
    username = data['username']
    password = data['password']

    if os.environ.get("USERNAME") != username or os.environ.get("PASSWORD") != password:
        response = jsonify({'message': "Unsuccessful login"})
        return response, 401
    else:
        credentials = {
            "username": username,
            "password": password
        }

    return jwt.encode(credentials, os.environ.get("KEY"), algorithm="HS256")


# Method that checks JWT tokens
# Parameters: jwt token in auth header
# Returns: true or false
def check_token(token):

    decoded = jwt.decode(token, os.environ.get("KEY"), algorithms="HS256")
    username = decoded['username']
    password = decoded['password']

    if os.environ.get("USERNAME") != username or os.environ.get("PASSWORD") != password:
        raise AuthorizationException("Incorrect Token")
    else:
        return True





