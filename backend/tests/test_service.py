import json

from src.Services.QuestionnaireService import add_value, add_answers
from src.Services.database_config import change_database_for_testing
from src.Entities.Song import Song
from src.Entities.PlaylistRating import PlaylistRating
from src.Entities.SongRating import SongRating


def test_add_song_ratings():
    tup = [
        Song(
            "2hSBhzE4hbWRWl4PLMiJsu",
            "JOVEN PARA SIEMPRE",
            [{"artist_name": "Funzo y Baby Loud"}]
        ),
        Song(
            "1p0ZOyfoywejbepwfUyQAG",
            "Dale",
            [{"artist_name": "Pole"}, {"artist_name": "Hens"}]

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
    assert "Success storing of top songs" == add_top_songs(add_user(1), tup)


def test_add_answers():
    tup = [(1, 1, 1), (1, 2, 3)]
    assert "Success storing all Answers" == add_answers(tup)
def test_get_top_songs():
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

    user_id = add_user(1)
    add_top_songs(user_id, tup)
    actual = get_top_songs(user_id)

    for i, song in enumerate(actual):
        assert song.spotify_url == tup[i].spotify_url and \
               song.name == tup[i].name
        for j, artist in enumerate(song.artists):
            assert artist == tup_art[i][j]


def test_add_playlist_ratings():

    matched_user_id = add_user(2)

    playlist_ratings = [
        PlaylistRating(matched_user_id, add_user(1), 3),
        PlaylistRating(matched_user_id, add_user(1), 2),
        PlaylistRating(matched_user_id, add_user(1), 5)
    ]

    assert add_playlist_ratings(playlist_ratings) == "Success storing playlist ratings"


def test_add_song_ratings():
    matched_user_id = add_user(2)

    song_ratings = [
        SongRating(matched_user_id, add_user(1), "2hSBhzE4hbWRWl4PLMiJsu", 3),
        SongRating(matched_user_id, add_user(1), "1p0ZOyfoywejbepwfUyQAG", 2),
        SongRating(matched_user_id, add_user(1), "6COq76th7tzFFi2wlcD6xj", 5)
    ]

    assert add_song_ratings(song_ratings) == "Success storing song ratings"






def test_add_user():
    actual = add_user(1)
    assert type(actual) == int


def test_add_value():
    user_id = add_user(1)
    tup = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    assert "Success storing value" == add_value(user_id, tup)


def test_add_personality():
    user_id = add_user(1)
    tup = (1, 1, 1, 1, 1, 1)
    assert "Success storing personality" == add_personality(user_id, tup)


def test_change_database_for_testing():
    value = 0
    change_database_for_testing(False)
    with open('../src/config.json', 'r+') as f:
        data = json.load(f)
        value = data['is_testing']

    assert not json.loads(value)

    change_database_for_testing(True)
    with open('../src/config.json', 'r+') as f:
        data = json.load(f)
        value = data['is_testing']

    assert json.loads(value)



if __name__ == '__main__':
    test_change_database_for_testing()
    change_database_for_testing(True)
    test_add_answers()
    test_add_user()
    test_add_value()
    test_add_personality()

