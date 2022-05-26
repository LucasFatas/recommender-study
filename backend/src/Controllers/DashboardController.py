import io, csv
import numpy as np
from flask import request, Blueprint, jsonify, make_response

from src.Services.DashboardService import get_all_scores, get_all_answers, get_all_songs, get_all_match_data

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


# Batch 2 information starts here.
# Method that gets all the match information of users being matched.
# Parameters: batch number
# Returns: a csv of tuples containing userId and the feedback provided based on the matches they got.
@dashboard.route("/match")
def retrieve_match_data():
    # Retrieve data and number of questions per match from the service
    match_data, number_of_questions = get_all_match_data()

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

    # Data computation starts here
    i = 0
    # Will store the answers for all the questions across matches.
    answers = np.zeros(number_of_questions*3)
    for row in match_data:
        # We add entries to the answer array, checking all the combinations.
        if i < pow(number_of_questions, 3) - 1:
            # If all answers have been recorded, continue with the for loop, avoids unnecessary checks.
            if answers.all():
                i = i + 1
                continue
            # Record answers of first match.
            if answers[row[3]-1] == 0:
                answers[row[3] - 1] = row[4]
            # Record answers of second match.
            if answers[number_of_questions + row[8] - 1] == 0:
                answers[number_of_questions + row[8]-1] = row[9]
            # Record answers of third match.
            if answers[2 * number_of_questions + row[13] - 1] == 0:
                answers[2 * number_of_questions + row[13]-1] = row[14]
            i = i + 1

        else:
            # Add userId, matchedUserId and rating of first match (values).
            final_row = [row[0], row[1], row[2]]
            for answer in answers[0: number_of_questions]:
                # Add answer for each question.
                final_row.append(answer)

            # Add feedback of first match, matchedUserId and rating of second match (personality).
            final_row.extend([row[5], row[6], row[7]])
            for answer in answers[number_of_questions: 2 * number_of_questions]:
                # Add answer for each question.
                final_row.append(answer)

            # Add feedback of second match, matchedUserId and rating of third match (random).
            final_row.extend([row[10], row[11], row[12]])
            for answer in answers[2*number_of_questions:]:
                # Add answer for each question.
                final_row.append(answer)
            final_row.append(row[15])

            # Write the row after formatting correctly.
            writer.writerow(final_row)
            # Reset variables for handling of new match.
            i = 0
            answers = np.zeros(number_of_questions*3)

    output = make_response(data.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output

