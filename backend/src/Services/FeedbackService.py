import mysql.connector
from src.Services.database_config import DatabaseException, open_connection


def add_feedback_questions(userId, matchedUserId, answers):
    db, cursor, database = open_connection()

    try:
        sql = "Insert into " + database + ".questionfeedback(UserId, MatchedUserId, QuestionNumber, Answer) " \
              "Values(%s, %s, %s, %s);"

        params = []
        for i, answer in enumerate(answers):
            params.append((userId, matchedUserId, i + 1, answer))

        cursor.executemany(sql, params)
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error while adding question feedback in database")


def add_open_feedback(userId, matchedUserId, feedback):
    db, cursor, database = open_connection()

    try:
        sql = "Insert into " + database + ".openfeedback(UserId, MatchedUserId, Feedback) VALUES(%s, %s, %s)"
        answer = (userId, matchedUserId, feedback)

        cursor.execute(sql, answer)
        db.commit()

        return "Success storing answers"
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error while adding open feedback in database")


>>>>>>> backend/src/Services/FeedbackService.py
