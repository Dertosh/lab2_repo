#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from librip.gens import field

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': None, 'price': 2000, 'color': 'red'},
    {'title': None, 'price': None, 'color': 'green'},
    {'title': None, 'price': None, 'color': None},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1
test = field(goods,'title')
# geyrn c env
print("Test:")
for string in test:
    print(string)

test = field(goods,'title', 'color')
# geyrn c env
print("Test:")
for string in test:
    print(string)