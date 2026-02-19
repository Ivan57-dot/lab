import itertools

def rez():
    letters = "ИВАН"
    count = 0

    for code in itertools.product(letters, repeat=5):
        if "И" in code:
            count += 1
    return count
print(f"Задача 1: {rez()}")

