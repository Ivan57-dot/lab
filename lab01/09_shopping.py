#!/usr/bin/env python3
# -*- coding: utf-8 -*-

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

sweets = {}

for sweet_name in ['печенье', 'конфеты', 'карамель', 'пирожное']:
    prices = []
    
    for shop_name in shops:
        products = shops[shop_name]
        
        for product in products:
            if product['name'] == sweet_name:
                prices.append({
                    'shop': shop_name,
                    'price': product['price']
                })
    
    list = []
    for item in prices:
        list.append([item['price'], item])
    
    list.sort()
    
    sorted_prices = []
    for price, item in list:
        sorted_prices.append(item)
    
    sweets[sweet_name] = sorted_prices[:2]

print("\nТовар        Магазин       Цена")
print("-" * 30)

for sweet_name in sweets:
    print(f"\n{sweet_name}:")
    for shop_info in sweets[sweet_name]:
        print(f"           {shop_info['shop']:<10} {shop_info['price']} руб.")
