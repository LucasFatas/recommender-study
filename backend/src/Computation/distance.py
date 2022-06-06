import numpy as np


def manhattan_distance(arg1, arg2):
    point1 = np.array(arg1)
    point2 = np.array(arg2)

    # Calculate manhattan distance.
    distance = np.sum(np.abs(point1 - point2))

    print(distance)
    return distance


def euclidean_distance(arg1, arg2):

    point1 = np.array(arg1)
    point2 = np.array(arg2)

    # Calculate Euclidean distance
    distance = np.linalg.norm(point1 - point2)

    return distance

