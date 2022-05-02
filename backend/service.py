def store_answers(user_id, answers):
    for i in range(len(answers)):
        store_answer(user_id, answers[i], i + 1)
    return "Success storing all Answers"


def store_user(user_id, values, personalities, batch):
    # TODO: store all data in our database
    return "Success storing user"


def store_answer(user_id, answer, question_number):
    # TODO: store one answer
    return "Success storing answer"
