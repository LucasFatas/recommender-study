import numpy as np


# Calculates value scores of a user given the answers to the quiz.
# Parameters: answers related to value theory.
# Returns an array of floats representing the personality scores.
def val_calc(val_answers):
    grand_mean = np.mean(val_answers)

    # List with the 10 value fields.
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
    ])

    norm = values - grand_mean
    return norm.round(2).tolist()


# Calculates the reverse of the HEXACO score, in order to compute the scores of the questionnaire
def reverse(score):
    return 6 - score


# Calculates HEXACO personality scores of a user given the answers to the quiz.
# Parameters: answers related to personality.
# Returns an array of floats representing the personality scores.
def pers_calc(pers_answers):

    # List with the 6 personality fields. Comment on top of each entry is coding key for personality calculation.
    # R after a number corresponds to the reverse of that score. Explained in the corresponding method.
    personalities = np.array([
        # Honesty-Humility - 6, 30R, 54, 12R, 36, 60R, 18, 42R, 24R, 48R
        np.mean([pers_answers[5], reverse(pers_answers[29]), pers_answers[53], reverse(pers_answers[11]),
                 pers_answers[35], reverse(pers_answers[59]), pers_answers[17], reverse(pers_answers[41]),
                 reverse(pers_answers[23]), reverse(pers_answers[47])]),

        # Emotionality - 5, 29, 53R, 11, 35R, 17, 41R, 23, 47, 59R
        np.mean([pers_answers[4], pers_answers[28], reverse(pers_answers[52]), pers_answers[10],
                 reverse(pers_answers[34]), pers_answers[16], reverse(pers_answers[40]),
                 pers_answers[22], pers_answers[46], reverse(pers_answers[58])]),

        # Extraversion - 4, 28R, 52R, 10R, 34, 58, 16, 40, 22, 46R
        np.mean([pers_answers[3], reverse(pers_answers[27]), reverse(pers_answers[51]), reverse(pers_answers[9]),
                 pers_answers[33], pers_answers[57], pers_answers[15], pers_answers[39],
                 pers_answers[21], reverse(pers_answers[45])]),

        # Agreeableness - 3, 27, 9R, 33, 51, 15R, 39, 57R, 21R, 45
        np.mean([pers_answers[2], pers_answers[26], reverse(pers_answers[8]), pers_answers[32],
                 pers_answers[50], reverse(pers_answers[14]), pers_answers[38], reverse(pers_answers[56]),
                 reverse(pers_answers[20]), pers_answers[44]]),

        # Conscientiousness - 2, 26R, 8, 32R, 14R, 38, 50, 20R, 44R, 56R
        np.mean([pers_answers[1], reverse(pers_answers[25]), pers_answers[7], reverse(pers_answers[31]),
                 reverse(pers_answers[13]), pers_answers[37], pers_answers[49], reverse(pers_answers[19]),
                 reverse(pers_answers[43]), reverse(pers_answers[55])]),

        # Openness to Experience - 1R, 25, 7, 31R, 13, 37, 49R, 19R, 43, 55R
        np.mean([reverse(pers_answers[0]), pers_answers[24], pers_answers[6], reverse(pers_answers[30]),
                 pers_answers[12], pers_answers[36], reverse(pers_answers[48]), reverse(pers_answers[18]),
                 pers_answers[42], reverse(pers_answers[54])]),

    ]).round(2).tolist()

    return personalities


# Connecting method, called from QuestionnaireController.py. Includes both previous methods.
# Parameters: answers related to value theory, answers related to personality.
# Returns a tuple consisting of calculated value and personality scores, in that order.
def calculations(val_answers, pers_answers):
    return val_calc(val_answers), pers_calc(pers_answers)
