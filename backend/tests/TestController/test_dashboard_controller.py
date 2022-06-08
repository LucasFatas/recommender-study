from src.main import app
from tests.fixtures import set_up


def test_retrieve_scores(set_up):
    response = app.test_client().get("/dashboard/scores?batchId=1")

    expected = "UserID,Openness,Honesty,Emotionality,Extroversion,Agreeableness,Conscientiousness,Stimulation," \
               "SelfDirection,Universalism,Benevolence,Tradition,Conformity,SecurityVal,PowerVal,Achievement," \
               "Hedonism\r\n" \
               "1,2.6,3.0,3.7,3.5,3.3,2.9,3.0,2.0,2.75,3.83,2.5,1.33,2.33,2.5,2.67,2.6\r\n" \
               "2,3.0,2.7,3.7,3.9,2.8,3.3,3.0,2.0,2.75,3.83,2.5,1.33,2.33,2.5,2.67,2.6\r\n" \
               "3,3.0,2.7,3.7,3.9,2.8,3.3,3.0,3.0,2.75,3.33,2.5,1.33,3.67,2.5,2.67,2.4\r\n"

    assert response.text == expected


def test_retrieve_answers(set_up):
    response = app.test_client().get("/dashboard/answers?batchId=2")

    expected = "UserId,QuestionNumber,Answer\r\n4,0,2\r\n4,1,4\r\n4,2,3\r\n"

    assert response.text == expected


def test_retrieve_songs(set_up):
    response = app.test_client().get("/dashboard/songs?batchId=1")

    expected = "UserId,SpotifyUrl\r\n1,https://open.spotify.com/track/03J7yqJA8a4eSjnFUSfCbp\r\n" \
               "1,https://open.spotify.com/track/0LUwBqSMzszqZA7td5TjpK\r\n" \
               "1,https://open.spotify.com/track/2hSBhzE4hbWRWl4PLMiJsu\r\n" \
               "1,https://open.spotify.com/track/5JnASEjM04jp20CjK6PqfI\r\n" \
               "1,https://open.spotify.com/track/6COq76th7tzFFi2wlcD6xj\r\n" \
               "2,https://open.spotify.com/track/08o9yCplgxLM11ymhvkbl8\r\n" \
               "2,https://open.spotify.com/track/3lrNU0pvwTaXsgDqa55A8j\r\n" \
               "2,https://open.spotify.com/track/3NqwLwpzbpyvXB2wJE0Oe6\r\n" \
               "2,https://open.spotify.com/track/4mK6NMhrACj0W3dWPiQ72G\r\n" \
               "2,https://open.spotify.com/track/6X6BRvpa5Z9wW0SuxxlhmI\r\n" \
               "3,https://open.spotify.com/track/1emB9tyqtTOH4xLVhZsbZZ\r\n" \
               "3,https://open.spotify.com/track/2GiZ3sC2p1Cc2t2gbdMKsN\r\n" \
               "3,https://open.spotify.com/track/3nAq2hCr1oWsIU54tS98pL\r\n" \
               "3,https://open.spotify.com/track/4XJJCXGv7VDdmsHGwq6LCM\r\n" \
               "3,https://open.spotify.com/track/4zFM2jL5OmDZAoIr3vwcZh\r\n" \

    assert response.text == expected
