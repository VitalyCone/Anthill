from copy import copy

from matplotlib.figure import Figure

from src.utils.statistics.Statistics import DataStatistics
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, y_name):
        self.data = DataStatistics.data
        self.x_name = 'Номер тика'
        self.y_name = y_name

    def load_graph(self) -> Figure:
        x_values = self.data.get(self.x_name)
        y_values = self.data.get(self.y_name)

        fig = Figure()
        ax = fig.add_subplot()

        ax.plot(x_values[:len(y_values)], y_values, marker=',', linestyle='-')
        # ax.x_label(self.x_name, fontweight='bold')
        # ax.ylabel(self.y_name, fontweight='bold')
        # ax.title(self.y_name, fontweight='bold')

        return fig
