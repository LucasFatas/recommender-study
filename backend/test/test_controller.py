import jsonify


def test_save_answer(client):
    data = {
        "user": 1,
        "value_answers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "personality_answers": [5, 6]
    }
    response = client.post("/saveAnswer", data)
    assert jsonify(values=0, personalities=0) == response.json()
