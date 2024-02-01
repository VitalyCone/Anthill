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
        self.prey = None
        logging.info(f'Объект {self.uri} был успешно инициализирован')
        all_update(f'Объект {self.uri} был успешно инициализирован')
        path = None
        self.graphics_entity = None

        super().__init__()

    @abstractmethod
    def run(self):
        self.energy -= 0.001

    @abstractmethod
    def move(self, scene):
        killed = []
        self.scene = scene
        self.apples = self.get_apples(self.scene)
        self.ants = self.get_ants(self.scene)
        self.spiders = self.get_spiders(self.scene)

        logging.info(f"{self} делает ход!")
        all_update(f"{self} делает ход!")

        if self.energy <= 0:
            self.die(self)
            killed.append(self.get_uri())
        self.run()
        return killed

    @abstractmethod
    def die(self, obj):  # Смерть
        try:
            pass
        except:
            pass
        logging.info(f'{self} умер')
        all_update(f'{self} умер')

    @abstractmethod
    def body(self):
        pass

    @abstractmethod
    def render(self):
        pass

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

    def get_spiders(self, scene):
        spiders = []
        for spider in scene:
            if spider.name == 'Spider':
                spiders.append(spider)
        return spiders

    def get_ants(self, scene):
        ants = []
        for ant in scene:
            if ant.name == 'Ant':
                ants.append(ant)
        return ants

    def get_apples(self, scene):
        apples = []
        for apple in scene:
            if apple.name == 'Apple':
                apples.append(apple)
        return apples

    def get_anthill(self, scene):
        anthill_1 = None
        for anthill in scene:
            if anthill.name == 'Anthill':
                anthill_1 = anthill
        return anthill_1

    def get_uri(self):
        """
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
        self.u_trig = [(entity.geo[1] - self.geo[1]) / self.get_distance(entity),
                       (entity.geo[0] - self.geo[0]) / self.get_distance(entity)]

