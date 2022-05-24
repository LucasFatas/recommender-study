import mysql.connector
from src.Services.database_config import DatabaseException, open_connection


# Method that gets all the users of a certain batch and their questionnaire scores
# Parameters: batch number
# Returns: a list of tuples containing userId and their scores
def get_all_scores(batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select UserID, Openness, Honesty, Emotionality, Extroversion, Agreeableness, Conscientiousness," \
            " Stimulation, SelfDirection, Universalism, Benevolence, Tradition, Conformity, SecurityVal, PowerVal, " \
            "Achievement, Hedonism "\
            "From recommender.personality as pe Inner Join recommender.participant as pa on pe.PersonalityId = "\
            "pa.UserId Inner Join recommender.value as v on v.ValueId = pa.UserId Where pa.Batch = %s"

        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


# Method that gets all the answers of users of a certain batch
# Parameters: batch number
# Returns: a list of tuples containing userId, question number, answer
def get_all_answers(batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select p.UserId, QuestionNumber, Response from recommender.Answer as a Left Join recommender.participant" \
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
def get_all_songs(batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select p.UserId, spotify_url from recommender.song as s Left Join recommender.participant" \
              " as p on s.UserId=p.UserId Where p.Batch = %s"
        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


