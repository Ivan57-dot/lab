#Рекурсивная функция
def calc_rec(k, u, v):
    if k == 1:
        return u, v
    a_prev, b_prev = calc_rec(k-1, u, v)
    a = 2 * b_prev + a_prev
    b = 2 * b_prev * b_prev + b_prev
    return a, b

#Без рекурсивной функции
def calc_norec(k, u, v):
    a = u
    b = v
    for i in range(2, k+1): 
        new_a = 2 * b + a
        new_b = 2 * b * b + b
        a = new_a
        b = new_b
    return a, b

print("Рекурсивно: ", calc_rec(3, 1, 2))
print("Без рекурсии: ", calc_norec(3, 1, 2))
