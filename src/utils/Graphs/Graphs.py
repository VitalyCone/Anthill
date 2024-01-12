"""Содержит класс matplotlib графика"""
from copy import copy

from matplotlib.figure import Figure

from src.utils.statistics.Statistics import DataStatistics


class Graph:
    """
    Класс matplotlib графика
    """

    def __init__(self, y_name):
        self.data = copy(DataStatistics.data)
        self.x_name = 'Номер тика'
        self.y_name = y_name

    def load_graph(self) -> Figure:
        """
        Возвращает построенный график для отображения
        :return: Figure
        """
        x_values = self.data.get(self.x_name)
        y_values = self.data.get(self.y_name)

        fig = Figure()
        ax = fig.add_subplot(111)

        ax.plot(x_values[:len(y_values)], y_values, marker=',', linestyle='-')
        ax.set_title(self.y_name)
        ax.hold = False
        return fig
