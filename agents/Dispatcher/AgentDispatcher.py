"""Содержит класс диспетчера агентов"""
import logging


from thespian.actors import ActorSystem

from agents.Ant.AntAgent import AntAgent
from agents.Spider.SpiderAgent import SpiderAgent
from agents.Anthill.AnthillAgent import AnthillAgent
from agents.Apple.AppleAgent import AppleAgent
from agents.Scene.SceneAgent import SceneAgent

from Messages.Messages import MessageType
from agents.ReferenceBook.ReferenceBook import ReferenceBook

# В зависимости от типа сущности мы выбираем класс агента
TYPES_AGENTS = {
    'Spider': SpiderAgent,
    'Ant': AntAgent,
    'Anthill': AnthillAgent,
    'Apple': AppleAgent,
    'Scene': SceneAgent,
}


class AgentDispatcher:
    """
    Класс диспетчера агентов
    """

    def __init__(self, scene):
        self.actor_system = ActorSystem()
        self.reference_book = ReferenceBook()
        self.scene = scene
        self.create_agent(SceneAgent, scene)

    def run_planning(self):
        """
        Запускает игру
        """
        for entity in self.reference_book.agents_entities:
            agent = self.reference_book.get_address(entity)
            move_message = (MessageType.GIVE_CONTROL, self)
            self.actor_system.tell(agent, move_message)

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
