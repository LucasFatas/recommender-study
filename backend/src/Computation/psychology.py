import numpy as np


def val_calc(val_answers):
    """
    Calculates the scores of a user based on his answers to the PVQ questionnaire.
    Scoring key is commented over each array entry
    :param val_answers: Answers of the user, an array of size 40
    :return: an array of 10 scores representing the rating for each of the 10 values for the user
    """
    # We have to subtract the total mean of the values to each score.
    grand_mean = np.mean(val_answers)

    # List with the 10 value fields.
    values = np.array([
        # Stimulation - 6,15,30
        np.mean([val_answers[5], val_answers[14], val_answers[29]]),

        # Self-Direction - 1,11,22,34
        np.mean([val_answers[0], val_answers[10], val_answers[21], val_answers[33]]),

        # Universalism - 3,8,19,23,29,40
        np.mean([val_answers[2], val_answers[7], val_answers[18],
                 val_answers[22], val_answers[28], val_answers[39]]),

        # Benevolence - 12,18,27,33
        np.mean([val_answers[11], val_answers[17], val_answers[26], val_answers[32]]),

        # Tradition - 9,20,25,38
        np.mean([val_answers[8], val_answers[19], val_answers[24], val_answers[37]]),

        # Conformity - 7,16,28,36
        np.mean([val_answers[6], val_answers[15], val_answers[27], val_answers[35]]),

        # Security - 5,14,21,31,35
        np.mean([val_answers[4], val_answers[13], val_answers[20], val_answers[30], val_answers[34]]),

        # Power - 2,17,39
        np.mean([val_answers[1], val_answers[16], val_answers[38]]),

        # Achievement - 4,13,24,32
        np.mean([val_answers[3], val_answers[12], val_answers[23], val_answers[31]]),

        # Hedonism - 10,26,37
        np.mean([val_answers[9], val_answers[25], val_answers[36]])
    ])

    norm = values - grand_mean
    return norm.round(2).tolist()


def reverse(score):
    """
    Calculates the reverse of a 1-5 score, in order to compute the scores of the HEXACO questionnaire
    Thus, 1 becomes 5, 2 becomes 4, 3 stays as 3, 4 becomes 2 and 5 becomes 1.
    :param score: the number to reverse
    :return: the reversed score.
    """
    return 6 - score


def pers_calc(pers_answers):
    """
    Calculates the scores of a user based on his answers to the HEXACO questionnaire.
    Scoring key is commented over each array entry. The letter R after a number symbolizes the reverse of the score.
    :param pers_answers: Answers of the user, an array of size 60
    :return: an array of 6 scores representing the rating for each of the 6 personality traits for the user.
    """
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


def calculations(val_answers, pers_answers):
    """
    Divides the calculations so that there is only one method called from the controllers and services
    :param val_answers: answers of the user for the PVQ questionnaire
    :param pers_answers: answers of the user for the HEXACO questionnaire
    :return: a tuple with the scores calculated based on the answers. Two arrays of size 10 and 6
    """
    return val_calc(val_answers), pers_calc(pers_answers)
