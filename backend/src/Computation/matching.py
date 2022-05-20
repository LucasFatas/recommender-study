from src.Services.QuestionnaireService import get_all_values, get_all_personalities, get_random_user, add_matches
from src.Computation.distance import manhattan_distance, euclidean_distance, camberan_distance


def match(userId, values, personality, batch, metric):
    """
    Real code when values is implemented
    #batch_values = get_all_values(batch)
    #val_user = closest_user(values, batch_values, metric)

    pers_user = userId
    # batch_personality = get_all_personalities(batch)
    # pers_user = closest_user(personality, batch_personality, metric)

    #random_user = get_random_user(val_user, pers_user, batch)
    # add_matches(userId, val_user, pers_user, random_user)
    return val_user, pers_user, random_user
    """
    batch_personality = get_all_personalities(batch,userId)
    pers_user = closest_user(personality, batch_personality, metric)

    random_user = get_random_user(userId, pers_user, batch)
    return userId, pers_user, random_user


# Calculates Distance of two vectors based on a defined metric
def calculate_distance(answer, batch_answer, metric):
    if metric.casefold() == "manhattan".casefold():
        return manhattan_distance(answer, batch_answer)
    elif metric.casefold() == "euclidean".casefold():
        return euclidean_distance(answer, batch_answer)
    else:
        return camberan_distance(answer, batch_answer)


def closest_user(answer, batch_answer, metric):
    print(answer)
    closest = -1
    closest_distance = float("inf")
    for x in batch_answer:
        distance = calculate_distance(answer, x[-(len(x) - 1):], metric)
        if distance < closest_distance:
            closest_distance = distance
            closest = x[0]
    return closest