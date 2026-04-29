def run():
    shops = {
        'ашан': [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
        'пятерочка': [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
        'магнит': [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
    }
    
    sweets = {}
    sweet_names = ['печенье', 'конфеты', 'карамель', 'пирожное']
    
    for sweet_name in sweet_names:
        prices = []
        for shop_name in shops:
            for product in shops[shop_name]:
                if product['name'] == sweet_name:
                    prices.append({'shop': shop_name, 'price': product['price']})
        
        prices.sort(key=lambda x: x['price'])
        sweets[sweet_name] = prices[:2]
    
    print("\nТовар        Магазин       Цена")
    print("-" * 35)
    for sweet_name in sweets:
        print(f"\n{sweet_name}:")
        for shop_info in sweets[sweet_name]:
            print(f"           {shop_info['shop']:<10} {shop_info['price']} руб.")

