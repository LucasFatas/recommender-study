import mysql.connector
import json


class DatabaseException(Exception):
    pass


def open_connection():

    with open('config.json', 'r') as f:
        configuration = json.load(f)

    if configuration['is_testing']:
        database = configuration['test_database']
    else:
        database = configuration['database']

    db = mysql.connector.connect(
        # Change once it is no longer hosted
        host="localhost",
        user="dani",
        passwd="root",
        database=database
    )

    cursor = db.cursor()

    return db, cursor


# Method that stores all answers of a user to the database
# Parameters: a list of tuples containing: a user id, the question number and the user's answer
# Returns: A confirmation message
def add_answers(answers):
    try:
        db, cursor = open_connection()
        sql = """INSERT INTO Recommender.Answer(ParticipantId, QuestionNumber, Response) VALUES (%s, %s, %s)"""
        # The SQL statement for storing answers in the Answer table
        sql = "INSERT INTO Recommender.Answer(UserId, QuestionNumber, Response) VALUES (%s, %s, %s)"

        cursor.executemany(sql, answers)
        db.commit()
        return "Success storing all Answers"

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding answers.")


# Method that stores a new user to the database
# Parameters: a batch id
# Returns: a user id
def add_user(batch_id):
    try:
        db, cursor = open_connection()
        cursor.execute("Insert Into Recommender.Participant(Batch) Values(2)")

        participant_id = cursor.lastrowid

        db.commit()
        return participant_id

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding users.")


# Method that stores the value vector of a user to the database
# Parameters: a user id and a value vector
# Returns: A confirmation message
def add_value(user_id, values):
    try:
        # The SQL statement for storing a value in the Value table
        db, cursor = open_connection()
        sql = "INSERT INTO Recommender.Value (ValueId, Stimulation, SelfDirection, Universalism" \
              ",Benevolence,Tradition, Conformity, SecurityVal, PowerVal, Achievement,Hedonism)" \
              " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (user_id, values[0], values[1], values[2], values[3], values[4],
               values[5], values[6], values[7], values[8], values[9])
        cursor.execute(sql, val)
        db.commit()

        return "Success storing value"

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding values.")


# Method that stores the personality vector of a user to the database
# Parameters: a user id and a personality vector
# Returns: A confirmation message
def add_personality(user_id, personality):

    try:
        # The SQL statement for storing a personality in the Personality table
        db, cursor = open_connection()
        sql = "INSERT INTO Recommender.Personality (PersonalityId, Openness, Honesty, Emotionality" \
              ", Extroversion, Agreeableness, Conscientiousness VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (user_id, personality[0], personality[1], personality[2],
               personality[3], personality[4], personality[5], personality[6])
        cursor.execute(sql, val)
        db.commit()

        return "Success storing personality"

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding personalities.")


if __name__ == '__main__':
    add_value(2,(1,2,3,4,5,6,7,8,9,10))