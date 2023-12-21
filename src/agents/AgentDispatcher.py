"""Содержит класс диспетчера агентов"""
import logging
from copy import copy

from thespian.actors import ActorSystem
import traceback

from src.utils.statistics.Statistics import StatisticsAlfa
from src.agents.BaseAgent import AgentBase
from src.agents.AntAgent import AntAgent
from src.agents.SpiderAgent import SpiderAgent
from src.agents.AnthillAgent import AnthillAgent
from src.agents.AppleAgent import AppleAgent
from src.agents.SceneAgent import SceneAgent
from src.agents.GroupAgent import GroupAgent
from src.Game.GameAgent import GameAgent

from src.utils.Messages.Messages import MessageType
from src.utils.ReferenceBook.ReferenceBook import ReferenceBook

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


class AgentDispatcher(AgentBase):
    """
    Класс диспетчера агентов
    """

    def __init__(self, scene):
        super().__init__()
        self.name = 'Диспетчер агентов'
        self.actor_system = ActorSystem()
        self.reference_book = ReferenceBook()
        self.handlers = {}
        self.scene = scene
        self.create_agent(SceneAgent, scene)
        self.pause = False
        self.subscribe(MessageType.GAME_RENDERING_RESPONSE, self.handle_game_rendering_response)
        self.game_address = None
        self.statisticsalfa = StatisticsAlfa(scene)
    def handle_game_rendering_response(self, message, sender):
        """
        Обработка ответа на сообщение о рендеринге игры
        :return:
        """
        if message[1]:
            logging.info(f'Ответ на сообщение о рендеринге игры от {sender}, игра на паузе')
        else:
            logging.info(f'Ответ на сообщение о рендеринге игры от {sender}, планирование продолжается')
        self.pause = message[1]

    def run_planning(self):
        """
        Запускает игру
        """
        if not self.pause:
            entities = copy(self.reference_book.agents_entities)
            for entity in entities:
                agent = self.reference_book.get_address(entity)
                move_message = (MessageType.GIVE_CONTROL, self)
                self.actor_system.tell(agent, move_message)
            self.statisticsalfa.move()
        self.actor_system.tell(self.game_address, (MessageType.GAME_RENDERING_REQUEST, self.pause))

    def add_game_entity(self, game_entity):
        """
        Создает агента сцены с привязкой к сущности и диспетчеру агента
        :param game_entity:
        :return:
        """
        entity_type = game_entity.name
        agent = self.actor_system.createActor(GameAgent)
        init_data = {'dispatcher': self, 'scene': self.scene, 'entity': game_entity}
        init_message = (MessageType.INIT_MESSAGE, init_data)
        self.actor_system.tell(agent, init_message)
        logging.info(f'{agent} сущecтва {game_entity} был создан')
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
        return agent

    def receiveMessage(self, msg, sender):
        """
        Обрабатывает сообщения - запускает их обработку в зависимости от типа.
        :param msg:
        :param sender:
        :return:
        """
        logging.debug('%s получил сообщение: %s', self.name, msg)

        if isinstance(msg, tuple):

            message_type, message_data = msg
            if message_type in self.handlers:
                try:
                    self.handlers[message_type](msg, sender)
                except Exception as ex:
                    traceback.print_exc()
                    logging.error(ex)
            else:
                logging.warning('%s Отсутствует подписка на сообщение: %s', self.name, message_type)
        else:
            logging.error('%s Неверный формат сообщения: %s', self.name, msg)
            super().receiveMessage(msg, sender)
