"""Содержит класс диспетчера агентов"""
import logging
import sys
import time
from copy import copy

from thespian.actors import ActorSystem
import traceback

from src.entitites.Ant import Ant
from src.entitites.Spider import Spider
from src.utils.statistics.Statistics import StatisticsAlfa, Config
from src.agents.BaseAgent import AgentBase
from src.agents.AntAgent import AntAgent
from src.agents.SpiderAgent import SpiderAgent
from src.agents.AnthillAgent import AnthillAgent
from src.agents.AppleAgent import AppleAgent
from src.agents.SceneAgent import SceneAgent
from src.agents.GroupAgent import GroupAgent
from src.agents.GameAgent import GameAgent

from src.entitites.Apple import Apple

from src.utils.Messages.Messages import MessageType
from src.utils.ReferenceBook.ReferenceBook import ReferenceBook
from src.utils.statistics.Statistics import all_update, debug_update

from src.utils.statistics.Statistics import Denotations, count_id

# В зависимости от типа сущности мы выбираем класс агента
TYPES_AGENTS = {
    'Spider': SpiderAgent,
    'Ant': AntAgent,
    'Anthill': AnthillAgent,
    'Apple': AppleAgent,
    'Scene': SceneAgent,
    'Game': GameAgent,
    'Group': GroupAgent,
}

PAUSE = True


class AgentDispatcher(AgentBase):
    """
    Класс диспетчера агентов
    """

    def __init__(self, scene):
        super().__init__()
        self.name = 'Диспетчер агентов'
        self.statisticsalfa = StatisticsAlfa(scene)
        self.actor_system = ActorSystem()
        self.reference_book = ReferenceBook()
        self.handlers = {}
        self.scene = scene
        self.pause = PAUSE
        self.negotiations_on = True
        self.gap = Config.dataset['system']['apple_spawn_time']
        self.spider_gap = Config.dataset['system']['spider_spawn_time']
        self.kill = False
        self.window = None
        self.subscribe(MessageType.GAME_RENDERING_RESPONSE, self.handle_game_rendering_response)
        self.game_address = None

        self.n = 0
        self.spider_n = 0

    def create_scene_agent(self, scene):
        self.create_agent(SceneAgent, scene)

    def handle_game_rendering_response(self, message, sender):
        """
        Обработка ответа на сообщение о рендеринге игры
        :return:
        """
        if message[1]:
            logging.info(f'Ответ на сообщение о рендеринге игры от {sender}, игра на паузе')
            all_update(f'Ответ на сообщение о рендеринге игры от {sender}, игра на паузе')

        else:
            logging.info(f'Ответ на сообщение о рендеринге игры от {sender}, планирование продолжается')
            all_update(f'Ответ на сообщение о рендеринге игры от {sender}, планирование продолжается')
        self.pause = message[1]

    def create_apple(self):
        """
        Создает яблоко рандомно каждые n тиков
        """
        self.n += 1
        if self.n == self.gap:
            apple = Apple(self.scene.get_entities_by_type('Anthill')[0], count_id('apple'))
            self.window.graph_scene.addItem(apple.graphics_entity)
            apple.graphics_entity.graph_scene = self.window.graph_scene
            Denotations.uris['apple'].append(apple.uri)
            self.add_entity(apple)
            self.n = 0

    def create_spider(self):
        """
        Создает яблоко рандомно каждые n тиков
        """
        self.spider_n += 1
        if self.n == self.spider_gap:
            for i in range(self.scene.get_entities_by_type('Spider')/5 + 1):
                spider = Spider(self.scene.get_entities_by_type('Spider') + self.scene.get_entities_by_type('Apple'),
                                count_id('spider'))
                self.window.graph_scene.addItem(spider.graphics_entity)
                spider.graphics_entity.graph_scene = self.window.graph_scene
                Denotations.uris['spider'].append(spider.uri)
                self.add_entity(spider)

    def create_ant(self):
        """
        Создает яблоко рандомно каждые n тиков
        """
        ant = Ant(self.scene.get_entities_by_type('Apple'), self.scene.get_entities_by_type('Anthill')[0],
                  count_id('ant'))
        self.window.graph_scene.addItem(ant.graphics_entity)
        ant.graphics_entity.graph_scene = self.window.graph_scene
        Denotations.uris['ant'].append(ant.uri)
        self.add_entity(ant)

    def run_planning(self):
        """
        Запускает игру
        """
        if not PAUSE:
            scene_copy = copy(self.scene.entities)
            for entities in scene_copy.values():
                for entity in entities:
                    agent = self.reference_book.get_address(entity)
                    if agent:
                        move_message = (MessageType.GIVE_CONTROL, self)
                        self.actor_system.tell(agent, move_message)
            self.create_apple()
            self.create_spider()
            self.statisticsalfa.move()
        # self.actor_system.tell(self.game_address, (MessageType.GAME_RENDERING_REQUEST, self.pause))

    def add_game_entity(self, game_entity):
        """
        Создает агента сцены с привязкой к сущности и диспетчеру агента
        :param game_entity:
        :return:
        """
        agent = self.actor_system.createActor(GameAgent)
        init_data = {'dispatcher': self, 'scene': self.scene, 'entity': game_entity}
        init_message = (MessageType.INIT_MESSAGE, init_data)
        self.actor_system.tell(agent, init_message)
        logging.info(f'{agent} сущecтва {game_entity} был создан')
        all_update(f'{agent} сущecтва {game_entity} был создан')
        self.game_address = agent

    def add_entity(self, entity):
        """
        Добавляет сущность в сцену, создает агента и отправляет ему сообщение об инициализации
        :param entity:
        :return:
        """
        entity_type = entity.name
        self.scene.entities[entity_type].append(entity)
        agent_type = TYPES_AGENTS.get(entity_type)
        logging.info(f'{entity} был добавлен в сцену')
        all_update(f'{entity} был добавлен в сцену')
        if agent_type:
            self.create_agent(agent_type, entity)
            return True
        return False

    def create_agent(self, agent_class, entity):
        """
        Создает агента заданного класса с привязкой к сущности
        :param agent_class:
        :param entity:
        :return:
        """
        agent = self.actor_system.createActor(agent_class)
        self.reference_book.add_agent(entity=entity, agent_address=agent)
        init_data = {'dispatcher': self, 'scene': self.scene, 'entity': entity}
        init_message = (MessageType.INIT_MESSAGE, init_data)
        self.actor_system.tell(agent, init_message)
        logging.info(f'{agent} сущecтва {entity} был создан')
        all_update(f'{agent} сущecтва {entity} был создан')
        return agent

    def receiveMessage(self, msg, sender):
        """
        Обрабатывает сообщения - запускает их обработку в зависимости от типа.
        :param msg:
        :param sender:
        :return:
        """
        logging.debug('%s получил сообщение: %s', self.name, msg)
        debug_update(f'{self.name} получил сообщение: {msg}')

        if isinstance(msg, tuple):

            message_type, message_data = msg
            if message_type in self.handlers:
                try:
                    self.handlers[message_type](msg, sender)
                except Exception as ex:
                    traceback.print_exc()
                    logging.error(ex)
                    all_update(traceback.format_exc())
            else:
                logging.warning('%s Отсутствует подписка на сообщение: %s', self.name, message_type)
                all_update(f'{self.name} Отсутствует подписка на сообщение: {message_type}')
        else:
            logging.error('%s Неверный формат сообщения: %s', self.name, msg)
            all_update(f'{self.name} Неверный формат сообщения {msg}')
            super().receiveMessage(msg, sender)
