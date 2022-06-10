import numpy as np


def manhattan_distance(arg1, arg2):
    """
    This method calculates the manhattan distance between two personality/value vectors
    :param arg1: first vector representing the personality/value scores of a user
    :param arg2: second vector representing the personality/value scores of a user
    :return: manhattan distance between the two points
    """
    point1 = np.array(arg1)
    point2 = np.array(arg2)

    # Calculate manhattan distance.
    distance = np.sum(np.abs(point1 - point2))

    return distance


def euclidean_distance(arg1, arg2):
    """
    This method calculates the euclidean distance between two personality/value vectors.
    :param arg1: first vector representing the personality/value scores of a user.
    :param arg2: second vector representing the personality/value scores of a user.
    :return: euclidean distance between the two points.
    """
    point1 = np.array(arg1)
    point2 = np.array(arg2)

    # Calculate Euclidean distance
    distance = np.linalg.norm(point1 - point2)

    return distance

