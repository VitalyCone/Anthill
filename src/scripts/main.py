from PySide6.QtWidgets import QApplication
import logging

from src.agents.AgentDispatcher import AgentDispatcher
from src.entitites.Ant import Ant
from src.entitites.Anthill import Anthill
from src.entitites.Apple import Apple
from src.entitites.Spider import Spider
from src.scene.Scene import Scene
from src.utils.statistics.Statistics import Denotations, count_id
from src.UI.forms.MainForm import MainForm

from threading import Thread

import sys


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
scene = Scene()
agent_dispatcher = AgentDispatcher(scene)
# Инициализация игры
# Входные данные для моделирования
# TODO: Расширить входные данные для пауков, муравьев и т. д. с задачей множества параметров

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
