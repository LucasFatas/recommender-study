import sys

from src.Services.QuestionnaireService import get_all_values, get_all_personalities, get_random_user, add_matches
from src.Computation.distance import manhattan_distance, euclidean_distance, camberan_distance
from src.Services.database_config import open_connection


def match(userId, values, personality, batch, metric):
    """
    Real code when values is implemented
    #batch_values = get_all_values(batch)
    #val_user = closest_user(values, batch_values, metric)

    pers_user = userId
    # batch_personality = get_all_personalities(batch)
    # pers_user = closest_user(personality, batch_personality, metric)

    #random_user = get_random_user(val_user, pers_user, batch)
    return val_user, pers_user, random_user
    """
    db, cursor, database = open_connection()
    batch_personality = get_all_personalities(batch, db, cursor, database)
    batch_values = get_all_values(batch, db, cursor, database)

    pers_user = closest_user(personality, batch_personality, metric, 0)
    val_user = closest_user(values, batch_values, metric, pers_user)

    random_user = get_random_user(userId, pers_user, val_user, batch, db, cursor, database)
    add_matches(userId, val_user, pers_user, random_user, db, cursor, database)
    return val_user, pers_user, random_user


# Calculates Distance of two vectors based on a defined metric
def calculate_distance(answer, batch_answer, metric):
    if metric.casefold() == "manhattan".casefold():
        return manhattan_distance(answer, batch_answer)
    elif metric.casefold() == "euclidean".casefold():
        return euclidean_distance(answer, batch_answer)
    else:
        return camberan_distance(answer, batch_answer)


def closest_user(answer, batch_answer, metric, id):
    closest = -1
    closest_distance = sys.maxsize
    count = 0
    for x in batch_answer:
        count += 1
        distance = calculate_distance(answer, x[1:], metric)
        print(distance, answer, x[1:], metric)
        if distance < closest_distance and count != id:
            closest_distance = distance
            closest = x[0]
    return closest


a = closest_user([0, 0], [[1, 0, 2], [2, 2, 1], [3, 1, 1]], "euclidian", -1)
