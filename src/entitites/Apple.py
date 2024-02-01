import os
import random
import math
import logging
import importlib.resources

import pygame
from PySide6.QtCore import QPointF

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
        self.r = 50
        self.u = random.uniform(0, 4 * math.pi)
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
        path = str(os.path.abspath('../../assets/icons/apple.png'))
        self.graphics_entity = GraphicsEntity(self.geo,
                                              path,
                                              self.u)
        logging.info(f'Объект {self.uri} был успешно инициализирован')
        all_update(f'Объект {self.uri} был успешно инициализирован')

    def body(self):
        if self.weight == 1:
            return pygame.transform.scale(self.apple_icon, (25, 25))
        if self.weight == 2:
            return pygame.transform.scale(self.apple_icon, (35, 35))
        if self.weight == 3:
            return pygame.transform.scale(self.apple_icon, (45, 45))
        if self.weight == 4:
            return pygame.transform.scale(self.apple_icon, (55, 55))

    def die(self, apple):
        apple.status = 'dead'
        self.scene.remove(apple)
        self.anthill.get_food_apple(apple)
        apple.graphics_entity.delete_entity()

    def find_travel_speed(self):
        quantity_ants = len(self.travelset)
        normal_speed = 3
        normal_weight = self.weight / self.ants[0].power
        speed = normal_speed * quantity_ants / normal_weight
        return speed

    def move(self, scene):
        killed = []
        self.scene = scene
        self.apples = self.get_apples(self.scene)  # диспетчер переопределяет сцену
        self.ants = self.get_ants(self.scene)
        self.spiders = self.get_spiders(self.scene)
        self.anthill = self.get_anthill(self.scene)

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
            self.die(self)
            self.anthill.get_food_apple(self)
            killed.append(self.get_uri())
        self.run()
        return killed

    def run(self):
        self.geo[0] += self.speed * self.u_trig[1]
        self.geo[1] += self.speed * self.u_trig[0]

    def render(self):
        self.graphics_entity.setPos(QPointF(self.geo[0], self.geo[1]))
        self.graphics_entity.setRotation(math.degrees(self.u))
