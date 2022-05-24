import io, csv
from flask import request, Blueprint, jsonify, make_response

from src.Services.DashboardService import get_all_scores, get_all_answers, get_all_songs

dashboard = Blueprint('dashboard', __name__)


# Method that gets all the users of a certain batch and their questionnaire scores
# Parameters: batch number
# Returns: a list of tuples containing userId and their scores
@dashboard.route("/scores")
def retrieve_scores():
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
@dashboard.route("/answers")
def retrieve_answers():
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
@dashboard.route("/songs")
def retrieve_songs_from_batch():
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


