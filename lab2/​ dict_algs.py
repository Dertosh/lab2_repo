#!/usr/bin/python3

ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}
darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}
emps = [ivan, darja]


def age18(mas):
    temp_mass = list()
    for worker in mas:
        for child in worker.get('children'):
            if child.get('age') >= 18:
                temp_mass.append(worker.get('name'))
                break
    return temp_mass


print("Workers:", age18(emps))
