import io, csv
import os

import numpy as np
import flask
from flask import request, Blueprint, jsonify, make_response
from src.Services.DashboardService import get_all_scores, get_all_answers, get_all_songs, get_all_match_data, get_song_ratings
from src.Services.database_config import open_connection
from dotenv import load_dotenv
import jwt

from src.spotify import AuthorizationException

dashboard = Blueprint('dashboard', __name__)


# Method that gets all the users of a certain batch and their questionnaire scores
# Parameters: batch number
# Returns: a list of tuples containing userId and their scores
@dashboard.route("/scores")
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
    batchId = request.args['batchId']

    batchId = request.args['batchId']

    scores = get_all_scores(batchId, db, cursor, database)

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
@dashboard.route("/answers")
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
    batchId = request.args['batchId']

    batchId = request.args['batchId']

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
@dashboard.route("/songs")
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
    batchId = request.args['batchId']

    batchId = request.args['batchId']

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


# Batch 2 information starts here.

# Method that gets all the match information of users being matched.
# Returns: a csv of tuples containing userId and the feedback provided based on the matches they got.
@dashboard.route("/match")
def retrieve_match_data():
    db, cursor, database = open_connection()

    # Retrieve data and number of questions per match from the service
    match_data, number_of_questions = get_all_match_data(db, cursor, database)

    data = io.StringIO()
    writer = csv.writer(data)

    # Since the number of questions is modifiable, we account for that by building the column names in three batches,
    # one per match.
    column_names = ["UserID", "Value_Match_Id", "Value_Match_Rating"]
    for i in range(number_of_questions):
        # Store Number of the question.
        column_names.append("Value_Match_Q" + str(i + 1))
    column_names.append("Value_Match_Open_Feedback")

    column_names.append("Personality_Match_Id")
    column_names.append("Personality_Match_Rating")
    for i in range(number_of_questions):
        # Store Number of the question.
        column_names.append("Personality_Match_Q" + str(i + 1))
    column_names.append("Personality_Match_Open_Feedback")

    column_names.append("Random_Match_Id")
    column_names.append("Random_Match_Rating")
    for i in range(number_of_questions):
        # Store Number of the question.
        column_names.append("Random_Match_Q" + str(i + 1))
    column_names.append("Random_Match_Open_Feedback")

    # Write the columns calculated to the CSV file.
    writer.writerow(tuple(column_names))

    # Will store the answers for all the questions across matches.
    for row in match_data:
        final_row = [row[0], row[1], row[2]]
        final_row.extend(int(i) for i in row[3].split(","))
        final_row.extend([row[4], row[5], row[6], row[7]])
        final_row.extend(int(i) for i in row[8].split(","))
        final_row.extend([row[9], row[10], row[11], row[12]])
        final_row.extend(int(i) for i in row[13].split(","))
        final_row.append(row[14])

        writer.writerow(final_row)

    output = make_response(data.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output


# Method that gets all the song ratings of matched users.
# Returns: a csv of tuples containing userId and the song ratings for each rating, 0 if there is no rating
@dashboard.route("/songRatings")
def retrieve_song_ratings():
    db, cursor, database = open_connection()

    # Retrieve data and number of questions per match from the service.
    # Data is returned as userId and three strings containing the information about which songs have been answered.
    # Strings are formatted as such: "songNumber-rating, songNumber-rating" and it has maximum five elements.
    rows = get_song_ratings(db, cursor, database)

    data = io.StringIO()
    writer = csv.writer(data)

    # Since the number of questions is set, we can build our column titles straight away.
    column_names = (
                    "UserId", "Values_Song_1_Rating", "Values_Song_2_Rating", "Values_Song_3_Rating",
                    "Values_Song_4_Rating",	"Values_Song_5_Rating",	"Personality_Song_1_Rating",
                    "Personality_Song_2_Rating", "Personality_Song_3_Rating", "Personality_Song_4_Rating",
                    "Personality_Song_5_Rating", "Random_Song_1_Rating", "Random_Song_2_Rating", "Random_Song_3_Rating",
                    "Random_Song_4_Rating", "Random_Song_5_Rating"
    )

    # Write the columns calculated to the CSV file.
    writer.writerow(column_names)

    for row in rows:
        # Add userId of the user.
        final_row = [row[0]]

        # Add ratings to value related songs. Result is given in a string, so some string formatting needed.
        value_song_ratings = np.zeros(5)
        for rating in row[1].split(","):
            value_song_ratings[int(rating.split('-')[0]) - 1] = int(rating.split('-')[1])
        final_row.extend(value_song_ratings)

        # Add ratings to personality related songs. Result is given in a string, so some string formatting needed.
        personality_song_ratings = np.zeros(5)
        for rating in row[2].split(","):
            personality_song_ratings[int(rating.split('-')[0]) - 1] = int(rating.split('-')[1])
        final_row.extend(personality_song_ratings)

        # Add ratings to randomly recommended songs. Result is given in a string, so some string formatting needed.
        random_song_ratings = np.zeros(5)
        for rating in row[3].split(","):
            random_song_ratings[int(rating.split('-')[0]) - 1] = int(rating.split('-')[1])
        final_row.extend(random_song_ratings)

        # Write the final formatted row.
        writer.writerow(final_row)

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





