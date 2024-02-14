import logging
import math
from abc import ABC, abstractmethod

from PySide6.QtCore import QPointF

from src.utils.statistics.Statistics import all_update


class EntityBase(ABC):
    """
    Базовая реализация сущности
    """

    def __init__(self):
        self.name = 'Базовая сущность'
        self.name = __class__.__name__
        self.uri = None
        self.status = None
        self.geo = None
        self.isready = None
        self.agent = None
        self.state = None
        self.charachter = None
        self.u = None
        self.speed = None
        self.r = None
        self.energy_consumption = None
        self.attack = None
        self.speed = None
        self.r = None
        self.intravel = None
        self.damage = None
        self.power = None
        self.energy = None
        self.scene = None
        self.apples = None
        self.anthill = None
        self.ants = None
        self.spiders = None
        self.weight = None
        self.group = None
        self.u_trig = None
        self.error = None
        self.weights = None
        self.friends = None
        self.enemies = None
        self.preys = None
        self.spawn = None
        self.searchState = None
        self.removed = []
        self.prey = None
        logging.info(f'Объект {self.uri} был успешно инициализирован')
        all_update(f'Объект {self.uri} был успешно инициализирован')
        path = None
        self.graphics_entity = None

        super().__init__()

    def run(self):
        """
        :return:
        """
        self.energy -= self.energy_consumption

    def update_scene(self, scene):
        """
        Функция обновления сцены.
        :param scene:
        :return:
        """
        self.scene = scene
        self.ants = self.get_specific_entities(self.scene, "Ant")
        self.apples = self.get_specific_entities(self.scene, "Apple")
        self.spiders = self.get_specific_entities(self.scene, "Spider")

    def add_agents_to_scene(self, agents):
        """
        Добавление агентов в сцену.
        :param agents:
        :return:
        """
        if agents:
            logging.info(f'В сцену была добавлена информация от других агентов: {agents}')
            all_update(f'В сцену была добавлена информация от других агентов: {agents}')
        self.scene += agents
        self.ants += self.get_specific_entities(self.scene, "Ant")
        self.apples += self.get_specific_entities(self.scene, "Apple")
        self.spiders = self.get_specific_entities(self.scene, "Spider")

    def move(self, scene):
        """
        Функция представляет собой единичный шаг сущности.
        :param scene:
        :return:
        """
        self.removed = []
        self.update_scene(scene)

        logging.info(f"{self.uri} делает ход!")
        all_update(f"{self} делает ход!")

    def die(self):
        """
        Смерть сущности.
        :return:
        """
        self.status = 'dead'
        self.removed.append(self.get_uri())
        logging.info(f'{self} умер')
        all_update(f'{self} умер')

    def live(self, scene):
        """
        Обработка запроса на ход муравья
        :param scene:
        :return killed:
        """
        killed = self.move(scene)
        logging.info(f'Объект {self.uri} сделал ход, изменений в сцене: {len(killed)}')
        all_update(f'Объект {self.uri} сделал ход, изменений в сцене: {len(killed)}')
        return killed

    @staticmethod
    def get_specific_entities(scene, entity_type):
        """
        Возвращение сущностей указанного типа.
        :param scene:
        :param entity_type:
        :return:
        """
        entities = [entity for entity in scene if entity.name == entity_type]
        return entities

    def get_uri(self):
        """
        Возвращение уникального идентификатора.
        :return: uri
        """
        return self.uri

    def get_distance(self, obj):
        """
        Возвращает информацию о расстоянии до объекта при помощи теоремы Пифагора
        """
        return math.sqrt((self.geo[0] - obj.geo[0]) ** 2 + (self.geo[1] - obj.geo[1]) ** 2)

    def set_vector_to_object(self, entity):
        """
        Определяет направляющие векторы для движения к объекту
        :param entity:
        :return:
        """
        try:
            self.u_trig = [(entity.geo[1] - self.geo[1]) / self.get_distance(entity),
                           (entity.geo[0] - self.geo[0]) / self.get_distance(entity)]
        except ZeroDivisionError:
            self.u_trig = [0, 0]

