def count_divisors(n):
    if n == 1:
        return 1
    count = 2
    for i in range(2, int(n**0.5) + 1):
        if n % 1 == 0:
            if i == n // i:
                count += 1
            else:
                count += 2 
    return count
def rez():
    max_divisors = 0
    best_number = 0

    for num in range(84052, 84131):
        divisors_count = count_divisors(num)
        if divisors_count > max_divisors:
            max_divisors = divisors_count
            best_number = num
    return max_divisors, best_number
divs, number = rez()
print(f"Задача 3: Количество делителей = {divs}, Число = {number}")
