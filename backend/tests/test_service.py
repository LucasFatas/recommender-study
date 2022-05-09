from backend.src.service import change_database_for_testing, add_answers, add_user, add_value, add_personality
import json


def test_add_answers():
    tup = [(1, 1, 1), (1, 2, 3)]
    assert "Success storing all Answers" == add_answers(tup)


def test_add_user():
    actual = add_user(1)
    assert type(actual) == int


def test_add_value():
    user_id = add_user(1)
    tup = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    assert "Success storing value" == add_value(user_id, tup)


def test_add_personality():
    user_id = add_user(1)
    tup = (1, 1, 1, 1, 1, 1)
    assert "Success storing personality" == add_personality(user_id, tup)


def test_change_database_for_testing():
    value = 0
    change_database_for_testing(False)
    with open('../config.json', 'r+') as f:
        data = json.load(f)
        value = data['is_testing']

    assert not json.loads(value)

    change_database_for_testing(True)
    with open('../config.json', 'r+') as f:
        data = json.load(f)
        value = data['is_testing']

    assert json.loads(value)



if __name__ == '__main__':
    test_change_database_for_testing()
    change_database_for_testing(True)
    test_add_answers()
    test_add_user()
    test_add_value()
    test_add_personality()

