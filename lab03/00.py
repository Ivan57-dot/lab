#Рекурсивная функция
def find_rec(data, x):
    pos = 0
    for item in data:
        if item == x:
            return pos
        if type(item) == list:
            res = find_rec(item, x)
            if res != None:
                return pos + res
        pos = pos + 1
    return None

#Без рекурсивной функции
def find_norec(data, x):
    s = [(data, 0)]
    total = 0
    while s:
        lst, start = s.pop()
        for i in range(len(lst)):
            if lst[i] == x:
                return start
            if type(lst[i]) == list:
                s.append((lst[i], start + i))
    return None

data = [1, 2, [3, 4, [5, [6, []]]]]
print("Рекурсивно: ", find_rec(data, 'spam'))
print("Без рекурсии: ", find_norec(data, 'spam'))

