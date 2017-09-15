#!/usr/bin/python3
mass = [8, 9, 4, 10]


def my_min(x):
    tmp = x[0]
    for n in x:
        if n < tmp:
            tmp = n
    return tmp


def my_max(x):
    tmp = x[0]
    for n in x:
        if n > tmp:
            tmp = n
    return tmp


def my_mid(x):
    tmp = 0
    for n in x:
        tmp += n
    return tmp / len(x)


print ("min = ", my_min(mass))

print ("min = ", my_max(mass))

print ("mid = ", my_mid(mass))
