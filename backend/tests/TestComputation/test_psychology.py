from src.Computation.psychology import val_calc, pers_calc, calculations


def test_val_calc():
    val_answers = [1, 2, 3, 4, 5, 6,
                   6, 5, 4, 3, 2, 1,
                   6, 6, 6, 6, 6, 6,
                   1, 1, 1, 1, 1, 1,
                   2, 2, 2, 2, 2, 2,
                   4, 4, 4, 4, 4, 4,
                   3, 3, 5, 5]

    exp_values = [1.27, -1.4, -0.57, -0.15, -0.9, 1.1, 0.6, 0.93, 0.35, -0.73]

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

    exp_values = [1.27, -1.4, -0.57, -0.15, -0.9, 1.1, 0.6, 0.93, 0.35, -0.73]
    exp_pers = [3.0, 2.8, 3.7, 3.6, 3.1, 3.4]

    assert calculations(val_answers, pers_answers) == (exp_values, exp_pers)


