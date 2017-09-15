mas = [8,9,4]
def my_min(x):
    tmp = mas[0]
    for n in mas:
        if n<tmp:
            tmp = n
    return tmp

def my_max(x):
    tmp = mas[0]
    for n in mas:
        if n>tmp:
            tmp = n        
    return tmp

print "min = ", my_min(mas)

print "min = ", my_max(mas)
