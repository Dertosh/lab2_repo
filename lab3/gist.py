
class Gist ():
    # данные гистаграммы
    _date = dict()

    def __init__(self, date):
        for number in date:
            self._date.update({number: self._date.get(number, 0) + 1})

    def get_data(self):
        return self._date

    def __str__(self):
        str_out = ""
        for age, stat in self._date.items():
            str_out += str(age).ljust(4) + str().ljust(stat, '#') + '\n'
        return str_out
