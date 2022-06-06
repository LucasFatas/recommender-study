import numpy as np
from tests.fixtures import set_up
from src.Services.QuestionnaireService import add_user, add_value, add_personality
from src.Services.SongService import add_top_songs
from src.main import app
from src.Entities.Song import Song


def test_match_user(set_up):
    response = app.test_client().get("/spotify/match?userId=4")
    expected = {
        "match": [
            {
                "songs": [
                    {
                        "artists": [
                            "Funzo & Baby Loud"
                        ],
                        "name": "JOVEN PARA SIEMPRE",
                        "preview_url": "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/2hSBhzE4hbWRWl4PLMiJsu"
                    },
                    {
                        "artists": [
                            "Pole.",
                            "Hens"
                        ],
                        "name": "Dale",
                        "preview_url": "https://p.scdn.co/mp3-preview/ab9f4d3741dffa1c41ce156f523e440f7d288d5d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/5JnASEjM04jp20CjK6PqfI"
                    },
                    {
                        "artists": [
                            "Azel"
                        ],
                        "name": "Vuelve",
                        "preview_url": "https://p.scdn.co/mp3-preview/cf4be4c14b31037207998ebc190973f56cf5dd4c?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/6COq76th7tzFFi2wlcD6xj"
                    },
                    {
                        "artists": [
                            "Azel"
                        ],
                        "name": "Amanecer",
                        "preview_url": "https://p.scdn.co/mp3-preview/e851e103d110d4c1b0002346c47d344da1b1945d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/03J7yqJA8a4eSjnFUSfCbp"
                    },
                    {
                        "artists": [
                            "Azel"
                        ],
                        "name": "Loca",
                        "preview_url": "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/0LUwBqSMzszqZA7td5TjpK"
                    }
                ],
                "user_id": 1
            },
            {
                "songs": [
                    {
                        "artists": [
                            "Funzo & Baby Loud"
                        ],
                        "name": "JOVEN PARA SIEMPRE",
                        "preview_url": "https://p.scdn.co/mp3-preview/754ac47c66968d7bed8072e826cb9eb239457e11?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/2hSBhzE4hbWRWl4PLMiJsu"
                    },
                    {
                        "artists": [
                            "Pole.",
                            "Hens"
                        ],
                        "name": "Dale",
                        "preview_url": "https://p.scdn.co/mp3-preview/ab9f4d3741dffa1c41ce156f523e440f7d288d5d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/5JnASEjM04jp20CjK6PqfI"
                    },
                    {
                        "artists": [
                            "Azel"
                        ],
                        "name": "Vuelve",
                        "preview_url": "https://p.scdn.co/mp3-preview/cf4be4c14b31037207998ebc190973f56cf5dd4c?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/6COq76th7tzFFi2wlcD6xj"
                    },
                    {
                        "artists": [
                            "Azel"
                        ],
                        "name": "Amanecer",
                        "preview_url": "https://p.scdn.co/mp3-preview/e851e103d110d4c1b0002346c47d344da1b1945d?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/03J7yqJA8a4eSjnFUSfCbp"
                    },
                    {
                        "artists": [
                            "Azel"
                        ],
                        "name": "Loca",
                        "preview_url": "https://p.scdn.co/mp3-preview/6bbc122d01a67f9aeac6c659455ee83478149c69?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/0LUwBqSMzszqZA7td5TjpK"
                    }
                ],
                "user_id": 1
            },
            {
                "songs": [
                    {
                        "artists": [
                            "Seyté"
                        ],
                        "name": "La vie est belle",
                        "preview_url": "https://p.scdn.co/mp3-preview/82297494c718dc600046790c282c19ff29dab78e?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/4zFM2jL5OmDZAoIr3vwcZh"
                    },
                    {
                        "artists": [
                            "Stromae"
                        ],
                        "name": "Invaincu",
                        "preview_url": "https://p.scdn.co/mp3-preview/3256cf09b2c0e5e15778bcb3df8ab50a625b85c8?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/2GiZ3sC2p1Cc2t2gbdMKsN"
                    },
                    {
                        "artists": [
                            "Kanye West"
                        ],
                        "name": "Waves",
                        "preview_url": "https://p.scdn.co/mp3-preview/0e7abaa6542bcb388c9487a9b0e72847141cf4af?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/3nAq2hCr1oWsIU54tS98pL"
                    },
                    {
                        "artists": [
                            "Coline & Toitoine"
                        ],
                        "name": "La salle aux lumières",
                        "preview_url": "https://p.scdn.co/mp3-preview/a89901b1a695d2e0cfd7a601344d704cb2cdab2e?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/4XJJCXGv7VDdmsHGwq6LCM"
                    },
                    {
                        "artists": [
                            "Lonepsi"
                        ],
                        "name": "La pluie, c'est le passé qui revient",
                        "preview_url": "https://p.scdn.co/mp3-preview/d45179ec202c69bfe54e38664a6a29b2f06e6d25?cid=8073ee0f16a64774bd0e7f8fa955b9d6",
                        "spotify_url": "https://open.spotify.com/track/1emB9tyqtTOH4xLVhZsbZZ"
                    }
                ],
                "user_id": 3
            }
        ]
    }
    assert response.json == expected


def test_save_ratings(set_up):
    data = {
        "userId": 5,
        "random": {
            "matchedUserId": 8,
            "playlistRating": 3,
            "songsRatings": [4, 0, 3, 0, 5],
            "songUrls": ["https://open.spotify.com/track/03J7yqJA8a4eSjnFUSfCbp",
                         "https://open.spotify.com/track/5JnASEjM04jp20CjK6PqfI",
                         "https://open.spotify.com/track/5JnASEjMfwe4jp20CjK6PqfI",
                         "https://open.spotify.com/track/03J7yqJA8eweSjFUSfCbp",
                         "https://open.spotify.com/track/03J7yawefwSjnFUSfp"],
            "comment": "",
            "questionFeedback": [4, 2, 5, 2, 5]
        },
        "values": {
            "matchedUserId": 9,
            "playlistRating": 3,
            "songsRatings": [4, 0, 3, 0, 5],
            "songUrls": ["https://open.spotify.com/track/03J7yqJA8a4jnFUSfCbp",
                         "https://open.spotify.com/track/5JnASEjM04p20CjK6PqfI",
                         "https://open.spotify.com/track/5nASEjMfwe4j20CjK6PqfI",
                         "https://open.spotify.com/track/3J7yqJweewenSfCbp",
                         "https://open.spotify.com/track/01J7gwegJA8awefwSUSfCbp"],
            "comment": "",
            "questionFeedback": [4, 2, 5, 2, 5]
        },
        "personality": {
            "matchedUserId": 10,
            "playlistRating": 3,
            "songsRatings": [4, 0, 3, 0, 5],
            "songUrls": ["https://open.spotify.com/track/03J7yqJA8a4eSjnFUSfCbp",
                         "https://open.spotify.com/track/5JnASEjM04jp20CjK6PqfI",
                         "https://open.spotify.com/track/5JnASEjMfwe4jp20CjK6PqfI",
                         "https://open.spotify.com/track/03J7yqJA8eSjnFUSfCbp",
                         "https://open.spotify.com/track/03J7yq8awefwSjnFUSfCbp"],
            "comment": "",
            "questionFeedback": [4, 2, 5, 2, 5]
        }
    }

    response = app.test_client().post('/spotify/ratings/add', json=data)

    assert response.json == "Success"


