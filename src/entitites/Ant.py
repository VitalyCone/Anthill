import math
import os
import random

import logging
import importlib.resources

from PySide6.QtCore import QPointF

from src.GraphicsEntity.GrapicsEntity import GraphicsEntity
from src.states.SearchState import SearchState
from src.states.defense_group_state import DefenseGroupState
from src.states.group_state import GroupState
from src.utils.statistics.Statistics import all_update
from src.entitites.BaseEntity import EntityBase


class Ant(EntityBase):

    def __init__(self, anthill, uri='0', geo=None):
        super().__init__()
        MODULE_PATH = importlib.resources.files("assets")
        self.name = __class__.__name__
        self.uri = self.name + str(uri)
        self.status = 'alive'
        self.geo = geo
        if not self.geo:
            self.geo = [random.randint(10, 490), random.randint(10, 490)]
        self.agent = None
        self.u = 0  # Случайный угол по x
        self.speed = 2
        self.r = 70
        self.energy_consumption = 0
        self.attack = False
        self.intravel = False
        self.damage = 0.4
        self.power = 1500
        self.energy = 1
        self.apples = None  # Вообще все яблоки
        self.anthill = anthill  # Муравейник
        self.ants = None  # Вообще все муравьи
        self.spiders = None  # Вообще все пауки
        self.weight = 0.2
        self.group = None
        self.u_trig = [math.sin(self.u), math.cos(self.u)]  # угол направления паука-вектора
        self.error = math.pi / 6  # угол в радиусе которого допускается отклонение
        # 1. друзья 2.враги 3.добыча 4.угол отклонения 5.внутри карты
        self.weights = [0.2, -0.3, 0.3, 0.2, 1]  # весовые коэфициенты многофактроной целевой функции поиска
        self.friends = ["Ant"]  # друзьяшки паука(здесь и в следующих массивах это имена классов-агентов)
        self.enemies = ["Spider"]  # враги пауков
        self.defensible_enemies = ["Spider"]
        self.preys = ["Apples"]    # добыча пауков
        self.group_preys = ["Apple"]
        self.spawn = []     # обьекты для состояния спавна
        self.searchState = SearchState(self)    # создания экземпляра класса состояния поиска
        self.group_state = GroupState(self)
        self.defense_group_state = DefenseGroupState(self)
        self.prey = None
        logging.info(
            f'Object {self.uri} was successfully initialized'
        )
        all_update(
            f'Object {self.uri} was successfully initialized'
                   )
        path = str(os.path.abspath('assets/icons/ant.png'))
        self.graphics_entity = GraphicsEntity(self.geo,
                                              path,
                                              self.u)

    @staticmethod
    def add_ant(scene, anthill):
        """
        Добавляет муравья в сцену, привязывает к муравейнику.
        Иначе при добавлении класса муравья в муравейник,
        происходит ошибка циклического импорта.
        :param scene:
        :param anthill:
        :return:
        """
        return Ant(scene, anthill)

    def move(self, scene):
        """
        Функция представляет собой единичный шаг сущности.
        :param scene:
        :return:
        """
        super().move(scene)

        if self.spiders:
            sorted(self.spiders,
                   key=lambda x: self.get_distance(x))  # Отсортированный по расстоянию к self список пауков
        if self.apples:
            sorted(self.apples, key=lambda x: self.get_distance(x))  # Отсортированный по расстоянию к self список яблок

        self.defense_group_state.move(self)  # При отсутствии цели ищет паука для атаки

        self.group_state.move(self)  # При отсутствии пауков ищет яблоки для перетаскивания и формировании группы

        if not self.prey:
            self.searchState.move(self)  # При отсутствии любых целей попадает в состояние поиска

        if self.energy <= 0:
            self.die()
        self.run()
        return self.removed

    def set_u(self):
        """
        Задает угол поворота муравья, исходя из синуса и косинуса этого угла
        Выбор угла ведется с поправкой на то, что изначально спрайты уже повернуты на math.pi
        """
        if (self.u_trig[0] > 0 and self.u_trig[1] > 0) or (self.u_trig[0] < 0 < self.u_trig[1]):
            self.u = math.asin(self.u_trig[0]) - math.pi/2
        elif self.u_trig[0] > 0 > self.u_trig[1]:
            self.u = math.asin(self.u_trig[0])
        elif self.u_trig[0] < 0 and self.u_trig[1] < 0:
            self.u = math.asin(self.u_trig[0]) - math.pi
        elif self.u_trig[0] == 0 and self.u_trig[1] == 1:
            self.u = -math.pi/2
        elif self.u_trig[0] == 0 and self.u_trig[1] == -1:
            self.u = math.pi/2
        elif self.u_trig[0] == 1 and self.u_trig[1] == 0:
            self.u = 0
        elif self.u_trig[0] == -1 and self.u_trig[1] == 0:
            self.u = math.pi

    def profit(self, ants, agent_resource):
        """
        Высчитывание выгоды муравья от взаимодействия с яблоком:
            без self
            вместе с self
        :param ants:
        :param agent_resource:
        :return:
        """
        speed = agent_resource.speed + 0.000001
        their_profit = (agent_resource.energy/10)/len(ants) - self.get_distance(self.anthill)/speed*self.energy_consumption
        # Если они толкают без меня!!!
        
        new_speed = (agent_resource.speed*agent_resource.weight + self.speed*self.weight)/agent_resource.weight
        our_profit = (agent_resource.energy/10)/(len(ants)+1) - self.get_distance(self.anthill)/new_speed*self.energy_consumption #Если они толкали со мной
        return our_profit - their_profit

    def run(self):
        """
        Перемещение муравья в нужном направлении.
        :return:
        """
        super().run()
        self.geo[0] += self.speed * self.u_trig[1]
        self.geo[1] += self.speed * self.u_trig[0]
        if self.geo[0] > 500:
            self.geo[0] = 500
        elif self.geo[0] < 0:
            self.geo[0] = 0
        if self.geo[1] > 500:
            self.geo[1] = 500
        elif self.geo[1] < 0:
            self.geo[1] = 0
