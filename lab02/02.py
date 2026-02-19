def rez():
    virazhenie = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255

    octal_virazhenie = oct(virazhenie)[2:]

    zero_count = octal_virazhenie.count('0')

    return zero_count 
print(f"Задача 2: {rez()}")

