from src.Computation.matching import closest_user


def test_closest_user_manhattan_size_2():
    answer = closest_user([0, 0], [[1, 0, 2], [2, 2, 1], [3, 1, 1]], "manhattan")
    assert answer == 1


def test_closest_user_manhattan_size_2():
    answer = closest_user([0, 0], [[1, 0, 2], [2, 2, 1], [3, 1, 1]], "euclidean")
    assert answer == 3


def test_closest_user_manhattan_size_4():
    answer = closest_user([0, 0, 0, 0], [[1, 2, 2, 2, 2], [2, 1, 6, 2, 4], [3, 0, 0, 0, 6]], "manhattan")
    assert answer == 3


def test_closest_user_euclidian_size_4():
    answer = closest_user([0, 0, 0, 0], [[1, 2, 2, 2, 2], [2, 1, 6, 2, 4], [3, 0, 0, 0, 6]], "euclidean")
    assert answer == 1


def test_closest_user_manhattan_size_10():
    answer = closest_user([0, 0, 2, 5, 0, 1, 2, 2, 2, 2], [
        [1, 2, 2, 2, 2, 5, 1, 2, 2, 2, 2],
        [2, 1, 6, 2, 4, 1, 2, 2, 2, 2, 4],
        [3, 2, 2, 2, 2, 6, 3, 0, 0, 0, 6]],
        "manhattan")
    assert answer == 1


def test_closest_user_euclidian_size_10():
    answer = closest_user([0, 0, 2, 5, 0, 1, 2, 2, 2, 2], [
        [1, 2, 2, 2, 2, 5, 1, 2, 2, 2, 2],
        [2, 1, 6, 2, 4, 1, 2, 2, 2, 2, 4],
        [3, 2, 2, 2, 2, 6, 3, 0, 0, 0, 6]],
        "euclidean")
    assert answer == 1


def test_closest_user_manhattan_negative():
    answer = closest_user([0, 0, 0, 0], [[1, -2, -2, -2, -2], [2, -1, -6, -2, -4], [3, 0, 0, 0, -6]], "manhattan")
    assert answer == 3


def test_closest_user_euclidian_negative():
    answer = closest_user([0, 0, 0, 0], [[1, -2, -2, -2, -2], [2, -1, -6, -2, -4], [3, 0, 0, 0, -6]], "euclidean")
    assert answer == 1