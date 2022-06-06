import mysql.connector
from src.Services.database_config import DatabaseException, open_connection


# Method that gets all the users of a certain batch and their questionnaire scores
# Parameters: batch number
# Returns: a list of tuples containing userId and their scores
def get_all_scores(batch, db, cursor, database):
    try:
        sql = "Select UserID, Openness, Honesty, Emotionality, Extroversion, Agreeableness, Conscientiousness," \
            " Stimulation, SelfDirection, Universalism, Benevolence, Tradition, Conformity, SecurityVal, PowerVal, " \
            "Achievement, Hedonism "\
            "From " + database + ".Personality as pe Inner Join " + database + ".Participant as pa on pe.PersonalityId="\
            "pa.UserId Inner Join " + database + ".value as v on v.ValueId = pa.UserId Where pa.Batch = %s"

        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


# Method that gets all the answers of users of a certain batch
# Parameters: batch number
# Returns: a list of tuples containing userId, question number, answer
def get_all_answers(batch, db, cursor, database):
    try:
        sql = "Select p.UserId, QuestionNumber, Response from " + database + ".Answer as a " \
              "Left Join recommender.Participant" \
              " as p on a.UserId=p.UserId Where p.Batch = %s"
        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


# Method that gets all the songs of users of a certain batch
# Parameters: batch number
# Returns: a list of tuples containing userId, spotify_url
def get_all_songs(batch, db, cursor, database):
    try:
        sql = "Select p.UserId, spotify_url from " + database + ".Song as s Left Join recommender.Participant" \
              " as p on s.UserId=p.UserId Where p.Batch = %s"
        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


