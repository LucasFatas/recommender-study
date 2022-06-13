import mysql.connector
from src.Services.database_config import DatabaseException, open_connection
from random import randint
from src.Services.database_config import DatabaseException
from dotenv import load_dotenv
import os
import time
import random

load_dotenv()


def add_answers(answers, db, cursor, database):
    """
    Stores answers provided by the user in the questionnaire
    :param answers: list of ints symbolizing the answers to the questionnaires.
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: result with all the users of a provided batch along with their answers to the questionnaires
    """
    try:
        # The SQL statement for storing answers in the Answer table
        sql = """INSERT INTO """ + database + """.Answer(userId, questionNumber, response) VALUES (%s, %s, %s);"""

        cursor.executemany(sql, answers)

        # Commit only if we are not testing the application
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()
        return "Success storing all Answers"

    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding answers.")


def add_user(batch_id, db, cursor, database):
    """
    Stores a new user in the database
    :param batch_id: batch number of the experiment
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: id of the new user
    """
    try:
        cursor.execute("""INSERT INTO """ + database + """.Participant(batch) VALUES (%s);""", (batch_id,))

        participant_id = cursor.lastrowid

        time.sleep(1)

        # Commit only if we are not testing the application
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()
        return participant_id

    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding users.")


def add_value(user_id, values, db, cursor, database):
    """
    Stores PVQ questionnaire related answers of the user in the database
    :param user_id: id of the participant
    :param values: answers of the PVQ questionnaire
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: success message
    """
    try:
        # The SQL statement for storing a value in the Value table
        sql = """
            INSERT INTO """ + database + """.Value (userId, stimulation, selfDirection, universalism
            , benevolence, tradition, conformity, securityVal, powerVal,
            achievement, hedonism)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        val = (user_id, values[0], values[1], values[2], values[3], values[4],
               values[5], values[6], values[7], values[8], values[9])
        cursor.execute(sql, val)

        # Commit only if we are not testing the application
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()

        return "Success storing value"

    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding values.")


def add_personality(user_id, personality, db, cursor, database):
    """
    Stores HEXACO personality answers of a user in the database
    :param user_id: id of the participant
    :param personality: answers of the HEXACO questionnaire
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: success message
    """
    try:
        # The SQL statement for storing a personality in the Personality table
        sql = """
            INSERT INTO """ + database + """.Personality (userId, honesty, emotionality,
            extroversion, agreeableness, conscientiousness, openness)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        val = (user_id, personality[0], personality[1], personality[2],
               personality[3], personality[4], personality[5])
        cursor.execute(sql, val)

        # Commit only if we are not testing the application
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()

        return "Success storing personality"

    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding personalities.")


def get_value(user_id, db, cursor, database):
    """
        Returns value scores of a user
        :param user_id: id of the participant
        :param db: database object, handles the connection to our database
        :param cursor: cursor that executes the SQL commands in our database
        :param database: string of the database name we will be using
        :except mysql.connector.errors.Error: handles the case where the database has some errors
        :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
        :return: a tuple with userId and 10 value scores
        """
    try:
        sql = """
            SELECT stimulation, selfDirection, universalism, benevolence,
            tradition, conformity, securityVal, powerVal, achievement, hedonism
            FROM """ + database + """.Value AS v 
            WHERE v.userId = %s;
        """

        cursor.execute(sql, (user_id,))

        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when trying to retrieve values.")


def get_personality(user_id, db, cursor, database):
    """
    Returns personality scores of a user
    :param user_id: id of the participant
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: a tuple with userId and the 6 personality scores
    """
    try:
        sql = """
            SELECT openness, honesty, emotionality, extroversion, agreeableness, conscientiousness 
            FROM """ + database + """.Personality AS pe 
            WHERE pe.userId = %s
        """
        cursor.execute(sql, (user_id,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when trying to retrieve personality.")


def add_matches(user_id, val_user, pers_user, random_user, db, cursor, database):
    """
    Stores match information of a user in the database
    :param user_id: id of the participant
    :param val_user: id of the first match (value based match)
    :param pers_user: id of the second match (personality based match)
    :param random_user: id of the third match (random based match)
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: success message
    """
    try:
        # The SQL statement for storing user id and matches in the Match table
        sql = """
            INSERT INTO """ + database + """.Matches (userId, valueId, personalityId, randomId)
            VALUES (%s, %s, %s, %s)
        """

        val = (user_id, val_user, pers_user, random_user)
        cursor.execute(sql, val)

        # Commit only if we are not testing the application
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()

        return "Success storing personality"
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding personalities.")


def get_all_values(batch, db, cursor, database, pers_user):
    """
    Returns value scores of all users in a batch
    :param pers_user: the calculated personality user, since these two users can't be the same
    :param batch: batch to retrieve information about
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: a list of tuples with userId and 10 value scores
    """
    try:
        v_sql = """
            SELECT pa.userId, stimulation, selfDirection, universalism, benevolence, 
            tradition, conformity, securityVal, powerVal, achievement, hedonism 
            FROM """ + database + """.Value AS v , """ + database + """.Participant AS pa
            WHERE v.userId = pa.userId AND pa.batch = %s AND NOT pa.userId = %s
        """

        cursor.execute(v_sql, (batch, pers_user))
        result = cursor.fetchall()
        return result
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving values.")


def get_all_personalities(batch, db, cursor, database):
    """
    Returns personality scores of all users in a batch
    :param batch: batch to retrieve information about
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: a list of tuples with userId and 6 value scores
    """
    try:
        p_sql = """
            SELECT pa.userID, openness, honesty, emotionality, extroversion, agreeableness, conscientiousness 
            FROM """ + database + """.personality AS pe , """ + database + """.participant AS pa 
            WHERE pe.userId = pa.UserId AND pa.Batch = %s
        """

        cursor.execute(p_sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving personalities.")


def get_random_user(user1, user2, batch, db, cursor, database):
    """
        Retrieves all users that are not already matched and returns a random user from the set of users retrieved
        :param user1: value based matched user
        :param user2: personality based matched user
        :param batch: batch to retrieve information about
        :param db: database object, handles the connection to our database
        :param cursor: cursor that executes the SQL commands in our database
        :param database: string of the database name we will be using
        :except mysql.connector.errors.Error: handles the case where the database has some errors
        :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
        :return: a userId chosen at random from all the users in the batch that are not user1 or user2
        """
    try:
        sql = """
                SELECT pa.userId FROM """ + database + """.Participant AS pa
                WHERE pa.batch = %s AND NOT (pa.userId = %s OR pa.userId = %s)
            """

        cursor.execute(sql, (batch, user1, user2))
        result = cursor.fetchall()
        return random.choice(result)[0]

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving users.")
