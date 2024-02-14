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
    def __init__(self, anthill, _id='0'):
        super().__init__()
        MODULE_PATH = importlib.resources.files("assets")
        self.name = __class__.__name__
        self.uri = self.name + str(_id)
        self.status = 'alive'
        self.geo = [random.randint(10, 490), random.randint(10, 490)]
        self.r = 500
        self.u = 0
        self.u_trig = [math.sin(self.u), math.cos(self.u)]
        self.travelset = set()
        self.agent = None
        self.scene = None
        self.apples = None
        self.energy_consumption = 0.01
        self.anthill = anthill
        self.ants = None
        self.spiders = None
        self.distance = ((self.anthill.geo[0] - self.geo[0]) ** 2 + (self.anthill.geo[1] - self.geo[1]) ** 2) ** 0.5
        self.weight = 1
        self.energy = self.weight
        self.speed = 0
        self.inertiaState = InertiaState(self)
        path = str(os.path.abspath('assets/icons/apple.png'))
        self.graphics_entity = GraphicsEntity(self.geo,
                                              path,
                                              self.u)
        logging.info(f'Объект {self.uri} был успешно инициализирован')
        all_update(f'Объект {self.uri} был успешно инициализирован')

    def die(self):
        super().die()
        self.anthill.get_food_apple(self)

    def move(self, scene):
        super().move(scene)

        f = self.inertiaState.move(self)
        my_ants = f[1]
        distance = self.get_distance(self.anthill)
        if distance <= 15:
            for ant in my_ants:
                ant.prey = None
                ant.state[1] = None
                print(ant.energy)
                ant.energy += (self.energy / 10) / len(my_ants)
                print(ant.energy)
            self.die()
            self.anthill.get_food_apple(self)
            self.removed.append([self.get_uri(), self.prey.version])
        self.run()
        return self.removed

    def run(self):
        super().run()
        self.geo[0] += self.speed * self.u_trig[1]
        self.geo[1] += self.speed * self.u_trig[0]
