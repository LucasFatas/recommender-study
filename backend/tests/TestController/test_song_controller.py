import numpy as np
from src.Entities.Song import Song
from src.Services.QuestionnaireService import add_user, add_value, add_personality
from src.Services.SongService import add_top_songs
from src.main import app


# Tests for SongController.
def test_retrieve_top_songs():
    songs = [
        Song(
            "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "JOVEN PARA SIEMPRE",
            [{"artist_name": "Funzo y Baby Loud"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/ab9f4d3741dffa1c41ce156f523e440f7d288d5d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Dale",
            [{"artist_name": "Pole"}, {"artist_name": "Hens"}]

        ),
        Song(
            "https://p.scdn.co/mp3-preview/cf4be4c14b31037207998ebc190973f56cf5dd4c?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Vuelve",
            [{"artist_name": "Azel"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/e851e103d110d4c1b0002346c47d344da1b1945d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Amanecer",
            [{"artist_name": "Azel"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Loca",
            [{"artist_name": "Azel"}]
        )
    ]
    expected = [
        {"artists": ["Funzo y Baby Loud"], "name": "JOVEN PARA SIEMPRE", "spotify_url":
        "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6"},
        {"artists": ["Pole", "Hens"], "name": "Dale", "spotify_url":
        "https://p.scdn.co/mp3-preview/ab9f4d3741dffa1c41ce156f523e440f7d288d5d?cid=8073ee0f16a64774bd0e7f8fa955b9d6"},
        {"artists": ["Azel"], "name": "Vuelve", "spotify_url":
        "https://p.scdn.co/mp3-preview/cf4be4c14b31037207998ebc190973f56cf5dd4c?cid=8073ee0f16a64774bd0e7f8fa955b9d6"},
        {"artists": ["Azel"], "name": "Amanecer", "spotify_url":
        "https://p.scdn.co/mp3-preview/e851e103d110d4c1b0002346c47d344da1b1945d?cid=8073ee0f16a64774bd0e7f8fa955b9d6"},
        {"artists": ["Azel"], "name": "Loca", "spotify_url":
        "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6"}]

    userId = add_user(1)
    add_top_songs(userId, songs)

    userId = {"userId": userId}

    response = app.test_client().get('/spotify/songs/get', json=userId)

    assert response.status_code == 200 and response.json['songs'] == expected


def test_match_user():

    # Original user to find matches to
    user = add_user(2)
    vals = np.random.rand(10)
    add_value(user, vals)
    pers = np.random.rand(6)
    add_personality(user, pers)

    user_1 = add_user(1)
    add_value(user_1, vals)
    add_top_songs(user_1, [
        Song(
            "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "JOVEN PARA SIEMPRE",
            [{"artist_name": "Funzo y Baby Loud"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/ab9f4d3741dffa1c41ce156f523e440f7d288d5d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Dale",
            [{"artist_name": "Pole"}, {"artist_name": "Hens"}]

        ),
        Song(
            "https://p.scdn.co/mp3-preview/cf4be4c14b31037207998ebc190973f56cf5dd4c?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Vuelve",
            [{"artist_name": "Azel"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/e851e103d110d4c1b0002346c47d344da1b1945d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Amanecer",
            [{"artist_name": "Azel"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Loca",
            [{"artist_name": "Azel"}]
        )
    ])

    user_2 = add_user(1)
    add_personality(user_2, pers)
    add_top_songs(user_2, [
        Song(
            "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "JOVEN PARA SIEMPRE",
            [{"artist_name": "Funzo y Baby Loud"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/ab9f4d3741dffa1c41ce156f523e440f7d288d5d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Dale",
            [{"artist_name": "Pole"}, {"artist_name": "Hens"}]

        ),
        Song(
            "https://p.scdn.co/mp3-preview/cf4be4c14b31037207998ebc190973f56cf5dd4c?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Vuelve",
            [{"artist_name": "Azel"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/e851e103d110d4c1b0002346c47d344da1b1945d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Amanecer",
            [{"artist_name": "Azel"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Loca",
            [{"artist_name": "Azel"}]
        )
    ])

    user_3 = add_user(1)
    add_top_songs(user_3, [
        Song(
            "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "JOVEN PARA SIEMPRE",
            [{"artist_name": "Funzo y Baby Loud"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/ab9f4d3741dffa1c41ce156f523e440f7d288d5d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Dale",
            [{"artist_name": "Pole"}, {"artist_name": "Hens"}]

        ),
        Song(
            "https://p.scdn.co/mp3-preview/cf4be4c14b31037207998ebc190973f56cf5dd4c?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Vuelve",
            [{"artist_name": "Azel"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/e851e103d110d4c1b0002346c47d344da1b1945d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Amanecer",
            [{"artist_name": "Azel"}]
        ),
        Song(
            "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
            "Loca",
            [{"artist_name": "Azel"}]
        )
    ])

    data = {"user": user, "metric": "manhattan"}

    response = app.test_client().get('/spotify/match', json=data)

    assert response.status_code == 200 and \
           response.json['match'][0]['user_id'] == user_1 and \
           response.json['match'][1]['user_id'] == user_2 and \
           response.json['match'][2]['user_id'] == user_3


def test_save_ratings():
    # In case that the database is empty, create three users.
    add_user(2)
    add_user(1)
    add_user(1)
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
