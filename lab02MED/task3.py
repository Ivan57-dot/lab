def count_divisors(n):
    """
    Считает количество делителей числа n.
    
    Проверка:
    >>> count_divisors(1)
    1
    
    >>> count_divisors(4)
    3
    
    >>> count_divisors(12)
    6
    """
    if n == 1:
        return 1
    count = 2
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # БЫЛО: n % 1 == 0 (это ошибка!)
            if i == n // i:
                count += 1
            else:
                count += 2
    return count

def rez():
    """
    Находит число от 84052 до 84130, у которого больше всего делителей.
    
    Проверка:
    >>> rez()
    (72, 84084)
    """
    max_divisors = 0
    best_number = 0
    
    for num in range(84052, 84131):
        divisors_count = count_divisors(num)
        if divisors_count > max_divisors:
            max_divisors = divisors_count
            best_number = num
    return max_divisors, best_number
