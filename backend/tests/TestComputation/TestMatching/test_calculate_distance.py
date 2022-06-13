from src.Computation.matching import calculate_distance


def test_calculate_distance_manhattan_size_2():
    answer = calculate_distance([0, 0], [1, 1], "Manhattan")
    assert answer == 2


def test_calculate_distance_euclidean_size_2():
    answer = calculate_distance([0, 0], [1, 1], "Euclidean")
    assert answer == 1.4142135623730951


def test_calculate_distance_manhattan_size_4():
    answer = calculate_distance([0, 2, 3, 6], [0, 6, 6, 6], "Manhattan")
    assert answer == 7


def test_calculate_distance_euclidean_size_4():
    answer = calculate_distance([0, 2, 3, 6], [0, 6, 6, 6], "Euclidean")
    assert answer == 5


def test_calculate_distance_manhattan_size_10():
    answer = calculate_distance([0, 2, 3, 6, 3, 0, 2, 3, 6, 1], [0, 6, 6, 6, 4, 0, 2, 3, 6, 0], "Manhattan")
    assert answer == 9


def test_calculate_distance_euclidean_size_10():
    answer = calculate_distance([0, 2, 3, 6, 3, 0, 2, 3, 6, 1], [0, 6, 6, 6, 4, 0, 2, 3, 6, 0], "Euclidean")
    assert answer == 5.196152422706632


def test_calculate_distance_manhattan_negative():
    answer = calculate_distance([0, -2, -3, -6], [0, -6, -6, -6], "Manhattan")
    assert answer == 7


def test_calculate_distance_euclidean_negative():
    answer = calculate_distance([0, -2, -3, -6], [0, -6, -6, -6], "Euclidean")
    assert answer == 5




