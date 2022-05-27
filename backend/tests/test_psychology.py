from src.Computation.psychology import val_calc, pers_calc, calculations


def test_val_calc():
    val_answers = [1, 2, 3, 4, 5, 6,
                   6, 5, 4, 3, 2, 1,
                   6, 6, 6, 6, 6, 6,
                   1, 1, 1, 1, 1, 1,
                   2, 2, 2, 2, 2, 2,
                   4, 4, 4, 4, 4, 4,
                   3, 3, 5, 5]

    exp_values = [1.1, -0.9, -0.15, -0.57, -1.4, 1.27, -0.73, 0.35, 0.93, 0.6]

    assert val_calc(val_answers) == exp_values


def test_pers_calc():
    pers_answers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1,
                   1, 1, 1, 1, 1, 2, 2, 2, 2, 2,
                   3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                   5, 5, 5, 5, 5, 4, 4, 4, 4, 4,
                   3, 3, 3, 3, 3, 2, 2, 2, 2, 2,
                   1, 1, 1, 1, 1, 1, 2, 3, 4, 5
                   ]

    exp_pers = [3.0, 2.8, 3.7, 3.6, 3.1, 3.4]

    assert pers_calc(pers_answers) == exp_pers


def test_calculations():
    val_answers = [1, 2, 3, 4, 5, 6,
                   6, 5, 4, 3, 2, 1,
                   6, 6, 6, 6, 6, 6,
                   1, 1, 1, 1, 1, 1,
                   2, 2, 2, 2, 2, 2,
                   4, 4, 4, 4, 4, 4,
                   3, 3, 5, 5]

    pers_answers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1,
                   1, 1, 1, 1, 1, 2, 2, 2, 2, 2,
                   3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                   5, 5, 5, 5, 5, 4, 4, 4, 4, 4,
                   3, 3, 3, 3, 3, 2, 2, 2, 2, 2,
                   1, 1, 1, 1, 1, 1, 2, 3, 4, 5
                   ]

    exp_values = [4.5, 2.5, 3.25, 2.83, 2.0, 4.67, 2.67, 3.75, 4.33, 4.0]
    exp_pers = [3.0, 2.8, 3.7, 3.6, 3.1, 3.4]

    assert calculations(val_answers, pers_answers) == (exp_values, exp_pers)


if __name__ == '__main__':
    test_pers_calc()
    test_val_calc()
    test_calculations()
