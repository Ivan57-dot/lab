#!/usr/bin/env python3
# -*- coding: utf-8 -*-

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)

all_flowers = garden_set | meadow_set
print('Все виды цветов:', all_flowers)

each_flowers = garden_set & meadow_set
print('В саду и на лугу:', each_flowers)

garden_flowers = garden_set - meadow_set
print('В саду:', garden_flowers)

meadow_flowers = meadow_set - garden_set
print('На лугу:', meadow_flowers)


