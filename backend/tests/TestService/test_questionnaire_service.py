from src.Services.QuestionnaireService import add_value, add_answers, add_user, add_personality


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


def test_add_answers():
    tup = [(1, 1, 1), (1, 2, 3)]
    assert "Success storing all Answers" == add_answers(tup)

