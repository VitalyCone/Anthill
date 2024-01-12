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


def add_agents_to_system():
    input_apple_hp = 10000
    input_anthills = 1
    input_apple = 4
    input_spdr = 3
    input_ant = 60
    # Создание агентов, добавление оных в диспетчер агентов
    for i in range(input_anthills):
        anthill = Anthill(input_apple_hp, input_apple, 0, count_id('anthill'))
        Denotations.uris['anthill'].append(anthill.uri)
        agent_dispatcher.add_entity(anthill)
    # FIXME: Добавлять объекты сцены в инициализации, а не тут
    for i in range(input_apple):
        apple = Apple(scene.get_entities_by_type('Anthill')[0], count_id('apple'))
        Denotations.uris['apple'].append(apple.uri)
        agent_dispatcher.add_entity(apple)
    for i in range(input_ant):
        ant = Ant(scene.get_entities_by_type('Apple'), scene.get_entities_by_type('Anthill')[0], count_id('ant'))
        Denotations.uris['ant'].append(ant.uri)
        agent_dispatcher.add_entity(ant)
    for i in range(input_spdr):
        spider = Spider(scene.get_entities_by_type('Spider') + scene.get_entities_by_type('Apple'), count_id('spider'))
        Denotations.uris['spider'].append(spider.uri)
        agent_dispatcher.add_entity(spider)

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
    add_agents_to_system()
    proc = Thread(target=dispatch_process)
    proc.start()
    qt_thread()
    proc.join()
