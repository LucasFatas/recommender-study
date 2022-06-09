from src.Services.QuestionnaireService import add_value, add_answers, add_user, add_personality
from tests.fixtures import set_up


def test_add_user(set_up):
    db, cursor, database = set_up
    actual = add_user(1, db, cursor, database)
    assert type(actual) == int


def test_add_value(set_up):
    db, cursor, database = set_up
    user_id = add_user(1, db, cursor, database)
    tup = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    assert "Success storing value" == add_value(user_id, tup, db, cursor, database)


def test_add_personality(set_up):
    db, cursor, database = set_up
    user_id = add_user(1, db, cursor, database)
    tup = (1, 1, 1, 1, 1, 1)
    assert "Success storing personality" == add_personality(user_id, tup, db, cursor, database)


def test_add_answers(set_up):
    db, cursor, database = set_up
    tup = [(10, 1, 1), (10, 2, 3)]
    assert "Success storing all Answers" == add_answers(tup, db, cursor, database)

