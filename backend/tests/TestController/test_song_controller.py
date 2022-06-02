import numpy as np
from tests.fixtures import set_up
from src.Services.QuestionnaireService import add_user, add_value, add_personality
from src.Services.SongService import add_top_songs
from src.main import app
from src.Entities.Song import Song


# Tests for QuestionnaireController.
def test_save_answers(set_up):
    data = {
        "user": 101,

        "value_answers": [4, 1, 1, 4, 5, 6,
                   6, 5, 4, 3, 2, 1,
                   6, 6, 1, 1, 1, 6,
                   1, 6, 1, 6, 6, 1,
                   2, 2, 1, 2, 2, 2,
                   4, 4, 1, 4, 4, 4,
                   3, 4, 5, 5],

        "personality_answers": [1, 2, 3, 4, 5, 5, 4, 3, 2, 1,
                   1, 1, 1, 1, 1, 2, 2, 2, 2, 2,
                   3, 3, 3, 3, 3, 1, 1, 1, 4, 4,
                   1, 1, 1, 5, 5, 4, 4, 4, 4, 4,
                   3, 3, 3, 3, 3, 2, 2, 2, 2, 2,
                   5, 5, 5, 5, 5, 5, 2, 3, 4, 5]
    }

    response = app.test_client().post('/questionnaire/answer/add', json=data)

    assert response.json == {'personalities': [3.4, 2.4, 3.6, 3.3, 3.4, 3.4], 'values': [3.25, 4.0, 2.25, 3.33, 4.0,
                                                                                         3.0, 2.67, 3.75, 2.33, 4.0]}



def test_match_user(set_up):
    db, cursor, database = set_up
    # Original user to find matches to
    user = add_user(2, db, cursor, database)
    vals = np.random.rand(10)
    add_value(user, vals, db, cursor, database)
    pers = np.random.rand(6)
    add_personality(user, pers, db, cursor, database)

    user_1 = add_user(1, db, cursor, database)
    add_value(user_1, vals, db, cursor, database)
    add_top_songs(user_1, [
        Song(
            "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "JOVEN PARA SIEMPRE",
            [{"artist_name": "Funzo y Baby Loud"}],
            "https://open.spotify.com/track/2hSBhzE4hbWRWl4PLMiJsu"
        ),
        Song(
            "https://p.scdn.co/mp3-preview/ab9f4d3741dffa1c41ce156f523e440f7d288d5d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Dale",
            [{"artist_name": "Pole"}, {"artist_name": "Hens"}],
            'https://open.spotify.com/track/5JnASEjM04jp20CjK6PqfI'
        ),
        Song(
            "https://p.scdn.co/mp3-preview/cf4be4c14b31037207998ebc190973f56cf5dd4c?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Vuelve",
            [{"artist_name": "Azel"}],
            'https://open.spotify.com/track/6COq76th7tzFFi2wlcD6xj'

        ),
        Song(
            "https://p.scdn.co/mp3-preview/e851e103d110d4c1b0002346c47d344da1b1945d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Amanecer",
            [{"artist_name": "Azel"}],
            'https://open.spotify.com/track/03J7yqJA8a4eSjnFUSfCbp'
        ),
        Song(
            "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Loca",
            [{"artist_name": "Azel"}],
            'https://open.spotify.com/track/0LUwBqSMzszqZA7td5TjpK'
        )
    ], db, cursor, database)

    user_2 = add_user(1, db, cursor, database)
    add_personality(user_2, pers, db, cursor, database)
    add_top_songs(user_2, [
        Song(
            "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "JOVEN PARA SIEMPRE",
            [{"artist_name": "Funzo y Baby Loud"}],
            "https://open.spotify.com/track/2hSBhzE4hbWRWl4PLMiJsu"
        ),
        Song(
            "https://p.scdn.co/mp3-preview/ab9f4d3741dffa1c41ce156f523e440f7d288d5d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Dale",
            [{"artist_name": "Pole"}, {"artist_name": "Hens"}],
            'https://open.spotify.com/track/5JnASEjM04jp20CjK6PqfI'
        ),
        Song(
            "https://p.scdn.co/mp3-preview/cf4be4c14b31037207998ebc190973f56cf5dd4c?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Vuelve",
            [{"artist_name": "Azel"}],
            'https://open.spotify.com/track/6COq76th7tzFFi2wlcD6xj'

        ),
        Song(
            "https://p.scdn.co/mp3-preview/e851e103d110d4c1b0002346c47d344da1b1945d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Amanecer",
            [{"artist_name": "Azel"}],
            'https://open.spotify.com/track/03J7yqJA8a4eSjnFUSfCbp'
        ),
        Song(
            "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Loca",
            [{"artist_name": "Azel"}],
            'https://open.spotify.com/track/0LUwBqSMzszqZA7td5TjpK'
        )
    ], db, cursor, database)

    user_3 = add_user(1, db, cursor, database)
    add_top_songs(user_3, [
        Song(
            "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "JOVEN PARA SIEMPRE",
            [{"artist_name": "Funzo y Baby Loud"}],
            "https://open.spotify.com/track/2hSBhzE4hbWRWl4PLMiJsu"
        ),
        Song(
            "https://p.scdn.co/mp3-preview/ab9f4d3741dffa1c41ce156f523e440f7d288d5d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Dale",
            [{"artist_name": "Pole"}, {"artist_name": "Hens"}],
            'https://open.spotify.com/track/5JnASEjM04jp20CjK6PqfI'
        ),
        Song(
            "https://p.scdn.co/mp3-preview/cf4be4c14b31037207998ebc190973f56cf5dd4c?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Vuelve",
            [{"artist_name": "Azel"}],
            'https://open.spotify.com/track/6COq76th7tzFFi2wlcD6xj'

        ),
        Song(
            "https://p.scdn.co/mp3-preview/e851e103d110d4c1b0002346c47d344da1b1945d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Amanecer",
            [{"artist_name": "Azel"}],
            'https://open.spotify.com/track/03J7yqJA8a4eSjnFUSfCbp'
        ),
        Song(
            "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Loca",
            [{"artist_name": "Azel"}],
            'https://open.spotify.com/track/0LUwBqSMzszqZA7td5TjpK'
        )
    ], db, cursor, database)

    data = {"user": user, "metric": "manhattan"}

    response = app.test_client().get('/spotify/match', json=data)

    assert response.status_code == 200 and \
           response.json['match'][0]['user_id'] == user_1 and \
           response.json['match'][1]['user_id'] == user_2 and \
           response.json['match'][2]['user_id'] == user_3


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

