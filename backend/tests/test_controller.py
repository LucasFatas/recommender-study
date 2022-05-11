import json
from src.main import app


def test_connection():
    response = app.test_client().get('/')
    assert "Connection is working" == response.json['response']


def test_save_answers():
    data = {
        "user": "1",
        "value_answers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "personality_answers": [5, 6]
    }

    response = app.test_client().post('/saveAnswer', json=data)

    assert {"personalities": 0, "values": 0} == response.json
