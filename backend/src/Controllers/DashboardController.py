import io, csv
import os

import flask
from flask import request, Blueprint, jsonify, make_response
from src.Services.DashboardService import get_all_scores, get_all_answers, get_all_songs, get_user_total
from src.Services.database_config import open_connection
from dotenv import load_dotenv, set_key, find_dotenv
import jwt

from src.spotify import AuthorizationException

dashboard = Blueprint('dashboard', __name__)

"""Start of CSV retrieval methods."""


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

    db, cursor, database = open_connection()

    batchId = request.get_json(force=True)['batchId']

    scores = get_all_scores(batchId, db, cursor, database)

    data = io.StringIO()
    writer = csv.writer(data)
    column_names = (
        "UserID", "Openness", "Honesty", "Emotionality", "Extroversion", "Agreeableness", "Conscientiousness",
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

    db, cursor, database = open_connection()

    batchId = request.get_json(force=True)['batchId']

    scores = get_all_answers(batchId, db, cursor, database)

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
    except AuthorizationException as e:
        response = jsonify({'message': str(e)})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

    db, cursor, database = open_connection()

    batchId = request.get_json(force=True)['batchId']

    scores = get_all_songs(batchId, db, cursor, database)

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


"""Start of experiment parameter manipulation methods."""


# Method that gets all the total users of a certain batch
# Parameters: batch number
# Returns: total number of users.
@dashboard.route("/users")
def total_users():
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException:
        response = jsonify({'message': "Incorrect Token"})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

    batch = request.args['batch']
    db, cursor, database = open_connection()

    users = get_user_total(batch, db, cursor, database)

    return users


# Method that gets the batch the experiment is at.
# Returns: the stored batch number.
@dashboard.route("/batch")
def get_batch():
    # Authentication not needed because this needs to be accessed from other places (not just dashboard).
    batch = os.environ['BATCH']

    return batch


# Method that gets the metric employed by the experiment
# Returns: a string with either "euclidean" or "manhattan"
@dashboard.route("/metric")
def get_metric():
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException:
        response = jsonify({'message': "Incorrect Token"})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

    # If batch number is 1, then metric will be euclidean as default,
    # but it's not used at any point by the app when batch is 1
    metric = os.environ['METRIC']

    return jsonify(metric)


# Method that sets the experiment to the next batch.
# Parameters: metric employed.
# Returns: the batch number and the metric employed.
@dashboard.route("/setBatch", methods=["POST"])
def set_batch():
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException:
        response = jsonify({'message': "Incorrect Token"})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401
    
    asked_metric = request.get_json(force=True)['metric']

    os.environ["BATCH"] = str(2)
    set_key(find_dotenv(), "BATCH", os.getenv("BATCH"))
    batch = os.environ["BATCH"]

    os.environ["METRIC"] = asked_metric
    set_key(find_dotenv(), "METRIC", os.getenv("METRIC"))
    metric = os.environ["METRIC"]

    return str(batch) + ", " + metric


"""Authentication related methods"""


# Method that creates the JWT token of the researcher
# Parameters: username, password
# Returns: jwt token
@dashboard.route("/login", methods=["POST"])
def create_token():
    data = request.get_json(force=True)
    load_dotenv()
    username = data['username']
    password = data['password']

    if os.environ.get("RESEARCHER_USERNAME") != username or os.environ.get("RESEARCHER_PASSWORD") != password:
        response = jsonify({'message': "Unsuccessful login"})
        return response, 401
    else:
        credentials = {
            "username": username,
            "password": password
        }

        return flask.jsonify(token=jwt.encode(credentials, os.environ.get("KEY"), algorithm="HS256"))


# Method that checks JWT tokens
# Parameters: jwt token in auth header
# Returns: true or false
def check_token(token):
    try:
        decoded = jwt.decode(token, os.environ.get("KEY"), algorithms="HS256")
        username = decoded['username']
        password = decoded['password']

        if os.environ.get("RESEARCHER_USERNAME") != username or os.environ.get("RESEARCHER_PASSWORD") != password:
            raise AuthorizationException("Incorrect Token")
        else:
            return True
    except jwt.exceptions.DecodeError:
        raise AuthorizationException("Incorrect Token")
