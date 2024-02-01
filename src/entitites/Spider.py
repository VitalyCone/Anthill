import os.path
import random
import math

import logging
import importlib.resources

from PySide6.QtCore import QRectF

from src.GraphicsEntity.GrapicsEntity import GraphicsEntity
from src.states.SearchState import SearchState
from src.utils.statistics.Statistics import all_update


class Spider:
    def __init__(self, scene, id='0'):
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
        self.energy_consumption = 0.01
        # random.uniform(0, 2 * math.pi)
        self.r = 70  # радиус обзора паука
        self.energy = 1 # энергия муравья/паука, пока что у всех она -- 1
        self.scene = self.get_scene(scene)  # метод, который получает данные о всех обЪектах в области обзора паука
        self.chasing = False
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
        self.spawn = []     # обьекты для состояния спавна
        self.searchState = SearchState(self)    # создания экземпляра класса состояния поиска
        logging.info(f'Объект {self.uri} был успешно инициализирован')
        all_update(f'Объект {self.uri} был успешно инициализирован')
        path = str(os.path.abspath('../../assets/icons/spider.png'))
        self.graphics_entity = GraphicsEntity(self.geo,
                                              path,
                                              self.u)
        self.graphics_entity.setRect(QRectF(0, 0, 30, 30))

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

    def get_uri(self):
        """
        :return: uri
        """
        return self.uri

    def body(self):
        # s = random.randint(14, 20)
        # return pygame.Rect(self.geo[0], self.geo[1], s, s)
        surface = pygame.transform.rotate(self.spider_icon, math.degrees(self.u)-90)
        surface = pygame.transform.scale(surface, (30, 30))
        return surface

    def get_num_of_spiders_around(self, geo):
        # метод, который обрабатывает сцену, и ищет в ней количество пауков, в радиусе от заданных координат
        num_of_spiders = 0
        for spider in self.scene:
            if spider.name == Spider and (abs(geo[0] - spider.geo[0]) <= self.r) and (
                    abs(geo[0] - spider.geo[0]) <= self.r) and spider.geo == self.geo:
                num_of_spiders += 1
        return num_of_spiders

    def get_num_of_ants_around(self, geo):  # обрабатывает сцену и выдает кол-во пауков в радиусе обзора данной точки.
        num_of_ants = 0
        for ant in self.scene:
            if ant.name == 'Ant' and (abs(geo[0] - ant.geo[0]) <= self.r) and (abs(geo[0] - ant.geo[0]) <= self.r):
                num_of_ants += 1
        return num_of_ants

    def get_ants(self, scene):  # метод, возвращающий всех муравьев в зоне обзора
        ants = []
        for ant in scene:
            if ant.name == 'Ant':
                ants.append(ant)
        return ants

    def get_spiders(self, scene):  # метод, возвращающий всех пауков в зоне обзора
        spiders = []
        for spider in scene:
            if spider.name == 'Spider':
                spiders.append(spider)
        return spiders

    def get_apples(self, scene):
        apples = []
        for apple in scene:
            if apple.name == 'Apple':
                apples.append(apple)
        return apples

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

    def move(self, scene):
        # метод для рассчёта действий для хода муравья
        self.scene = scene
        if self.sended_objects:
            logging.info(f'В сцену была добавлена информация от других агентов: {self.sended_objects}')
            all_update(f'В сцену была добавлена информация от других агентов: {self.sended_objects}')
        self.scene += self.sended_objects
        self.sended_objects.clear()
        # получение данных из сцены и запись, только данных в области обзора паука
        ants = self.get_ants(self.scene)  # все муравьи в радиусе обзора паука
        spiders = self.get_spiders(self.scene)
        if ants and spiders:
            self.agent.send_information(spiders, ants)
        killed = []



        # fighters = []
        # for ant in ants:
        #     # if ant.attack and self.get_distance(ant) <= 20:
        #     if self.get_distance(ant) <= 40:
        #         fighters.append(ant)
        # if len(fighters) != 0:
        #     if len(fighters) <= 2:
        #         for i in range(0, len(fighters) - len(fighters) // 6):
        #             a = random.choice(fighters)
        #             a.die(a)
        #             fighters.remove(a)
        #     elif 3 <= len(fighters) <= 5:
        #         for i in range(0, len(fighters) - len(fighters) // 4):
        #             a = random.choice(fighters)
        #             a.die(a)
        #             fighters.remove(a)
        #         for i in fighters:
        #             print(i.energy)
        #             i.energy += self.energy/len(fighters)
        #             print(i.energy)
        #         print(self.name, "умер!")
        #         self.die()
        #         killed.append(self.get_uri())
        #     elif 6 <= len(fighters):
        #         for i in range(0, len(fighters) - len(fighters) // 2):
        #             a = random.choice(fighters)
        #             a.die(a)
        #             fighters.remove(a)
        #         for i in fighters:
        #             print(i.energy)
        #             i.energy += self.energy/len(fighters)
        #             print(i.energy)
        #         print(self.name, "умер!")
        #         self.die()
        #         killed.append(self.get_uri())

        #############
        if len(ants) == 0:  # если вокруг паука нет муравьев, то он продолжает находиться в состоянии поиска
            self.chasing = False
            self.my_ant = None

            self.u = self.searchState.move(self)
            self.u_trig = [math.sin(self.u), math.cos(self.u)]

        else:  # если же вокруг паука есть муравьи - он начинает охоту
            self.chasing = True
            best_ant = ants[0]
            for ant in ants:  # каждый ход охоты идет проверка, точно ли выбранный муравей - лучший.
                if self.get_energy(ant) > self.get_energy(
                        best_ant):  # если полученная энергия больше полученной энергии при охоте за лучшим муравьем, тогда назначается новый лучший муравей
                    best_ant = ant
            self.my_ant = best_ant
            distance = self.get_distance(self.my_ant)
            self.u_trig[0] = (self.my_ant.geo[1] - self.geo[1]) / distance
            self.u_trig[1] = (self.my_ant.geo[0] - self.geo[0]) / distance
            self.u = math.acos((self.my_ant.geo[0] - self.geo[0]) / distance)  # назначается угол-направление в сторону лучшего муравья.
            for spider in self.get_spiders(self.scene):
                if self.my_ant != None and spider.my_ant != None:
                    if spider.my_ant == self.my_ant:
                        if spider.get_energy(self.my_ant) > self.get_energy(self.my_ant):
                            self.my_ant = None  # нечто вроде прототипа ПВ-сетей между пауками, при выборе муравья,если они выбрали одну цель, то они вступают в что-то вроде конфликта,
                            self.chasing = False  # решая, чей профит будет выше => выше прибыль системы. Этот кусочек еще не тестировал, но его надо развивать.

            if self.my_ant and distance < (
                    self.speed + self.my_ant.speed):  # если же муравей оказался на дистанции меньшей, чем минимальное перемещение за ход, тогда муравей умирает
                self.my_ant.die(self.my_ant)
                logging.info(f'{self.my_ant} был убит {self}')
                all_update(f'{self.my_ant} был убит {self}')
                self.energy += self.my_ant.energy
                killed.append(self.my_ant.get_uri())
                self.scene.remove(self.my_ant)
                self.my_ant = None
                self.chasing = False  # муравей погибает и паук снова переходит в стадию поиска

        if self.energy <= 0:
            self.die()
            logging.info(f'{self} умер')
            all_update(f'{self} умер')
            killed.append(self.get_uri())
        self.run()
        return killed

    def get_energy(self, obj):  # возвращает энергию, полученную пауком.
        try:
            return self.energy + obj.energy - self.get_distance(obj) / (self.speed - obj.speed) * 0.01
        except ZeroDivisionError:
            return 0

    def get_distance(self, obj):  # возвращает информацию о расстоянии до обьекта при помощи любимой теоремы Пифагора
        return math.sqrt((self.geo[0] - obj.geo[0]) ** 2 + (self.geo[1] - obj.geo[1]) ** 2)

    def get_scene(self, scene):  # возвращает обьекты из сцены, в радиусе обзора паука
        scene1 = []
        for obj in scene:
            if (abs(obj.geo[0] - self.geo[0]) <= self.r) and (abs(obj.geo[1] - self.geo[1]) <= self.r):
                scene1.append(obj)
        return scene1

    def die(self):
        self.status = 'dead'

    def run(self):
        self.energy -= 0.005
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
        # self.graphics_entity.u = math.degrees(self.u)

    def render(self):
        self.graphics_entity.setRotation(math.degrees(self.u))
        self.graphics_entity.setPos(self.geo[0], self.geo[1])
