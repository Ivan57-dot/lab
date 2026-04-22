import itertools

def rez():
    """
    Считает, сколько есть слов длиной 5 из букв И, В, А, Н,
    в которых есть хотя бы одна буква И.
    
    Проверка:
    >>> rez()
    781
    """
    letters = "ИВАН"
    count = 0
    
    for code in itertools.product(letters, repeat=5):
        if "И" in code:
            count += 1
    return count
