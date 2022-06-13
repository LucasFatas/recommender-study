import os
from dotenv import set_key, find_dotenv
from flask import request, Blueprint, jsonify

from src.Controllers.Dashboard.DashboardLoginController import check_token, dashboard
from src.Services.DashboardService import get_user_total
from src.Services.database_config import open_connection
from src.spotify import AuthorizationException


@dashboard.route("/users")
def total_users():
    """
    Retrieves total number of users that have filled out the questionnaires
    :except AuthorizationException: if the token provided has the wrong credentials
    :except KeyError: if the token provided is missing
    :return: a JSON object with the amount of users with a fulfilled questionnaire in the current branch
    """
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException:
        response = jsonify({'message': "Incorrect Token"})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

    batch = request.args['batchId']
    db, cursor, database = open_connection()

    users = get_user_total(batch, db, cursor, database)

    return jsonify(users=users)


@dashboard.route("/batch")
def get_batch():
    """
    Retrieves the batch number from the .env file
    :return: a JSON object with the batch number, can be either 1 or 2 so far.
    """
    # Authentication code block not needed because this needs to be accessed from other places (not just dashboard).
    batch = os.getenv('BATCH')

    return jsonify(batch=batch)


@dashboard.route("/metric")
def get_metric():
    """
    Retrieves the metric being employed by the experiment at that moment
    :except AuthorizationException: if the token provided has the wrong credentials
    :except KeyError: if the token provided is missing
    :return: a JSON object with the metric of the experiment
    """
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

    return jsonify(metric=metric)


@dashboard.route("/setBatch")
def set_batch():
    """
    Method that sets the experiment into a new batch, with the option to change the metric.
    :except AuthorizationException: if the token provided has the wrong credentials
    :except KeyError: if the token provided is missing
    :return: a JSON object with the new batch number and the metric employed
    """
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException:
        response = jsonify({'message': "Incorrect Token"})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

    asked_metric = request.args['metric']

    os.environ["BATCH"] = str(2)
    set_key(find_dotenv(), "BATCH", os.getenv("BATCH"))
    batch = os.environ["BATCH"]

    os.environ["METRIC"] = asked_metric
    set_key(find_dotenv(), "METRIC", os.getenv("METRIC"))
    metric = os.environ["METRIC"]

    return jsonify(batch=batch, metric=metric)


@dashboard.route("/revert", methods=['POST'])
def revert_batch():
    """
    Reverts the experiment to batch 1 and euclidean metric as default
    Method non-accessible by the dashboard, only for development purposes
    :except AuthorizationException: if the token provided has the wrong credentials
    :except KeyError: if the token provided is missing
    :return: a JSON object with the amount of users with a fulfilled experiment.
    """
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException:
        response = jsonify({'message': "Incorrect Token"})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

    os.environ["BATCH"] = str(1)
    set_key(find_dotenv(), "BATCH", os.getenv("BATCH"))
    batch = os.environ["BATCH"]

    os.environ["METRIC"] = "Euclidean"
    set_key(find_dotenv(), "METRIC", os.getenv("METRIC"))
    metric = os.environ["METRIC"]

    return jsonify(batch=batch)
