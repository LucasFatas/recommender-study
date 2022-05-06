from backend.src.service import get_all_values, get_all_personalities, get_random_user


def match(userId, values, personality, batch, metric):
    batch_values = get_all_values(batch)
    val_user = closest_user(values, batch_values, metric)

    batch_personality = get_all_personalities(batch)
    pers_user = closest_user(personality, batch_personality, metric)

    random_user = get_random_user(val_user,pers_user,batch)
    add_maches(userId, val_user, pers_user, random_user)
    return



def calculate_distance(answer, batch_answer, metric):
    sum = 0
    for x in len(answer):
        sum = sum + pow(abs(answer[x] - batch_answer[x+1]),metric)
    result = pow(sum, 1/metric)
    return

def closest_user(answer, batch_answer,metric):
    closest = -1
    closest_distance = -1
    for x in batch_answer:
        distance = calculate_distance(answer, x, metric)
        if (distance < closest_distance):
            closest_distance = distance
            closest = x[0]
    return closest