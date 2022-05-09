import json
from src.service import add_top_songs, get_top_songs, add_song_ratings, add_playlist_ratings, add_user
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




