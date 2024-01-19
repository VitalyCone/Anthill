from PySide6.QtWidgets import QApplication
import logging

from src.agents.AgentDispatcher import AgentDispatcher
from src.entitites.Ant import Ant
from src.entitites.Anthill import Anthill
from src.entitites.Apple import Apple
from src.entitites.Spider import Spider
from src.scene.Scene import Scene
from src.utils.statistics.Statistics import setConfig
from src.UI.forms.MainForm import MainForm

from threading import Thread

import sys


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
setConfig('src\\scripts\\cfg\\config.yml')
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
