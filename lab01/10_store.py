#!/usr/bin/env python3
# -*- coding: utf-8 -*-

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Лампа
lamp_code = goods['Лампа']
lamp_item = store[lamp_code][0]
lamp_quantity = lamp_item['quantity']
lamp_price = lamp_item['price']
lamp_cost = lamp_quantity * lamp_price
print('Лампа -', lamp_quantity, 'шт, стоимость', lamp_cost, 'руб')

# Стол
table_code = goods['Стол']
# Первая партия столов
table_item1 = store[table_code][0]
table_quantity1 = table_item1['quantity']
table_price1 = table_item1['price']
table_cost1 = table_quantity1 * table_price1
# Вторая партия столов
table_item2 = store[table_code][1]
table_quantity2 = table_item2['quantity']
table_price2 = table_item2['price']
table_cost2 = table_quantity2 * table_price2
# Общее количество и стоимость
total_table_quantity = table_quantity1 + table_quantity2
total_table_cost = table_cost1 + table_cost2
print('Стол -', total_table_quantity, 'шт, стоимость', total_table_cost, 'руб')

# Диван
sofa_code = goods['Диван']
# Первая партия диванов
sofa_item1 = store[sofa_code][0]
sofa_quantity1 = sofa_item1['quantity']
sofa_price1 = sofa_item1['price']
sofa_cost1 = sofa_quantity1 * sofa_price1
# Вторая партия диванов
sofa_item2 = store[sofa_code][1]
sofa_quantity2 = sofa_item2['quantity']
sofa_price2 = sofa_item2['price']
sofa_cost2 = sofa_quantity2 * sofa_price2
# Общее количество и стоимость
total_sofa_quantity = sofa_quantity1 + sofa_quantity2
total_sofa_cost = sofa_cost1 + sofa_cost2
print('Диван -', total_sofa_quantity, 'шт, стоимость', total_sofa_cost, 'руб')

# Стул
chair_code = goods['Стул']
# Первая партия стульев
chair_item1 = store[chair_code][0]
chair_quantity1 = chair_item1['quantity']
chair_price1 = chair_item1['price']
chair_cost1 = chair_quantity1 * chair_price1
# Вторая партия стульев
chair_item2 = store[chair_code][1]
chair_quantity2 = chair_item2['quantity']
chair_price2 = chair_item2['price']
chair_cost2 = chair_quantity2 * chair_price2
# Третья партия стульев
chair_item3 = store[chair_code][2]
chair_quantity3 = chair_item3['quantity']
chair_price3 = chair_item3['price']
chair_cost3 = chair_quantity3 * chair_price3
# Общее количество и стоимость
total_chair_quantity = chair_quantity1 + chair_quantity2 + chair_quantity3
total_chair_cost = chair_cost1 + chair_cost2 + chair_cost3
print('Стул -', total_chair_quantity, 'шт, стоимость', total_chair_cost, 'руб')
