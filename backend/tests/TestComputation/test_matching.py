from src.Computation.matching import calculate_distance, closest_user


def test_calculate_distance_manhattan():
    answer = calculate_distance([0, 2, 3, 6], [0, 6, 6, 6], "Manhattan")
    assert answer == 7


def test_calculate_distance_euclidean():
    answer = calculate_distance([0, 2, 3, 6], [0, 6, 6, 6], "Euclidean")
    assert answer == 5

def test_closest_user_trivial_easy():
    answer = closest_user([0, 0, 0, 0], [[20, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2]], "manhattan", -1)
    assert answer == 20


def test_closest_user_trivial():
    answer = closest_user([0, 0, 0, 0], [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [20, 0, 0, 0, 0]], "manhattan", -1)
    assert answer == 20


def test_closest_user_nontrivial():
    answer = closest_user([0, 0, 0, 0], [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [20, 20, 20, 20, 20]], "manhattan", -1)
    assert answer == 1
