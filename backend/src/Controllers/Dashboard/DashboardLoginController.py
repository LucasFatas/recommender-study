import os
import flask
import jwt
from dotenv import load_dotenv
from flask import request, Blueprint, jsonify

from src.spotify import AuthorizationException

loginDashboard = Blueprint('dashboard/login', __name__)


@loginDashboard.route("", methods=["POST"])
def create_token():
    """
    This method checks the credentials provided to us by the frontend when the researcher is logging in to the dashboard
    :return: a token containing the encoded credentials if they provided to the server are correct
    Otherwise, it returns an error message
    """
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


def check_token(token):
    """
    It checks if a given token contains the correct credentials
    :param token: token provided by frontend
    :except AuthorizationException: if the credentials are wrong or non-decodable.
    :return: True only if credentials are correct.
    """
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
