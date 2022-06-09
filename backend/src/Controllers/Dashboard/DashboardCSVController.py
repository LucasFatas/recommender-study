import csv
import io

import numpy as np
from flask import request, Blueprint, jsonify, make_response

from src.Controllers.Dashboard.DashboardLoginController import check_token
from src.Services.DashboardService import get_all_scores, get_all_answers, get_all_songs, get_all_match_data, \
    get_song_ratings
from src.Services.database_config import open_connection
from src.spotify import AuthorizationException

CSVDashboard = Blueprint('dashboard/csv', __name__)


@CSVDashboard.route("/scores")
def retrieve_scores():
    """
    Retrieves CSV file containing tuples of userId, value scores and personality scores
    :except AuthorizationException: if the token provided has the wrong credentials
    :except KeyError: if the token provided is missing
    :return: a csv/text object with the scores of all the users in the given batch
    """
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

    scores = get_all_scores(batchId, db, cursor, database)

    data = io.StringIO()
    writer = csv.writer(data)
    column_names = (
        "UserID", "Honesty", "Emotionality", "Extroversion", "Agreeableness", "Conscientiousness", "Openness",
        "Stimulation", "SelfDirection", "Universalism", "Benevolence", "Tradition", "Conformity", "SecurityVal",
        "PowerVal", "Achievement", "Hedonism")
    writer.writerow(column_names)
    for row in scores:
        writer.writerow(row)

    output = make_response(data.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output


@CSVDashboard.route("/answers")
def retrieve_answers():
    """
    Retrieves CSV file containing tuples of userId, question number and answer for that question
    :except AuthorizationException: if the token provided has the wrong credentials
    :except KeyError: if the token provided is missing
    :return: a csv/text object with the answers of all the users in the given batch
    """
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


@CSVDashboard.route("/songs")
def retrieve_songs_from_batch():
    """
    Retrieves CSV file containing tuples of userId and spotify url of each user's top 5 songs.
    :except AuthorizationException: if the token provided has the wrong credentials
    :except KeyError: if the token provided is missing
    :return: a csv/text object with the songs of all the users in th provided branch
    """
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


@CSVDashboard.route("/match")
def retrieve_match_data():
    """
    Retrieves CSV file containing tuples of userId, matchedUserId and the feedback provided for the recommendation
    of that matchedUserId, for each of the matches.
    This method can only be accessed when the experiment is in batch 2 mode
    :except AuthorizationException: if the token provided has the wrong credentials
    :except KeyError: if the token provided is missing
    :return: a csv/text object with the feedback of all the matches generated by our app
    """
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException as e:
        response = jsonify({'message': str(e)})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

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


@CSVDashboard.route("/songRatings")
def retrieve_song_ratings():
    """
    Retrieves CSV file containing tuples of userId, matchedUserId and the feedback provided for the songs recommended to
    them for that matchedUserId, for each of the matches.
    This method can only be accessed when the experiment is in batch 2 mode
    :except AuthorizationException: if the token provided has the wrong credentials
    :except KeyError: if the token provided is missing
    :return: a csv/text object with the ratings of all the songs recommended to our user
    """
    try:
        check_token(request.headers['Authorization'].replace("Bearer ", ""))
    except AuthorizationException as e:
        response = jsonify({'message': str(e)})
        return response, 401
    except KeyError:
        response = jsonify({'message': "Missing Token"})
        return response, 401

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
