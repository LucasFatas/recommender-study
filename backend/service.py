import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="Recommender"
)

my_cursor = db.cursor()

def store_answers(user_id, answers):
    for i in range(len(answers)):
        store_answer(user_id, i + 1, answers[i])
    return "Success storing all Answers"


def store_user(user_id, values, personalities, batch):
    my_cursor.execute("Insert Into Recommender.Participant(ParticapantId, PersonalityVectorId, ValueVectorId, BatchId) "
                      "Values(" + str(user_id) + "," + str(user_id) + "," + str(user_id) + "," + str(batch) + ")")

    # TODO: store personality and value vectors of the user
    db.commit()
    return "Success storing user"


def store_answer(user_id, question_number, answer):
    my_cursor.execute("Insert Into Recommender.Answer(ParticipantId, QuestionNumber, Response) Values(" + str(user_id) + "," + str(question_number) + "," + str(answer) + ")")
    db.commit()

    return "Success storing answer"

if __name__ == '__main__':
    store_answer(1, 1, 4)