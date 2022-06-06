from tests.fixtures import set_up
from src.Services.DashboardService import get_all_scores, get_all_answers, get_all_songs


def test_get_all_scores(set_up):
    db, cursor, database = set_up
    data = [(4, 3.1, 2.7, 3.7, 3.9, 2.8, 3.3, 3.0, 3.0, 2.75, 3.33, 2.5, 1.33, 3.67, 2.5, 2.67, 2.4)]

    assert data == get_all_scores(2, db, cursor, database)


def test_get_all_answers(set_up):
    db, cursor, database = set_up
    data = [(4, 0, 2), (4, 1, 4), (4, 2, 3)]

    assert get_all_answers(2, db, cursor, database) == data


def test_get_all_songs(set_up):
    db, cursor, database = set_up
    data = [(1, 'https://open.spotify.com/track/03J7yqJA8a4eSjnFUSfCbp'),
            (1, 'https://open.spotify.com/track/0LUwBqSMzszqZA7td5TjpK'),
            (1, 'https://open.spotify.com/track/2hSBhzE4hbWRWl4PLMiJsu'),
            (1, 'https://open.spotify.com/track/5JnASEjM04jp20CjK6PqfI'),
            (1, 'https://open.spotify.com/track/6COq76th7tzFFi2wlcD6xj'),
            (2, 'https://open.spotify.com/track/08o9yCplgxLM11ymhvkbl8'),
            (2, 'https://open.spotify.com/track/3lrNU0pvwTaXsgDqa55A8j'),
            (2, 'https://open.spotify.com/track/3NqwLwpzbpyvXB2wJE0Oe6'),
            (2, 'https://open.spotify.com/track/4mK6NMhrACj0W3dWPiQ72G'),
            (2, 'https://open.spotify.com/track/6X6BRvpa5Z9wW0SuxxlhmI'),
            (3, 'https://open.spotify.com/track/1emB9tyqtTOH4xLVhZsbZZ'),
            (3, 'https://open.spotify.com/track/2GiZ3sC2p1Cc2t2gbdMKsN'),
            (3, 'https://open.spotify.com/track/3nAq2hCr1oWsIU54tS98pL'),
            (3, 'https://open.spotify.com/track/4XJJCXGv7VDdmsHGwq6LCM'),
            (3, 'https://open.spotify.com/track/4zFM2jL5OmDZAoIr3vwcZh')]

    assert data == get_all_songs(1, db, cursor, database)


