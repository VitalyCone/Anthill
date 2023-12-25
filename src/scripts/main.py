"""Файл для запуска игровой модели"""
import datetime
import logging
from os import makedirs

from src.agents.AgentDispatcher import AgentDispatcher
from src.entitites.Ant import Ant
from src.entitites.Anthill import Anthill
from src.entitites.Apple import Apple
from src.entitites.Spider import Spider
from src.game.Game import Game
from src.scene.Scene import Scene

input_spider_num = 15
input_ant_num = 150


# def setup_logging():
#     n2 = str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M'))
#
#     makedirs('../../logs/' + n2, exist_ok=True)
#
#     debug_handler = logging.FileHandler('../../logs/' + n2 + '/all_logs.log', 'w', 'utf-8')
#     info_handler = logging.FileHandler('../../logs/' + n2 + '/info_logs.log', 'w', 'utf-8')
#
#     # Установка уровней
#     debug_handler.setLevel(logging.DEBUG)
#     info_handler.setLevel(logging.INFO)
#
#     # Создание форматтера
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     debug_handler.setFormatter(formatter)
#     info_handler.setFormatter(formatter)
#
#     # Инициализация корневого логгера
#     logging.basicConfig(level=logging.DEBUG, handlers=[debug_handler, info_handler])
#
#     # Пример использования
#     logging.info("Это тестовое сообщение INFO")
#     logging.debug("Это тестовое сообщение DEBUG")


if __name__ == "__main__":
    # setup_logging()
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    scene = Scene()
    agent_dispatcher = AgentDispatcher(scene)
    # Инициализация игры
    game = Game(scene)
    # Входные данные для моделирования
    # TODO: Расширить входные данные для пауков, муравьев и т. д. с задачей множества параметров
    input_apple_hp = 10000
    input_anthills = 1
    input_apple = 8
    input_spdr = 10
    input_ant = 30
    logging.info("Это тестовое сообщение INFO111111")
    logging.debug("Это тестовое сообщение DEBUG1111111")
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
