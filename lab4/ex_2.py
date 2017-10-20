#!/usr/bin/env python3
from librip.gens import gen_random
from librip.gens import gen_random_one_string
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = gen_random_one_string(1, 3, 10)
data4 = list(i for i in Unique(['a', 'A', 'b', 'B'],ignore_case=False))

print(data1)
print(data2)
print(data3)
print(data4)
# Реализация задания 2