from src.Services.QuestionnaireService import get_all_values, get_all_personalities, get_random_user, add_matches
from src.Computation.distance import manhattan_distance, euclidean_distance
from src.Services.database_config import open_connection

db, cursor, database = open_connection()


def match(userId, values, personality, batch, metric):
    """
    Real code when values are implemented
    #batch_values = get_all_values(batch)
    #val_user = closest_user(values, batch_values, metric)

    pers_user = userId
    # batch_personality = get_all_personalities(batch)
    # pers_user = closest_user(personality, batch_personality, metric)

    #random_user = get_random_user(val_user, pers_user, batch)
    return val_user, pers_user, random_user
    """
    batch_personality = get_all_personalities(batch, db, cursor, database)
    pers_user = closest_user(personality, batch_personality, metric)

    batch_values = get_all_values(batch, db, cursor, database, pers_user)
    val_user = closest_user(values, batch_values, metric)

    random_user = get_random_user(pers_user, val_user, batch, db, cursor, database)
    add_matches(userId, val_user, pers_user, random_user, db, cursor, database)
    return val_user, pers_user, random_user


def calculate_distance(answer, batch_answer, metric):
    """
    Method that calculates which distance metric we are going to use to match users
    :param answer: score of the user that we are matching against
    :param batch_answer: one of the scores for the users that are in the batch that is going to be matched
    against this user
    :param metric: The specific metric that will be used for this matching process
    :return: distance computation of the user and the specific user
    """
    if metric.casefold() == "Manhattan".casefold():
        return manhattan_distance(answer, batch_answer)
    elif metric.casefold() == "Euclidean".casefold() or metric.casefold() == "Euclidian".casefold():
        return euclidean_distance(answer, batch_answer)


def closest_user(answer, batch_answer, metric):
    """
    Calculates the closest user to the given participant through the use of the distance calculation method
    :param answer: answer of the user to be matched
    :param batch_answer: list of answers and userIds of the participants in the specific batch
    :param metric: the metric that will be used to calculate the distances
    :return: closest id of all the users in the batch_answer set
    """
    closest = -1
    closest_distance = float("inf")
    for x in batch_answer:
        distance = calculate_distance(answer, x[-(len(x) - 1):], metric)
        if distance < closest_distance:
            closest_distance = distance
            closest = x[0]
    return closest
