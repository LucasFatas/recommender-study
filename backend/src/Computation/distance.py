import numpy as np


def manhattan_distance(arg1, arg2):
    point1 = np.array(arg1)
    point2 = np.array(arg2)

    #calculate manhattan distance
    distance = np.sum(np.abs(point1 - point2))

    return distance


def euclidean_distance(arg1, arg2):

    point1 = np.array(arg1)
    point2 = np.array(arg2)

    # calculate Euclidean distance
    distance = np.linalg.norm(point1 - point2)

    return distance

def camberan_distance(arg1, arg2):
    #TODO Add the last distance
    return 1
