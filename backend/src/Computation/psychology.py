
# Calculates value scores of a user given the answers to the quiz.
# Parameters: answers related to value theory.
# Returns an array of floats representing the personality scores.
def val_calc(val_answers):
    # TODO: Implement logic with PVQ questions
    return 0


# Calculates personality scores of a user given the answers to the quiz.
# Parameters: answers related to personality.
# Returns an array of floats representing the personality scores.
def pers_calc(val_answers):
    # TODO: Implement logic with HEXACO questions
    return 0


# Connecting method, called from QuestionnaireController.py. Includes both previous methods.
# Parameters: answers related to value theory, answers related to personality.
# Returns a tuple consisting of calculated value and personality scores, in that order.
def calculations(val_answers, pers_answers):
    return val_calc(val_answers), pers_calc(pers_answers)


# TODO: maybe delete this method because not needed anymore
def split_data(answers):
    # TODO: split received answers from frontend
    return 0, 0
