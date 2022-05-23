import mysql.connector
from src.Services.database_config import DatabaseException, open_connection


# Method that gets all the users of a certain batch and their personalities
# Parameters: batch number
# Returns: a list of tuples containing user and his personalities
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
