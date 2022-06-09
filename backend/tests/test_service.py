from tests.test_fixtures import set_up
from src.Services.QuestionnaireService import add_value, add_answers, add_user, add_personality
from src.Services.SongService import add_top_songs, get_top_songs, add_playlist_ratings, add_song_ratings
from src.Entities.Song import Song
from src.Entities.PlaylistRating import PlaylistRating
from src.Entities.SongRating import SongRating


def test_add_song_ratings(set_up):
    db, cursor, database = set_up

    tup = [
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
    assert "Success storing of top songs" == add_top_songs(add_user(1), tup, db, cursor, database)


def test_add_answers(set_up):
    db, cursor, database = set_up

    tup = [(1, 1, 1), (1, 2, 3)]
    assert "Success storing all Answers" == add_answers(tup, db, cursor, database)


def test_get_top_songs(set_up):
    db, cursor, database = set_up

    tup = [
        Song(
            "2hSBhzE4hbWRWl4PLMiJsu",
            "JOVEN PARA SIEMPRE",
            [{"artist_name": "Funzo y Baby Loud"}]
        ),
        Song(
            "1p0ZOyfoywejbepwfUyQAG",
            "Dale",
            [{"artist_name": "Pole."}, {"artist_name": "Hens"}, {"artist_name": "Pole"}]

        ),
        Song(
            "6COq76th7tzFFi2wlcD6xj",
            "Vuelve",
            [{"artist_name": "Azel"}]
        ),
        Song(
            "03J7yqJA8a4eSjnFUSfCbp",
            "Amanecer",
            [{"artist_name": "Azel"}]
        ),
        Song(
            "0LUwBqSMzszqZA7td5TjpK",
            "Loca",
            [{"artist_name": "Azel"}]
        )
    ]

    temp = []
    tup_art = []
    for song in tup:
        for artist in song.artists:
            temp.append(artist['artist_name'])
        tup_art.append(temp)
        temp = []

    user_id = add_user(1, db, cursor, database)
    add_top_songs(user_id, tup, db, cursor, database)
    actual = get_top_songs(user_id, db, cursor, database)

    for i, song in enumerate(actual):
        assert song.spotify_url == tup[i].spotify_url and \
               song.name == tup[i].name
        for j, artist in enumerate(song.artists):
            assert artist == tup_art[i][j]


def test_add_playlist_ratings(set_up):
    db, cursor, database = set_up

    matched_user_id = add_user(2, db, cursor, database)

    playlist_ratings = [
        PlaylistRating(matched_user_id, add_user(1, db, cursor, database), 3),
        PlaylistRating(matched_user_id, add_user(1, db, cursor, database), 2),
        PlaylistRating(matched_user_id, add_user(1, db, cursor, database), 5)
    ]

    assert add_playlist_ratings(playlist_ratings, db, cursor, database) == "Success storing playlist ratings"


def test_add_song_ratings(set_up):
    db, cursor, database = set_up

    matched_user_id = add_user(2, db, cursor, database)

    song_ratings = [
        SongRating(matched_user_id, add_user(1, db, cursor, database), "2hSBhzE4hbWRWl4PLMiJsu", 3),
        SongRating(matched_user_id, add_user(1, db, cursor, database), "1p0ZOyfoywejbepwfUyQAG", 2),
        SongRating(matched_user_id, add_user(1, db, cursor, database), "6COq76th7tzFFi2wlcD6xj", 5)
    ]

    assert add_song_ratings(song_ratings, db, cursor, database) == "Success storing song ratings"


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


