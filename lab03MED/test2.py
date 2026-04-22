from task2 import calc_rec, calc_norec

def test_первый_шаг():
    assert calc_rec(1, 1, 2) == (1, 2)
    assert calc_norec(1, 1, 2) == (1, 2)

def test_второй_шаг():
    assert calc_rec(2, 1, 2) == (5, 10)
    assert calc_norec(2, 1, 2) == (5, 10)

def test_третий_шаг():
    assert calc_rec(3, 1, 2) == (25, 210)
    assert calc_norec(3, 1, 2) == (25, 210)

def test_одинаково():
    assert calc_rec(3, 1, 2) == calc_norec(3, 1, 2)