from src.Computation.psychology import val_calc


def test_val_calc():
    val_answers = [1, 2, 3, 4, 5, 6,
                   6, 5, 4, 3, 2, 1,
                   6, 6, 6, 6, 6, 6,
                   1, 1, 1, 1, 1, 1,
                   2, 2, 2, 2, 2, 2,
                   4, 4, 4, 4, 4, 4,
                   3, 3, 5, 5]

    exp_values = [4.5, 2.5, 3.25, 2.83, 2.0, 4.67, 2.67, 3.75, 4.33, 4.0]

    assert val_calc(val_answers) == exp_values
