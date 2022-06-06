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
    response = app.test_client().get("/dashboard/answers?batchId=1")

    expected = "UserId,QuestionNumber,Answer\r\n3,0,4\r\n3,1,1\r\n3,2,5\r\n3,3,4\r\n3,4,5\r\n3,5,5\r\n3,6,4\r\n3,7,3\r\n" \
               "3,8,2\r\n3,9,1\r\n3,10,4\r\n3,11,1\r\n3,12,3\r\n3,13,1\r\n3,14,5\r\n3,15,2\r\n3,16,2\r\n3,17,2\r\n3,18,2" \
               "\r\n3,19,2\r\n3,20,3\r\n3,21,3\r\n3,22,3\r\n3,23,3\r\n3,24,3\r\n3,25,1\r\n3,26,5\r\n3,27,1\r\n3,28,1\r\n3,29,4" \
               "\r\n3,30,2\r\n3,31,5\r\n3,32,5\r\n3,33,2\r\n3,34,5\r\n3,35,2\r\n3,36,4\r\n3,37,3\r\n3,38,4\r\n3,39," \
               "4\r\n3,40,3\r\n3,41,3\r\n3,42,3\r\n3,43,3\r\n3,44,3\r\n3,45,2\r\n3,46,2\r\n3,47,4\r\n3,48,2\r\n3,49,2" \
               "\r\n3,50,5\r\n3,51,1\r\n3,52,2\r\n3,53,1\r\n3,54,4\r\n3,55,5\r\n3,56,2\r\n3,57,3\r\n3,58,4\r\n3,59,1\r\n" \
               "3,60,1\r\n3,61,2\r\n3,62,1\r\n3,63,4\r\n3,64,1\r\n3,65,1\r\n3,66,1\r\n3,67,2\r\n3,68,4\r\n3,69,3\r\n3,70,2" \
               "\r\n3,71,1\r\n3,72,1\r\n3,73,5\r\n3,74,1\r\n3,75,1\r\n3,76,1\r\n3,77,6\r\n3,78,5\r\n3,79,5\r\n3,80,1" \
               "\r\n3,81,6\r\n3,82,6\r\n3,83,1\r\n3,84,2\r\n3,85,5\r\n3,86,1\r\n3,87,6\r\n3,88,5\r\n3,89,2\r\n3,90,3" \
               "\r\n3,91,4\r\n3,92,3\r\n3,93,1\r\n3,94,2\r\n3,95,4\r\n3,96,3\r\n3,97,1\r\n3,98,5\r\n3,99,1\r\n"

    assert response.text == expected


def test_retrieve_songs(set_up):
    response = app.test_client().get("/dashboard/songs?batchId=1")

    expected = "UserId,SpotifyUrl\r\n3,https://open.spotify.com/track/1emB9tyqtTOH4xLVhZsbZZ\r\n" \
               "3,https://open.spotify.com/track/2GiZ3sC2p1Cc2t2gbdMKsN\r\n" \
               "3,https://open.spotify.com/track/3nAq2hCr1oWsIU54tS98pL\r\n" \
               "3,https://open.spotify.com/track/4XJJCXGv7VDdmsHGwq6LCM\r\n" \
               "3,https://open.spotify.com/track/4zFM2jL5OmDZAoIr3vwcZh\r\n"

    assert response.text == expected
