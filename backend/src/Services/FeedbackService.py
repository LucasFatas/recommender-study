import mysql.connector
from src.Services.database_config import DatabaseException, open_connection
from dotenv import load_dotenv
import os

load_dotenv()


def add_feedback_questions(userId, matchedUserId, answers, db, cursor, database):
    try:
        sql = "INSERT INTO " + database + ".QuestionFeedback(userId, matchedUserId, questionNumber, answer) " \
              "VALUES(%s, %s, %s, %s);"

        params = []
        for i, answer in enumerate(answers):
            params.append((userId, matchedUserId, i + 1, answer))

        cursor.executemany(sql, params)
        if not os.getenv('IS_TESTING'):
            db.commit()

        return "Success storing feedback questions."
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error while adding question feedback in database")


def add_open_feedback(userId, matchedUserId, feedback):
    db, cursor, database = open_connection()

    try:
        sql = "INSERT INTO " + database + ".OpenFeedback(userId, matchedUserId, feedback) VALUES(%s, %s, %s)"
        answer = (userId, matchedUserId, feedback)

        cursor.execute(sql, answer)
        if not os.getenv('IS_TESTING'):
            db.commit()

        return "Success storing open feedback."
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error while adding open feedback in database")
