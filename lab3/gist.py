
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


class Gist ():
    # данные гистаграммы
    _data = None
    _data_sorting = dict()

    def __init__(self, date):
        self._data = date
        for number in date:
            self._data_sorting.update({number: self._data_sorting.get(number, 0) + 1})

    def get_data(self):
        return self._data

    def printHist(self):
        str_out = ""
        for age, stat in self._data_sorting.items():
            str_out += str(age).ljust(4) + str().ljust(stat, '#') + '\n'
        print( str_out)

    def showHist(self,title,title_x,title_y):

        fig, ax = plt.subplots()
        ax.hist(self._data,range(list(self._data_sorting.keys())[0],list(self._data_sorting.keys())[-1]+1),normed=1)
        ax.set_title(title)
        ax.set_xlabel(title_x)
        ax.set_ylabel(title_y)
        plt.show()

    def showBar(self,title,title_x,title_y):
        plt.bar(list(self._data_sorting.keys()), self._data_sorting.values(), color='b' )
        plt.show()
