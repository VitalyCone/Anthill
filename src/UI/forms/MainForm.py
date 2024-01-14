"""Содержит класс главного окна приложения"""
from copy import copy

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QVBoxLayout, QLabel

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
from src.utils.statistics.Statistics import write_logs, DataStatistics


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

        self.start_ants_num = 0
        self.start_spiders_num = 0
        self.start_apples_num = 0

        """
        #F0F0F0
        """

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
                                              self.start_ants_num)

        if not AgentDispatcher.PAUSE:
            AgentDispatcher.PAUSE = True
            self.setupGameUi(self)
            self.return_button_game.clicked.connect(self.show_menu)
            self.pause_button.clicked.connect(self.set_on_pause)

            board = QGraphicsView()
            board.setScene(scene)
            board.setBackgroundBrush(QColor("#c2fab1"))
            layout = QVBoxLayout()
            layout.addWidget(board)
            self.graph_scene_widget.setLayout(layout)

            self.rend()

            AgentDispatcher.PAUSE = False

    def change_radius(self, r, entity_type):
        """
        Изменяет радиус обзора на r всем сущностям типа entity_type
        :r: The radius
        :entity_type: The entity type
        :return:
        """
        r = int(r)
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
        speed = int(speed)
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

    def show_agent_settings(self, entity_type: str):
        """
        Создает макет настроек агентов паука или муравья
        :param entity_type: name of the entity(Spider or Ant)
        """
        self.setupAgentSettingsUi(self)

        self.current_radius_label.setText("Current: " + str(copy(self.scene.entities).get(entity_type)[0].r))
        self.radius_submit_button.clicked.connect(lambda: self.change_radius(self.radius_input_line.text(),
                                                                             entity_type))

        self.current_speed_label.setText("Current: " + str(copy(self.scene.entities).get(entity_type)[0].speed))
        self.speed_submit_button.clicked.connect(lambda: self.change_speed(self.speed_input_line.text(), entity_type))

        self.return_button_agent_settings.clicked.connect(self.show_settings)

        self.show()

    def show_system_settings(self):
        """
        Создает макет настроек системы.
        Временные промежутки спавна яблок и пауков и начальное количество агентов в системе
        """
        self.setupSystemSettingsUi(self)

        self.current_apples_gap.setText("Current: " + str(self.dispatcher.gap))
        self.apples_gap_submit_button.clicked.connect(lambda:
                                                      self.change_apple_gap(self.apples_gap_input_line.text()))

        self.return_button_system_settings.clicked.connect(self.show_settings)

        self.show()

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

        self.show()

    def show_graphs(self):
        """Создает макет отображения графиков"""
        self.setupGraphsUi(self)

        self.return_button_graphs.clicked.connect(self.show_menu)
        self.download_graphs_button.clicked.connect(lambda: export_in_excel(Statistics.DataStatistics.data))

        self.show()

    def close_game(self):
        """Закрывает UI модели и останавливает процесс планирования системы"""
        self.dispatcher.kill = True
        self.app.quit()
