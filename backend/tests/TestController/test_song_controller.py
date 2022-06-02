import numpy as np
from tests.fixtures import set_up
from src.Services.QuestionnaireService import add_user, add_value, add_personality
from src.Services.SongService import add_top_songs
from src.main import app
from src.Entities.Song import Song


def test_match_user(set_up):





def test_save_ratings(set_up):
    db, cursor, database = set_up
    # In case that the database is empty, create three users.
    add_user(2, db, cursor, database)
    add_user(1, db, cursor, database)
    add_user(1, db, cursor, database)
    data = {
        "userId": 1,
        "songRatings": [
            {
                "matchedUserId": 2,
                "spotify_url": "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                "rating": 4
            },
            {
                "matchedUserId": 3,
                "spotify_url": "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                "rating": 3.5
            }
        ],
        "playlistRatings": [
            {
                "matchedUserId": 2,
                "rating": 1.5
            },
            {
                "matchedUserId": 3,
                "rating": 4
            }
        ]
    }

    response = app.test_client().post('/spotify/ratings/add', json=data)

    assert response.status_code == 200 and response.json == "Success"


def test_spotify_log_in():
    # TODO: add test for spotify callback. (see if possible)
    assert True

