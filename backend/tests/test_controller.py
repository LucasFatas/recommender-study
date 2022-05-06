import json
from src.controller import app


def test_save_answers():
    data = {
        "user": "1",
        "value_answers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "personality_answers": [5, 6]
    }

    response = app.test_client().post('/saveAnswer', json=data)

    assert json.dumps({'values': 0, 'personalities': 0}) == response.text
