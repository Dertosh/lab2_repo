# -*- coding: utf-8 -*-

import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for value in items:
            temp = value[args[0]]
            if temp is not None:
                yield temp
    else:
        for value in items:
            temp = {key: value.get(key) for key in args if value[key] is not None}
            if len(temp) != 0:
                yield temp
    # Необходимо реализовать генератор


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random_one_string(begin, end, num_count):
    return list(random.randint(begin, end) for n in range(num_count))

def gen_random(begin, end, num_count):
    mass = list()
    while num_count != 0:
        mass.append(random.randint(begin, end))
        num_count -= 1
    return mass

    # Необходимо реализовать генератор
