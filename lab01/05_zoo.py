#!/usr/bin/env python3
# -*- coding: utf-8 -*-

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, 'bear')
print(zoo)

birds = ['rooster', 'ostrich', 'lark', ]

zoo.extend(birds)
print(zoo)

zoo.remove('elephant')
print(zoo)

n = 0
for animal in zoo:
    if animal == 'lion':
        print("Лев сидит в", n+1, "-ой клетке")
    if animal == 'lark':
        print("Жаворонок сидит в", n+1, "-ой клетке")
    n += 1
