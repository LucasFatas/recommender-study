import numpy as np


# Calculates value scores of a user given the answers to the quiz.
# Parameters: answers related to value theory.
# Returns an array of floats representing the personality scores.
def val_calc(val_answers):
    mrat = np.mean(val_answers)

    # Tuple with the 10 value fields.
    values = np.array([
        # Conformity - 7,16,28,36
        np.mean([val_answers[6], val_answers[15], val_answers[27], val_answers[35]]),

        # Tradition - 9,20,25,38
        np.mean([val_answers[8], val_answers[19], val_answers[24], val_answers[37]]),

        # Benevolence - 12,18,27,33
        np.mean([val_answers[11], val_answers[17], val_answers[26], val_answers[32]]),

        # Universalism - 3,8,19,23,29,40
        np.mean([val_answers[2], val_answers[7], val_answers[18],
                 val_answers[22], val_answers[28], val_answers[39]]),

        # Self-Direction - 1,11,22,34
        np.mean([val_answers[0], val_answers[10], val_answers[21], val_answers[33]]),

        # Stimulation - 6,15,30
        np.mean([val_answers[5], val_answers[14], val_answers[29]]),

        # Hedonism - 10,26,37
        np.mean([val_answers[9], val_answers[25], val_answers[36]]),

        # Achievement - 4,13,24,32
        np.mean([val_answers[3], val_answers[12], val_answers[23], val_answers[31]]),

        # Power - 2,17,39
        np.mean([val_answers[1], val_answers[16], val_answers[38]]),

        # Security - 5,14,21,31,35
        np.mean([val_answers[4], val_answers[13], val_answers[20], val_answers[30], val_answers[34]])
    ]).round(2).tolist()

    meaned_values = values - mrat
    return values


# Calculates personality scores of a user given the answers to the quiz.
# Parameters: answers related to personality.
# Returns an array of floats representing the personality scores.
def pers_calc(val_answers):
    # TODO: Implement logic with HEXACO questions
    return [1, 2, 3, 3, 4, 5, 6]


# Connecting method, called from QuestionnaireController.py. Includes both previous methods.
# Parameters: answers related to value theory, answers related to personality.
# Returns a tuple consisting of calculated value and personality scores, in that order.
def calculations(val_answers, pers_answers):
    return val_calc(val_answers), pers_calc(pers_answers)
