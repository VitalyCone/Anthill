import os.path
import random
import math

import logging
import importlib.resources

from PySide6.QtCore import QRectF

from src.GraphicsEntity.GrapicsEntity import GraphicsEntity
from src.states.SearchState import SearchState
from src.states.hunt_state import HuntState
from src.utils.statistics.Statistics import all_update
from src.entitites.BaseEntity import EntityBase


class Spider(EntityBase):
    def __init__(self, scene, id='0'):
        super().__init__()
        MODULE_PATH = importlib.resources.files("assets")
        self.name = __class__.__name__
        # в каждом классе определил переменную-имя класса,
        # чтобы агентам не надо было импортровать друг друга, чтобы не появлялась circular import error
        self.uri = self.name + str(id)
        self.geo = [random.randint(10, 490), random.randint(10, 490)]
        self.status = 'alive'
        self.speed = 0.9
        self.u = 0.57
        self.agent = None
        self.sended_objects = []
        self.energy_consumption = 0.005
        # random.uniform(0, 2 * math.pi)
        self.r = 70  # радиус обзора паука
        self.energy = 1  # энергия муравья/паука, пока что у всех она -- 1
        self.scene = []
        # булево значение, которое контролирует переход между состояниями
        # (изначально - паук не преследует никакого муравья)
        self.my_ant = None
        self.u_trig = [math.sin(self.u), math.cos(self.u)]  # угол направления паука-вектора
        self.error = math.pi / 6  # угол в радиусе которого допускается отклонение
        # 1. друзья 2.враги 3.добыча 4.угол отклонения 5.внутри карты
        self.weights = [0.2, -0.3, 0.3, 0.2, 1]  # весовые коэффициенты многофакторной целевой функции поиска
        self.friends = []  # друзья паука(здесь и в следующих массивах это имена классов-агентов)
        self.enemies = ["Spider"]  # враги пауков
        self.preys = ["Ant"]    # добыча пауков
        self.prey = None
        self.spawn = []     # обьекты для состояния спавна
        self.searchState = SearchState(self)    # создания экземпляра класса состояния поиска
        self.hunt_state = HuntState(self)
        self.removed = []
        path = str(os.path.abspath('../../assets/icons/spider.png'))
        self.graphics_entity = GraphicsEntity(self.geo,
                                              path,
                                              self.u)
        self.graphics_entity.setRect(QRectF(0, 0, 30, 30))

        logging.info(f'Объект {self.uri} был успешно инициализирован')
        all_update(f'Объект {self.uri} был успешно инициализирован')

    def agent_in_radius(self, agent):
        """
        Проверка на нахождение агента в радиусе
        :param agent:
        :return bool:
        """
        return (abs(self.geo[0] - agent.geo[0]) <= self.r) and (abs(self.geo[0] - agent.geo[0]) <= self.r)

    def process_information(self, ants):
        """
        Обработка информации от других пауков.
        Добавление агентов вне радиуса.
        :param ants:
        :return:
        """
        for ant in ants:
            if len(self.sended_objects) >= 10:
                break
            elif not self.agent_in_radius(ant):
                self.sended_objects.append(ant)

    def try_give_in_prey(self):
        for spider in self.get_specific_entities(self.scene, "Spider"):
            if self.prey and spider.prey:
                if spider.prey == self.prey:
                    if spider.get_energy(self.prey) > self.get_energy(self.prey):
                        self.prey = None

    def kill_ant(self):
        self.prey.die()
        self.energy += self.prey.energy
        self.removed.append(self.prey.get_uri())
        self.prey = None
        logging.info(f'{self.prey} был убит {self}')
        all_update(f'{self.prey} был убит {self}')

    def move(self, scene):
        super().move(scene)

        self.add_agents_to_scene(self.sended_objects)
        self.sended_objects.clear()
        if self.ants and self.spiders:
            self.agent.send_information(self.spiders, self.ants)

        # если вокруг паука нет муравьев - состояние поиска
        if len(self.ants) == 0:

            self.u = self.searchState.move(self)

        # если же вокруг паука есть муравьи - он начинает охоту
        else:

            self.hunt_state.move(self)
            # если же муравей оказался на дистанции меньшей, чем минимальное перемещение за ход, тогда муравей умирает

            if (self.prey and self.get_distance(self.prey) <
                    (self.speed + self.prey.speed)):
                self.kill_ant()

        if self.energy <= 0:
            self.die()

        self.run()
        return self.removed

    def get_best_ant(self):
        best_ant = self.ants[0]
        for ant in self.ants:  # каждый ход охоты идет проверка, точно ли выбранный муравей - лучший.
            if self.get_energy(ant) > self.get_energy(
                    best_ant):
                best_ant = ant
        return best_ant

    def get_energy(self, obj):  # возвращает энергию, полученную пауком.
        try:
            return self.energy + obj.energy - self.get_distance(obj) / (self.speed - obj.speed) * 0.01
        except ZeroDivisionError:
            return 0

    def run(self):
        """
        Реализация перемещения агента по направляющему вектору
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
