import mysql.connector
from random import randint
from src.Services.database_config import DatabaseException, open_connection
from dotenv import load_dotenv
import os

load_dotenv()


# Method that stores all answers of a user to the database
# Parameters: a list of tuples containing: a user id, the question number and the user's answer
# Returns: A confirmation message
def add_answers(answers):
    try:
        db, cursor, database = open_connection()
        # The SQL statement for storing answers in the Answer table
        sql = "INSERT INTO " + database + ".Answer(UserId, QuestionNumber, Response) VALUES (%s, %s, %s)"

        cursor.executemany(sql, answers)
        if os.getenv('IS_TESTING'):
            db.rollback()
        else:
            db.commit()
        return "Success storing all Answers"

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding answers.")


# Method that stores a new user to the database
# Parameters: a batch id
# Returns: a user id
def add_user(batch_id):
    try:
        db, cursor, database = open_connection()
        cursor.execute("Insert Into " + database + ".Participant(Batch) Values (" + str(batch_id) + ")")

        participant_id = cursor.lastrowid

        if os.getenv('IS_TESTING'):
            db.rollback()
        else:
            db.commit()
        return participant_id

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when adding users.")


# Method that stores the value vector of a user to the database
# Parameters: a user id and a value vector
# Returns: A confirmation message
def add_value(user_id, values):
    try:
        # The SQL statement for storing a value in the Value table
        db, cursor, database = open_connection()
        sql = "INSERT INTO " + database + ".Value (ValueId, Stimulation, SelfDirection, Universalism" \
                                          ",Benevolence,Tradition, Conformity, SecurityVal, PowerVal, Achievement,Hedonism)" \
                                          " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (user_id, values[0], values[1], values[2], values[3], values[4],
               values[5], values[6], values[7], values[8], values[9])
        cursor.execute(sql, val)

        if os.getenv('IS_TESTING'):
            db.rollback()
        else:
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
        db, cursor, database = open_connection()
        sql = "INSERT INTO " + database + ".Personality (PersonalityId, Openness, Honesty, Emotionality" \
                                          ", Extroversion, Agreeableness, Conscientiousness) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (user_id, personality[0], personality[1], personality[2],
               personality[3], personality[4], personality[5])
        cursor.execute(sql, val)

        if os.getenv('IS_TESTING'):
            db.rollback()
        else:
            db.commit()

        return "Success storing personality"

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding personalities.")


# Returns user's value score and takes userId is input
def get_value(userId):
    try:
        db, cursor, database = open_connection()
        sql = "Select Stimulation, SelfDirection, Universalism, Benevolence," \
              " Tradition, Conformity, SecurityVal, PowerVal, Achievement, Hedonism " \
              "From " + database + ".value as v Where v.ValueId = " + str(userId)
        cursor.execute(sql)

        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when trying to retrieve values.")


# Returns user's personality score and takes userId as input
def get_personality(userId):
    try:
        db, cursor, database = open_connection()
        sql = "Select Openness, Honesty, Emotionality," \
              "Extroversion, Agreeableness, Conscientiousness " \
              "From " + database + ".personality as pe Where pe.PersonalityId = " + str(userId)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when trying to retrieve personality.")


# Method that stores a user and his matches on personality and value and a random other user
# Parameters: a user id , a value user id, a personality user id and a random user id
# Returns: A confirmation message
def add_matches(userId, val_user, pers_user, random_user):
    try:
        # The SQL statement for storing user id and matches in the Match table
        db, cursor, database = open_connection()
        sql = "INSERT INTO Recommender.Match (UserId, ValId, PersId, RandId) VALUES (%s, %s, %s, %s)"
        val = (userId, val_user, pers_user, random_user)
        cursor.execute(sql, val)

        if os.getenv('IS_TESTING'):
            db.rollback()
        else:
            db.commit()

        return "Success storing personality"

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding personalities.")


# Method that gets all the users of a certain batch and their values
# Parameters: batch number
# Returns: a list of tuples containing user and his values
def get_all_values(batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select UserId, Stimulation, SelfDirection, Universalism, Benevolence," \
              " Tradition, Conformity, SecurityVal, PowerVal, Achievement, Hedonism " \
              "From " + database + ".value as v , " + database + ".participant as p " \
                                                                 "Where v.ValueId = p.UserId and p.Batch = " + str(
            batch)

        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when retrieving values.")


# Method that gets all the users of a certain batch and their personalities
# Parameters: batch number
# Returns: a list of tuples containing user and his personalities
def get_all_personalities(batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select UserID, Openness, Honesty, Emotionality," \
              "Extroversion, Agreeableness, Conscientiousness " \
              "From " + database + ".personality as pe , " \
              + database + ".participant as pa " \
                           "Where pe.PersonalityId = pa.UserId and pa.Batch = " + str(batch)

        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when retrieving personalities.")


# Method that gets all the users of a certain batch apart from the value user and personality user
# Parameters: batch number
# Returns: one random user id
def get_random_user(user1, user2, batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select UserID From " + database + ".participant as p " \
                                                 "Where p.Batch = " + str(batch) + " and not (p.UserID =" + str(
            user1) + " or p.UserID =  " + str(user2) + ")"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result[randint(0, len(result))][0]
    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when retrieving users.")
