from src.Computation.matching import closest_user


def test_closest_user_manhattan_size_2():
    answer = closest_user([0, 0], [[1, 0, 2], [2, 2, 1], [3, 1, 1]], "manhattan", -1)
    assert answer == 1


def test_closest_user_manhattan_size_2():
    answer = closest_user([0, 0], [[1, 0, 2], [2, 2, 1], [3, 1, 1]], "euclidean", -1)
    assert answer == 3


def test_closest_user_manhattan_size_4():
    answer = closest_user([0, 0, 0, 0], [[1, 2, 2, 2, 2], [2, 1, 6, 2, 4], [3, 0, 0, 0, 6]], "manhattan", -1)
    assert answer == 3


def test_closest_user_euclidian_size_4():
    answer = closest_user([0, 0, 0, 0], [[1, 2, 2, 2, 2], [2, 1, 6, 2, 4], [3, 0, 0, 0, 6]], "euclidean", -1)
    assert answer == 1

