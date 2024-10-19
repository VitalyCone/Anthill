import logging
import sys
import os

sys.path.append(os.getcwd()[:-11])  # настройка на клиенте


from PySide6.QtWidgets import QApplication
from src.agents.AgentDispatcher import AgentDispatcher
from src.entitites.Ant import Ant
from src.entitites.Anthill import Anthill
from src.entitites.Apple import Apple
from src.entitites.Spider import Spider
from src.scene.Scene import Scene
from src.utils.statistics.Statistics import setConfig, setLocal
from src.UI.forms.MainForm import MainForm
from src.utils.path_util.path_util import resource_path
from threading import Thread



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
setLocal(resource_path('config/localization.yml'))
setConfig(resource_path('config/config.yml'))
scene = Scene()
agent_dispatcher = AgentDispatcher(scene)
# Инициализация игры
# Входные данные для моделирования


def qt_thread():
    app = QApplication(sys.argv)

    form = MainForm(app, agent_dispatcher, scene)
    agent_dispatcher.window = form
    app.exec()


def dispatch_process():
    while True:
        agent_dispatcher.run_planning()
        if agent_dispatcher.kill:
            break


if __name__ == '__main__':
    proc = Thread(target=dispatch_process)
    proc.start()
    qt_thread()
    proc.join()
