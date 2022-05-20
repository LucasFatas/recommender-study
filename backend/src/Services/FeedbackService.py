import mysql.connector
from src.Services.database_config import DatabaseException, open_connection


def add_open_feedback(userId, matchedUserId, feedback):
    db, cursor, database = open_connection()

    try:
        sql = "Insert into " + database + ".openfeedback(UserId, MatchedUserId, Feedback) VALUES(%s, %s, %s)"
        answer = (userId, matchedUserId, feedback)

        cursor.execute(sql, answer)
        db.commit()

        return "Success storing answers"
    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error while adding open feedback in database")


