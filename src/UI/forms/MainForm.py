"""Содержит класс главного окна приложения"""
import os
import threading
import time
from copy import copy

from PySide6.QtCore import QTimer, QSize, Qt, QThread
from PySide6.QtGui import QColor, QPixmap, QMovie
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QVBoxLayout, QLabel, QDialog

from src.UI.forms.StartGameDialog import StartGameDialog
from src.UI.windows.ui_agent_settings_window import Ui_AgentSettingsWindow
from src.UI.windows.ui_game_window import Ui_GameWindow
from src.UI.windows.ui_graphs_window import Ui_GraphsWindow
from src.UI.windows.ui_main_window import Ui_MainWindow
from src.UI.windows.ui_mas_info_window import Ui_MasInfoWindow
from src.UI.windows.ui_settings_window import Ui_SettingsWindow
from src.UI.windows.ui_system_settings_window import Ui_SystemSettingsWindow
from src.agents import AgentDispatcher
from src.utils.Export.Export import export_in_excel
from src.utils.statistics import Statistics
from src.utils.statistics.Statistics import write_logs, DataStatistics, Config


class MainForm(QMainWindow, Ui_MainWindow, Ui_MasInfoWindow, Ui_GraphsWindow, Ui_GameWindow,
               Ui_SettingsWindow, Ui_AgentSettingsWindow, Ui_SystemSettingsWindow):
    """
    Класс главного окна приложения. Отрисовки макетов и обработки событий.
    """

    def __init__(self, app: QApplication, dispatcher: AgentDispatcher.AgentDispatcher, scene):
        super().__init__()
        self.graph_scene = None
        self.app = app
        self.dispatcher = dispatcher
        self.scene = scene
        self.show_menu()

        self.entities_settings = {
            "Spider": {
                "speed": Config.dataset['spider']['speed'],
                "radius": Config.dataset['spider']['radius']
            },
            "Ant": {
                "speed": Config.dataset['ant']['speed'],
                "radius": Config.dataset['ant']["radius"]
            }
        }

        self.start_ants_num = Config.dataset['system']['ant_num']
        self.start_spiders_num = Config.dataset['system']['spider_num']
        self.start_apples_num = Config.dataset['system']['apple_num']

    def show_mas_info(self):
        """
        Создает макет с информацией о МАС Модели.
        """
        self.setupMasInfoUi(self)

        self.download_logs.clicked.connect(write_logs)
        self.return_button_mas_info.clicked.connect(self.show_menu)
        logs = ''
        for log in DataStatistics.all_logs[::-1][0:60]:
            logs += log + '\n'
        self.label.setText(logs)

        self.show()

    def set_on_pause(self):
        """
        Ставит диспетчер на паузу
        """
        AgentDispatcher.PAUSE = not AgentDispatcher.PAUSE

    def restart_game(self, start_game_dialog):
        AgentDispatcher.PAUSE = True
        start_game_dialog.planner.remove_all_data()
        self.show_game()

    def on_of_negotiations(self):
        if self.dispatcher.negotiations_on:
            self.mas_on_of.setText("Collective intelligence: off")
            self.dispatcher.negotiations_on = False
        else:
            self.mas_on_of.setText("Collective intelligence: on")
            self.dispatcher.negotiations_on = True

    def show_game(self):
        """
        Создает макет самой игры
        """
        scene = QGraphicsScene()
        self.graph_scene = scene
        if len(self.scene.entities) == 0:
            start_game_dialog = StartGameDialog(self.dispatcher, self.scene,
                                              1, self.start_apples_num,
                                              self.start_spiders_num,
                                              self.start_ants_num, self.entities_settings)
            self.start_apples_num = start_game_dialog.planner.apples_num
            self.start_spiders_num = start_game_dialog.planner.spdr_num
            self.start_ants_num = start_game_dialog.planner.ants_num

            if start_game_dialog.show_model:
                self.setupGameUi(self)
                self.return_button_game.clicked.connect(self.show_menu)
                self.pause_button.clicked.connect(self.set_on_pause)
                self.restart_system.clicked.connect(lambda: self.restart_game(start_game_dialog))
                self.mas_on_of.clicked.connect(self.on_of_negotiations)
                if self.dispatcher.negotiations_on:
                    self.mas_on_of.setText("Collective intelligence: on")
                else:
                    self.mas_on_of.setText("Collective intelligence: off")
                board = QGraphicsView()
                board.setScene(scene)
                board.setBackgroundBrush(QColor("#c2fab1"))
                layout = QVBoxLayout()
                layout.addWidget(board)
                self.scene_widget.setLayout(layout)

                self.rend()

                AgentDispatcher.PAUSE = False
        else:
            self.setupGameUi(self)
            self.return_button_game.clicked.connect(self.show_menu)
            self.pause_button.clicked.connect(self.set_on_pause)
            self.restart_system.clicked.connect(lambda: self.restart_game(StartGameDialog(self.dispatcher, self.scene,
                                              1, self.start_apples_num,
                                              self.start_spiders_num,
                                              self.start_ants_num, self.entities_settings)))
            self.mas_on_of.clicked.connect(self.on_of_negotiations)
            if self.dispatcher.negotiations_on:
                self.mas_on_of.setText("Negotiations: on")
            else:
                self.mas_on_of.setText("Negotiations: off")

            board = QGraphicsView()
            board.setScene(scene)
            board.setBackgroundBrush(QColor("#c2fab1"))
            layout = QVBoxLayout()
            layout.addWidget(board)
            self.scene_widget.setLayout(layout)

            self.rend()

            AgentDispatcher.PAUSE = False

    def change_radius(self, r, entity_type):
        """
        Изменяет радиус обзора на r всем сущностям типа entity_type
        :r: The radius
        :entity_type: The entity type
        :return:
        """
        r = float(r)
        self.entities_settings[entity_type]["radius"] = r
        scene_copy = self.scene.entities
        for entity in scene_copy.get(entity_type):
            entity.r = r

    def change_speed(self, speed, entity_type):
        """
        Изменяет скорость на speed всем сущностям типа entity_type
        :param speed: The speed
        :param entity_type: The entity type
        :return:
        """
        speed = float(speed)
        self.entities_settings[entity_type]["speed"] = speed
        scene_copy = self.scene.entities
        for entity in scene_copy.get(entity_type):
            entity.speed = speed

    def rend(self):
        """
        При создании макета игры, добавляет на графическую сцену графические сущности уже существующих сущностей
        """
        scene_copy = copy(self.scene.entities)
        for entities in scene_copy.values():
            if len(entities) != 0:
                if entities[0].name != 'Group':
                    for entity in entities:
                        self.graph_scene.addItem(entity.graphics_entity)
                        entity.graphics_entity.graph_scene = self.graph_scene
        self.graph_scene.advance()

    def submit_data_agent_settings(self, entity_type):
        try:
            radius = float((self.radius_input_line.text()))
            speed = float(self.speed_input_line.text())
            self.change_radius(radius,
                               entity_type)
            self.change_speed(speed, entity_type)
            self.show_menu()
        except ValueError:
            self.error_label_agent_settings.setVisible(True)

    def show_agent_settings(self, entity_type: str):
        """
        Создает макет настроек агентов паука или муравья
        :param entity_type: name of the entity(Spider or Ant)
        """
        self.load()
        self.setupAgentSettingsUi(self)

        self.error_label_agent_settings.setVisible(False)

        self.radius_input_line.setText(str(self.entities_settings[entity_type]["radius"]))

        self.speed_input_line.setText(str(self.entities_settings[entity_type]["speed"]))
        self.submit_editing_agent_settings.clicked.connect(lambda: self.submit_data_agent_settings(entity_type))

        self.return_button_agent_settings.clicked.connect(self.show_settings)

        self.show()

    def set_start_ants_num(self, num):
        self.start_ants_num = num

    def set_start_spiders_num(self, num):
        self.start_spiders_num = num

    def set_start_apples_num(self, num):
        self.start_apples_num = num

    def show_system_settings(self):
        """
        Создает макет настроек системы.
        Временные промежутки спавна яблок и пауков и начальное количество агентов в системе
        """
        self.load()
        self.setupSystemSettingsUi(self)

        self.error_label_system_settings.setVisible(False)

        self.apples_gap_input_line.setText(str(self.dispatcher.gap))
        self.return_button_system_settings.clicked.connect(self.show_settings)
        self.start_ants_num_input_line.setText(str(self.start_ants_num))
        self.start_spiders_num_input_line.setText(str(self.start_spiders_num))
        self.start_apples_num_input_line.setText(str(self.start_apples_num))
        self.submit_editing_system_settings.clicked.connect(lambda: self.submit_data_system_settings())

        self.show()

    def submit_data_system_settings(self):
        try:
            apple_gap = int(self.apples_gap_input_line.text())
            ants = int(self.start_ants_num_input_line.text())
            spiders = int(self.start_spiders_num_input_line.text())
            apples = int(self.start_apples_num_input_line.text())
            self.change_apple_gap(apple_gap)
            self.set_start_ants_num(
                int(ants))
            self.set_start_spiders_num(
                int(spiders))
            self.set_start_apples_num(
                int(apples))
            self.start_apples_num = int(self.start_apples_num_input_line.text())
            self.start_spiders_num = int(self.start_spiders_num_input_line.text())
            self.start_ants_num = int(self.start_ants_num_input_line.text())
            self.show_menu()
        except ValueError:
            self.error_label_system_settings.setVisible(True)

    def change_apple_gap(self, gap):
        """
        Изменяет количество тиков между спавном яблок на gap
        """
        self.dispatcher.gap = int(gap)

    def show_settings(self):
        """
        Создает макет настроек игры
        """
        self.setupSettingsUi(self)

        self.spiders_settings.clicked.connect(lambda: self.show_agent_settings("Spider"))
        self.ants_settins.clicked.connect(lambda: self.show_agent_settings("Ant"))
        self.system_settings.clicked.connect(self.show_system_settings)
        self.return_button_settings.clicked.connect(self.show_menu)

        self.show()

    def show_menu(self):
        """
        Создает макет меню или начального экрана
        """
        AgentDispatcher.PAUSE = True

        self.setupMainWindowUi(self)

        self.settings_button.clicked.connect(self.show_settings)
        self.mas_info_button.clicked.connect(self.show_mas_info)
        self.exit_button.clicked.connect(self.close_game)
        self.graph_button.clicked.connect(self.show_graphs)
        self.start_button.clicked.connect(self.show_game)

        path = str(os.path.abspath('../assets/images/ants_img.jpg'))
        self.image_label.setPixmap(QPixmap(path))

        self.show()

    def show_graphs(self):
        """Создает макет отображения графиков"""
        self.load()
        self.setupGraphsUi(self)
        self.return_button_graphs.clicked.connect(self.show_menu)
        self.download_graphs_button.clicked.connect(lambda: export_in_excel(Statistics.DataStatistics.data))
        self.show()

    def close_game(self):
        """Закрывает UI модели и останавливает процесс планирования системы"""
        self.dispatcher.kill = True
        self.app.quit()

    def load(self):
        # setup dialog
        dialog = QDialog()
        vbox = QVBoxLayout()
        lbl = QLabel()
        self.moviee = QMovie(os.path.abspath('assets/images/loader.gif'))
        lbl.setMovie(self.moviee)
        self.moviee.start()
        vbox.addWidget(lbl)
        dialog.setLayout(vbox)
        dialog.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        # setup thread
        thread = myThread()
        thread.finished.connect(thread.deleteLater)
        thread.finished.connect(dialog.close)
        thread.finished.connect(dialog.deleteLater)
        thread.start()

        dialog.exec()


class myThread(QThread):
    def run(self):
        # time consuming actions
        time.sleep(2)



