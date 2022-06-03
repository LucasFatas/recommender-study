import mysql.connector
from random import randint
from src.Services.database_config import DatabaseException, open_connection
from dotenv import load_dotenv
import os
import time

load_dotenv()


# Method that stores all answers of a user to the database
# Parameters: a list of tuples containing: a user id, the question number and the user's answer
# Returns: A confirmation message
def add_answers(answers, db, cursor, database):
    try:
        # The SQL statement for storing answers in the Answer table
        sql = "INSERT INTO " + database + ".Answer(userId, questionNumber, response) VALUES (%s, %s, %s)"

        cursor.executemany(sql, answers)
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()
        return "Success storing all Answers"

    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding answers.")


# Method that stores a new user to the database
# Parameters: a batch id
# Returns: a user id
def add_user(batch_id, db, cursor, database):
    try:
        cursor.execute("INSERT INTO " + database + ".Participant(batch) VALUES (%s)", (batch_id,))

        participant_id = cursor.lastrowid

        time.sleep(1)
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()
        return participant_id

    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding users.")


# Method that stores the value vector of a user to the database
# Parameters: a user id and a value vector
# Returns: A confirmation message
def add_value(user_id, values, db, cursor, database):
    try:
        # The SQL statement for storing a value in the Value table
        sql = "INSERT INTO " + database + ".Value (userId, stimulation, selfDirection, universalism" \
                                          ", benevolence, tradition, conformity, securityVal, powerVal, " \
                                          "achievement, hedonism)" \
                                          " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (user_id, values[0], values[1], values[2], values[3], values[4],
               values[5], values[6], values[7], values[8], values[9])
        cursor.execute(sql, val)

        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()

        return "Success storing value"

    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding values.")


# Method that stores the personality vector of a user to the database
# Parameters: a user id and a personality vector
# Returns: A confirmation message
def add_personality(user_id, personality, db, cursor, database):
    try:
        # The SQL statement for storing a personality in the Personality table
        sql = "INSERT INTO " + database + ".Personality (userId, openness, honesty, emotionality," \
                                          "extroversion, agreeableness, conscientiousness) " \
                                          "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (user_id, personality[0], personality[1], personality[2],
               personality[3], personality[4], personality[5])
        cursor.execute(sql, val)

        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()

        return "Success storing personality"

    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding personalities.")


# Returns user's value score and takes userId is input
def get_value(userId, db, cursor, database):
    try:
        sql = "SELECT stimulation, selfDirection, universalism, benevolence," \
              " tradition, conformity, securityVal, powerVal, achievement, hedonism " \
              "FROM " + database + ".Value AS v WHERE v.userId = %s"
        cursor.execute(sql, (userId,))

        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when trying to retrieve values.")


# Returns user's personality score and takes userId as input
def get_personality(userId, db, cursor, database):
    try:
        sql = "SELECT openness, honesty, emotionality," \
              "extroversion, agreeableness, conscientiousness " \
              "FROM " + database + ".Personality AS pe WHERE pe.userId = %s"
        cursor.execute(sql, (userId,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when trying to retrieve personality.")


# Method that stores a user and his matches on personality and value and a random other user
# Parameters: a user id , a value user id, a personality user id and a random user id
# Returns: A confirmation message
def add_matches(userId, val_user, pers_user, random_user, db, cursor, database):
    try:
        # The SQL statement for storing user id and matches in the Match table
        sql = "INSERT INTO " + database + ".Matches (userId, valueId, personalityId, randomId) " \
                                          "VALUES (%s, %s, %s, %s)"
        val = (userId, val_user, pers_user, random_user)
        cursor.execute(sql, val)

        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()

        return "Success storing personality"

    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding personalities.")


# Method that gets all the users of a certain batch and their values
# Parameters: batch number
# Returns: a list of tuples containing user and his values
def get_all_values(batch, db, cursor, database):
    try:
        sql = "SELECT userId, stimulation, selfDirection, universalism, benevolence," \
              " tradition, conformity, securityVal, powerVal, achievement, hedonism " \
              "FROM " + database + ".Value AS v , " + database + ".Participant AS p " \
                                                                 "WHERE v.ValueId = p.userId AND p.batch = %s"

        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving values.")


# Method that gets all the users of a certain batch and their personalities
# Parameters: batch number
# Returns: a list of tuples containing user and his personalities
def get_all_personalities(batch, db, cursor, database):
    try:
        sql = "SELECT userID, openness, honesty, emotionality," \
              "extroversion, agreeableness, conscientiousness " \
              "FROM " + database + ".personality AS pe , " \
              + database + ".participant AS pa " \
                           "WHERE pe.PersonalityId = pa.UserId AND pa.Batch = %s"

        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving personalities.")


# Method that gets all the users of a certain batch apart from the value user and personality user
# Parameters: batch number
# Returns: one random user id
def get_random_user(user1, user2, batch, db, cursor, database):
    try:
        sql = "SELECT userId FROM " + database + ".Participant AS p " \
                                                 "WHERE p.batch = %s AND NOT (p.UserID = %s or p.userId = %s)"

        cursor.execute(sql, (batch, user1, user2))
        result = cursor.fetchall()

        return result[randint(0, len(result))][0]
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving users.")
