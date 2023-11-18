"""Содержит класс диспетчера агентов"""
import logging

from thespian.actors import ActorSystem

from agents.Ant.Ant import Ant
from agents.Spider.Spider import Spider

from Messages.Messages import MessageType
from agents.ReferenceBook.ReferenceBook import ReferenceBook

# В зависимости от типа сущности мы выбираем класс агента
TYPES_AGENTS = {
    'Ant': Ant,
    'Spider': Spider,
}


class AgentDispatcher:
    """
    Класс диспетчера агентов
    """

    def __init__(self, scene):
        self.actor_system = ActorSystem()
        self.reference_book = ReferenceBook()
        self.scene = scene

    def add_entity(self, entity):
        """
        Добавляет сущность в сцену, создает агента и отправляет ему сообщение об инициализации
        :param entity:
        :return:
        """
        entity_type = entity.name
        self.scene.entities[entity_type].append(entity)
        return True
        # TODO: Добавить агентов к сущностям
        # entity_type = entity.get_type()
        # agent_type = TYPES_AGENTS.get(entity_type)
        # if not agent_type:
        #     logging.warning(f'Для сущности типа {entity_type} не указан агент')
        #     return False
        # self.scene.entities[entity_type].append(entity)
        # self.create_agent(agent_type, entity)
        # return True

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
