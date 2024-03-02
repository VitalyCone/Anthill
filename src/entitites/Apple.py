import os
import random
import math
import logging
import importlib.resources

from src.GraphicsEntity.GrapicsEntity import GraphicsEntity
from src.states.InertiaState import InertiaState
from src.utils.statistics.Statistics import all_update
from src.entitites.BaseEntity import EntityBase


class Apple(EntityBase):
    """
    Класс, представляющий сущность яблока.
    """
    def __init__(self, uri='0'):
        """
        :args:
        anthill: муравейник, к которому принадлежит яблоко.
        id: уникальный идентификатор для яблока (0 по умолчанию)
        """
        super().__init__()
        MODULE_PATH = importlib.resources.files("assets")
        self.name = __class__.__name__
        self.uri = uri
        self.status = 'alive'
        self.geo = [random.randint(10, 490), random.randint(10, 490)]
        self.r = 500
        self.u = 0
        self.u_trig = [math.sin(self.u), math.cos(self.u)]
        self.travelset = set()
        self.agent = None
        self.scene = None
        self.apples = None
        self.energy_consumption = 0
        self.ants = None
        self.spiders = None
        self.weight = 1
        self.energy = self.weight*10
        self.speed = 0
        self.inertiaState = InertiaState(self)
        path = str(os.path.abspath('../../assets/icons/apple.png'))
        self.graphics_entity = GraphicsEntity(self.geo,
                                              path,
                                              self.u)
        logging.info(
            f'Object {self.uri} was successfully initialized'
        )
        all_update(
            f'Object {self.uri} was successfully initialized'
        )

    def die(self) -> None:
        """
        Метод, который вызывается в случае поедания яблока.

        :return:
        """
        super().die()

    def move(self, scene) -> list:
        """
        Метод для перемещения яблока по сцене.
        
        param scene: Общая сцена

        return: Список удалённых объектов
        """
        super().move(scene)
        self.ants = sorted(self.ants, key=lambda x: x.get_distance(self))
        self.inertiaState.move(self)
        distance = self.get_distance(self.ants[0].anthill)
        if distance <= 20:
            self.die()
            self.removed.append([self.get_uri(), self.version])
        self.run()
        return self.removed

    def run(self) -> None:
        """
        Реализация перемещения агента по направляющему вектору.

        :return:
        """
        super().run()
        self.geo[0] += self.speed * self.u_trig[1]
        self.geo[1] += self.speed * self.u_trig[0]
