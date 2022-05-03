import mysql.connector
import json


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


def add_answers(answers):
    db, cursor = open_connection()
    sql = """INSERT INTO Recommender.Answer(ParticipantId, QuestionNumber, Response) VALUES (%s, %s, %s)"""
    cursor.executemany(sql, answers)
    db.commit()
    return "Success storing all Answers"


def add_user(batch_id):
    db, cursor = open_connection()
    cursor.execute("Insert Into Recommender.Participant(Batch) "
                      "Values(2)")

    participant_id = cursor.lastrowid

    db.commit()
    return participant_id


def store_answer(user_id, question_number, answer):
    db, cursor = open_connection()
    cursor.execute("Insert Into Recommender.Answer(UserId, QuestionNumber, Response) Values(" + str(user_id) + "," + str(question_number) + "," + str(answer) + ")")
    db.commit()

    return "Success storing answer"


def add_value(user_id, values):
    db, cursor = open_connection()
    sql = "INSERT INTO Recommender.Value (ValueId, Stimulation, SelfDirection, Universalism" \
          ",Benevolence,Tradition, Conformity, SecurityVal, PowerVal, Achievement,Hedonism)" \
          " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (user_id, values[0], values[1], values[2], values[3], values[4],
           values[5], values[6], values[7], values[8], values[9])
    cursor.execute(sql, val)
    db.commit()

    return "Success storing value"


def add_personality(user_id, personality):
    db, cursor = open_connection()
    sql = "INSERT INTO Recommender.Personality (PersonalityId, Openness, Honesty, Emotionality" \
          ", Extroversion, Agreeableness, Conscientiousness VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (user_id, personality[0], personality[1], personality[2],
           personality[3], personality[4], personality[5], personality[6])
    cursor.execute(sql, val)
    db.commit()

    return "Success storing personality"

if __name__ == '__main__':
    add_value(2,(1,2,3,4,5,6,7,8,9,10))