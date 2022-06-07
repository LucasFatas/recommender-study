import mysql.connector
from src.Services.database_config import DatabaseException
from dotenv import load_dotenv
import os

load_dotenv()


def add_feedback_questions(userId, matchedUserId, answers, db, cursor, database):
    """
    Stores all the questions provided by the participant about the recommended playlists
    :param userId: id of the participant
    :param matchedUserId: id of the participant he has been matched with
    :param answers: answers to the feedback questions provided
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling
    :return: success message
    """
    try:
        sql = """
            INSERT INTO """ + database + """.QuestionFeedback(userId, matchedUserId, questionNumber, answer)
            VALUES(%s, %s, %s, %s);
        """

        params = []
        # Create tuple with the proper values to store in database.
        for i, answer in enumerate(answers):
            params.append((userId, matchedUserId, i + 1, answer))

        # Execute the query at the same time for all the values
        cursor.executemany(sql, params)
        # Commit only if we are not testing the application
        if not os.getenv('IS_TESTING'):
            db.commit()

        return "Success storing feedback questions."
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error while adding question feedback in database")


def add_open_feedback(userId, matchedUserId, feedback, db, cursor, database):
    """
    Stores open feedback provided by the participant about the recommended playlists
    :param userId: id of the participant
    :param matchedUserId: id of the participant he has been matched with
    :param feedback: feedback provided by the user in the form of text.
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling
    :return: success message.
    """
    try:
        sql = """
            INSERT INTO """ + database + """.OpenFeedback(userId, matchedUserId, feedback) VALUES(%s, %s, %s)
        """
        answer = (userId, matchedUserId, feedback)

        cursor.execute(sql, answer)

        # Commit only if we are not testing the application
        if not os.getenv('IS_TESTING'):
            db.commit()

        return "Success storing open feedback."
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error while adding open feedback in database")
