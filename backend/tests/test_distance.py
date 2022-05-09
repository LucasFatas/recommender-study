from src.distance import manhattan_distance, euclidean_distance

def test_manhattan_distance_trivial():
    answer = manhattan_distance([0,0,0,0],[0,0,0,0])
    assert answer == 0


def test_manhattan_distance_nontrivial():
    answer = manhattan_distance([1,2,3,4],[4,4,4,4])
    assert answer == 6

def test_manhattan_distance_trivial():
        answer = euclidean_distance([0, 0, 0, 0], [0, 0, 0, 0])
        assert answer == 0


def test_manhattan_distance_nontrivial():
    answer = euclidean_distance([2,3,6],[6,6,6])
    assert answer == 5