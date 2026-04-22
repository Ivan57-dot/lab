from task1 import find_rec, find_norec

def test_находит_элемент():
    data = [1, 2, [3, 4, 5]]
    assert find_rec(data, 4) == 3
    assert find_norec(data, 4) == 3

def test_не_находит_элемент():
    data = [1, 2, 3]
    assert find_rec(data, 999) is None
    assert find_norec(data, 999) is None

def test_глубоко_вложенный():
    data = [1, [2, [3, [4, 5]]]]
    assert find_rec(data, 5) == 4
    assert find_norec(data, 5) == 4