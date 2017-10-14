# -*- coding: utf-8 -*-

# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.iter = len(items)
        self.items = items
        self.ignore_case = kwargs.get('ignore_case')

    def __next__(self):
        if self.ignore_case:
            while len(self.items) > 0:
                item = self.items.pop() 
                try: 
                    self.items.index(item)
                except ValueError:
                    return item
        else:
            flag = False
            while len(self.items) > 0:
                flag = False
                item = self.items.pop().lower()
                for temp in self.items: 
                    if item == temp.lower():
                        flag = True
                        break
                if not flag:
                    return item
        raise StopIteration

        # Нужно реализовать __next__    
        

    def __iter__(self):
        return self
