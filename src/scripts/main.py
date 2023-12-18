"""Файл для запуска игровой модели"""
import datetime
import logging

from src.agents.AgentDispatcher import AgentDispatcher

from src.scene.Scene import Scene

from src.entitites.Spider import Spider
from src.entitites.Ant import Ant
from src.entitites.Anthill import Anthill
from src.entitites.Apple import Apple
from src.Game.Game import Game

input_spider_num = 10
input_ant_num = 100

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    scene = Scene()
    agent_dispatcher = AgentDispatcher(scene)
    # Инициализация игры
    game = Game(scene)
    # Входные данные для моделирования
    # TODO: Расширить входные данные для пауков, муравьев и т. д. с задачей множества параметров
    input_apple_hp = 10000
    input_anthills = 1
    input_apple = 3
    input_spdr = 3
    input_ant = 30
    # Создание агентов, добавление оных в диспетчер агентов
    agent_dispatcher.add_game_entity(game)
    for i in range(input_anthills):
        anthill = Anthill(input_apple_hp, input_apple, 0, i)
        agent_dispatcher.add_entity(anthill)
    # FIXME: Добавлять объекты сцены в инициализации, а не тут
    for i in range(input_apple):
        apple = Apple(scene.get_entities_by_type('Anthill')[0], i)
        agent_dispatcher.add_entity(apple)
    for i in range(input_ant):
        ant = Ant(scene.get_entities_by_type('Apple'), scene.get_entities_by_type('Anthill')[0], i)
        agent_dispatcher.add_entity(ant)
    for i in range(input_ant):
        ant = Ant(scene.get_entities_by_type('Apple'), scene.get_entities_by_type('Anthill')[0], i)
        agent_dispatcher.add_entity(ant)
    for i in range(input_spdr):
        spider = Spider(scene.get_entities_by_type('Spider') + scene.get_entities_by_type('Apple'), i)
        agent_dispatcher.add_entity(spider)
    # rendering_process = multiprocessing.Process(target=game.render_game())
    # planning_process = multiprocessing.Process(target=agent_dispatcher.run_planning())
    start_time = datetime.datetime.now()
    while True:
        time_interval = (datetime.datetime.now() - start_time).seconds
        agent_dispatcher.run_planning()
