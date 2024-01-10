import threading
import threading
import time
from copy import copy

from PyQt6.QtCore import Qt, QThread
from PyQt6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QScrollArea,
                             QGridLayout, QGraphicsView, QGraphicsScene, QHBoxLayout, QLineEdit)
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from src.agents.AgentDispatcher import AgentDispatcher
from src.agents import AgentDispatcher
from src.utils.Graphs.Graphs import Graph
from src.utils.statistics import Statistics
from src.utils.statistics.Statistics import DataStatistics
from src.utils.Export.Export import export_in_excel


class MainWindow(QMainWindow):

    def __init__(self, app: QApplication, dispatcher: AgentDispatcher, scene):
        super().__init__()
        self.app = app
        self.scene = scene
        self.graph_scene = None
        self.setWindowTitle("Ants VS Spiders")
        self.set_screen_size()
        self.game_rendering = False
        self.dispatcher = dispatcher
        self.show_menu()
        self.lock = threading.Lock()

    def show_menu(self):
        AgentDispatcher.PAUSE = True
        self.graph_scene = None
        start_button = QPushButton('Start')
        start_button.clicked.connect(self.show_game)
        settings_button = QPushButton('Settings')
        settings_button.clicked.connect(self.show_settings)
        mas_info = QPushButton('MAS Information')
        mas_info.clicked.connect(self.show_mas_info)
        graph_button = QPushButton('Graph')
        graph_button.clicked.connect(self.show_graphs)
        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.close_game)
        layout = QVBoxLayout()
        layout.addWidget(start_button)
        layout.addWidget(graph_button)
        layout.addWidget(mas_info)
        layout.addWidget(settings_button)
        layout.addWidget(exit_button)
        container = QWidget()
        container.setLayout(layout)
        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

    def set_on_pause(self):
        AgentDispatcher.PAUSE = not AgentDispatcher.PAUSE

    def show_game(self):
        return_button = QPushButton("<--")
        return_button.clicked.connect(self.show_menu)
        pause_button = QPushButton("Pause")
        pause_button.clicked.connect(self.set_on_pause)
        hlayout = QHBoxLayout()
        hlayout.addWidget(return_button)
        hlayout.addWidget(pause_button)
        vlayout = QVBoxLayout()
        main_widget = QWidget()
        scene = QGraphicsScene()
        self.graph_scene = scene
        board = QGraphicsView()
        board.setScene(scene)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(board)
        main_widget.setLayout(vlayout)
        self.rend()
        self.setCentralWidget(main_widget)
        AgentDispatcher.PAUSE = False

    def rend(self):
        scene_copy = copy(self.scene.entities)
        for entities in scene_copy.values():
            if len(entities) != 0:
                if entities[0].name != 'Group':
                    for entity in entities:
                        self.graph_scene.addItem(entity.graphics_entity)
                        entity.graphics_entity.graph_scene = self.graph_scene
        self.graph_scene.advance()

    def show_mas_info(self):
        return_button = QPushButton("<--")
        download_logs = QPushButton("Download MAS log")
        download_logs.clicked.connect(Statistics.write_logs)
        return_button.clicked.connect(self.show_menu)
        main_widget = QWidget()
        vlayout = QVBoxLayout()
        scroll = QScrollArea()
        logs = ''
        for log in DataStatistics.all_logs[::-1][0:60]:
            logs += log + '\n'
        label = QLabel(logs)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(label)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(return_button)
        buttons_layout.addWidget(download_logs)
        vlayout.addLayout(buttons_layout)
        vlayout.addWidget(scroll)
        main_widget.setLayout(vlayout)
        self.setCentralWidget(main_widget)

    def show_settings(self):
        layout = QVBoxLayout()
        spiders_settings = QPushButton("Spider's Settings")
        spiders_settings.clicked.connect(lambda: self.show_agent_settings("Spider"))
        layout.addWidget(spiders_settings)
        ants_settings = QPushButton("Ant's Settings")
        ants_settings.clicked.connect(lambda: self.show_agent_settings("Ant"))
        layout.addWidget(ants_settings)
        system_settings = QPushButton("System Settings")
        system_settings.clicked.connect(self.show_system_settings)
        layout.addWidget(system_settings)
        return_button = QPushButton("<--")
        return_button.clicked.connect(self.show_menu)
        layout.addWidget(return_button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def change_radius(self, r, entity_type):
        r = int(r)
        scene_copy = self.scene.entities
        for entity in scene_copy.get(entity_type):
            entity.r = r

    def change_speed(self, speed, entity_type):
        speed = int(speed)
        scene_copy = self.scene.entities
        for entity in scene_copy.get(entity_type):
            entity.speed = speed

    def show_agent_settings(self, entity_type: str):
        radius_label = QLabel("Radius")
        radius_input_line = QLineEdit()
        radius_submit_button = QPushButton("Submit")
        current_radius_label = QLabel("Current: " + str(copy(self.scene.entities).get(entity_type)[0].r))
        radius_submit_button.clicked.connect(lambda: self.change_radius(radius_input_line.text(), entity_type))
        radius_layout = QHBoxLayout()
        radius_layout.addWidget(radius_label)
        radius_layout.addWidget(radius_input_line)
        radius_layout.addWidget(radius_submit_button)
        radius_layout.addWidget(current_radius_label)
        speed_label = QLabel("Speed")
        speed_input_line = QLineEdit()
        speed_submit_button = QPushButton("Submit")
        current_speed_label = QLabel("Current: " + str(copy(self.scene.entities).get(entity_type)[0].speed))
        speed_submit_button.clicked.connect(lambda: self.change_speed(speed_input_line.text(), entity_type))
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(speed_label)
        speed_layout.addWidget(speed_input_line)
        speed_layout.addWidget(speed_submit_button)
        speed_layout.addWidget(current_speed_label)
        return_button = QPushButton("<--")
        return_button.clicked.connect(self.show_settings)
        layout = QVBoxLayout()
        layout.addLayout(radius_layout)
        layout.addLayout(speed_layout)
        layout.addWidget(return_button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def change_apple_gap(self, gap):
        self.dispatcher.gap = int(gap)

    def show_system_settings(self):
        label_apple_gap = QLabel("Gap between apple spawns")
        apple_gap_input_line = QLineEdit()
        apple_gap_submit_button = QPushButton("Submit")
        apple_gap_submit_button.clicked.connect(lambda: self.change_apple_gap(apple_gap_input_line.text()))
        current_apple_gap = QLabel("Current: " + str(self.dispatcher.gap))
        apple_gap_layout = QHBoxLayout()
        apple_gap_layout.addWidget(label_apple_gap)
        apple_gap_layout.addWidget(apple_gap_input_line)
        apple_gap_layout.addWidget(apple_gap_submit_button)
        apple_gap_layout.addWidget(current_apple_gap)
        label_spider_gap = QLabel("Gap between spider spawns <Пока не работает. Надо ли?>")
        spider_gap_input_line = QLineEdit()
        spider_gap_submit_button = QPushButton("Submit")
        current_spider_gap = QLabel("Current: " + "")
        spider_gap_layout = QHBoxLayout()
        spider_gap_layout.addWidget(label_spider_gap)
        spider_gap_layout.addWidget(spider_gap_input_line)
        spider_gap_layout.addWidget(spider_gap_submit_button)
        spider_gap_layout.addWidget(current_spider_gap)
        return_button = QPushButton("<--")
        return_button.clicked.connect(self.show_settings)
        layout = QVBoxLayout()
        layout.addLayout(apple_gap_layout)
        layout.addLayout(spider_gap_layout)
        layout.addWidget(return_button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_graphs(self):
        hlayout = QHBoxLayout()
        return_button = QPushButton("<--")
        return_button.clicked.connect(self.show_menu)
        download_button = QPushButton("Download Graphs")
        download_button.clicked.connect(lambda: export_in_excel(Statistics.DataStatistics.data))
        hlayout.addWidget(return_button)
        hlayout.addWidget(download_button)
        layout = QGridLayout()
        vlayout = QVBoxLayout()
        y_names = ['Суммарные значения энергии муравьев', 'Суммарные значения энергии пауков',
                   'Значения энергии муравейника', 'Количество сообщений в системе']
        for i, y_name in enumerate(y_names):
            graph = Graph(y_name)
            canvas = FigureCanvasQTAgg(graph.load_graph())
            if i < 2:
                svlayout = QVBoxLayout()
                label = QLabel(y_name)
                svlayout.addWidget(label)
                svlayout.addWidget(canvas)
                swidget = QWidget()
                swidget.setLayout(svlayout)
                layout.addWidget(swidget, 0, i)
            else:
                svlayout = QVBoxLayout()
                label = QLabel(y_name)
                svlayout.addWidget(label)
                svlayout.addWidget(canvas)
                swidget = QWidget()
                swidget.setLayout(svlayout)
                layout.addWidget(swidget, 1, i-2)
        vlayout.addLayout(hlayout)
        vlayout.addLayout(layout)
        widget = QWidget()
        widget.setLayout(vlayout)
        self.setCentralWidget(widget)

    def close_game(self):
        self.dispatcher.kill = True
        self.app.quit()

    def set_screen_size(self):
        self.setWindowState(Qt.WindowState.WindowFullScreen)
