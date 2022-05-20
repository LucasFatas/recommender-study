import mysql.connector
from src.Services.database_config import DatabaseException, open_connection


def add_feedback_questions(userId, matchedUserId, answers):
    db, cursor, database = open_connection()

    try:
        sql = "Insert into " + database + ".questionfeedback(UserId, MatchedUserId, QuestionOne, QuestionTwo, " \
                                          "QuestionThree, QuestionFour, QuestionFive, QuestionSix ) " \
                                          "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        answer = (userId, matchedUserId,
                  answers[0], answers[1], answers[2], answers[3], answers[4], answers[5])

        cursor.execute(sql, answer)
        db.commit()

        return "Success storing answers"
    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error while adding open feedback in database")
