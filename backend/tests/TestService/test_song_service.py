from src.Entities.PlaylistRating import PlaylistRating
from src.Entities.Song import Song
from src.Entities.SongRating import SongRating
from src.Services.QuestionnaireService import add_user
from src.Services.SongService import add_top_songs, get_top_songs, add_playlist_ratings, add_song_ratings


def test_add_song_ratings():
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

