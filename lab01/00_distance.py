#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
x1, y1 = sites['Moscow']
x2, y2 = sites['London']
x3, y3 = sites['Paris']
ml = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
mp = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
lp = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
distances = {
    'Moscow': {'London': (ml), 'Paris': (mp)},
    'London': {'Moscow': (ml), 'Paris': (lp)},
    'Paris': {'Moscow': (mp), 'London': (lp)}
}
print(distances)





