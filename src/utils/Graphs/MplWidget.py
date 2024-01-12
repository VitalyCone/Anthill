"""Содержит класс mplwidget'а"""
from PySide6.QtWidgets import QVBoxLayout, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from src.utils.Graphs.Graphs import Graph


class MplWidget(QWidget):
    """
    Класс кастомного виджета для отрисовки matplotlib графика
    """

    def __init__(self, y_name):
        """
        Создание виджета и настройка на него графика с зависимостью данных y_name от количества тиков
        """
        super().__init__()
        graph = Graph(y_name)
        self.canvas = FigureCanvas(graph.load_graph())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)
