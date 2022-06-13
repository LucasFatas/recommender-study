from src.main import app
from tests.fixtures import set_up


# Tests for QuestionnaireController.
def test_save_answers(set_up):
    data = {
        "user": 5,
        "value_answers": [1, 2, 1, 4, 1, 1,
                          1, 2, 4, 3, 2, 1,
                          1, 5, 1, 1, 1, 6,
                          5, 5, 1, 6, 6, 1,
                          2, 5, 1, 6, 5, 2,
                          3, 4, 3, 1, 2, 4,
                          3, 1, 5, 1],
        "personality_answers": [2, 1, 5, 4, 5, 5, 4, 3, 2, 1,
                                4, 1, 3, 1, 5, 2, 2, 5, 2, 2,
                                3, 3, 3, 3, 3, 1, 5, 1, 1, 4,
                                2, 5, 5, 2, 5, 2, 4, 3, 4, 4,
                                3, 5, 1, 3, 3, 2, 2, 4, 2, 2,
                                5, 1, 2, 1, 4, 5, 2, 3, 4, 1]
    }

    response = app.test_client().post('/questionnaire/answer/add', json=data)
    expected = {
        "personalities": [
            3.1,
            2.7,
            3.7,
            3.9,
            2.8,
            3.3
        ],
        "values": [
            3.0,
            3.0,
            2.75,
            3.33,
            2.5,
            1.33,
            3.67,
            2.5,
            2.67,
            2.4
        ]
    }
    assert response.json == expected
