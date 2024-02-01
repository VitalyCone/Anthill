import math
import os
import random

import logging
import importlib.resources

from PySide6.QtCore import QPointF

from src.GraphicsEntity.GrapicsEntity import GraphicsEntity
from src.states.SearchState import SearchState
from src.utils.statistics.Statistics import all_update


class Ant:

    def __init__(self, scene, anthill, id='0'):
        MODULE_PATH = importlib.resources.files("assets")
        self.name = __class__.__name__
        self.uri = self.name + str(id)
        self.status = 'alive'
        self.geo = [random.randint(10, 490), random.randint(10, 490)]  # [50,344]
        self.isready = False
        self.agent = None
        self.state = [0, 0]  # Параметр, содержащий состояние state[0] и объект, связанный с состоянием state[1]
        # state[0] = 0 - в поиске яблока, 1 - нашел яблоко, тащит в муравейник,
        # 2 - атакует паук, нужно вместе его забороть, 3 - конец игры. нужно идти с муравейнику.
        # 4 - Убегает от паука, поскольку рядом нет товарищей/не способны оказать должное
        # Сопротивление пауку
        self.charachter = random.randint(0, 1)  # Характер. 0 - трусливый, 1 - доблестный
        self.u = 0 # Случайный угол по x
        self.speed = 0.8
        self.r = 70
        self.energy_consumption = 1/100
        self.attack = False
        if self.charachter == 0:  # Если трус, то выше скорость, но ниже радиус обзора
            self.speed = 0.5
            self.r = 50
        elif self.charachter == 1:  # Если доблестный, то наоборот
            self.speed = 0.3  # Скорость муравья
            self.r = 70  # Радиус зрения муравья
        self.intravel = False
        self.damage = 0.2
        self.power = 1500
        self.energy = random.uniform(0.01, 1)
        self.scene = scene  # Сцена
        self.apples = self.get_apples(self.scene)  # Вообще все яблоки
        self.anthill = anthill  # Муравейник
        self.ants = self.get_ants(self.scene)  # Вообще все муравьи
        self.spiders = self.get_spiders(self.scene)  # Вообще все пауки
        self.weight = 0.2
        self.group = None
        self.u_trig = [math.sin(self.u), math.cos(self.u)]  # угол направления паука-вектора
        self.error = math.pi / 6  # угол в радиусе которого допускается отклонение
        # 1. друзья 2.враги 3.добыча 4.угол отклонения 5.внутри карты
        self.weights = [0.2, -0.3, 0.3, 0.2, 1]  # весовые коэфициенты многофактроной целевой функции поиска
        self.friends = ["Ant"]  # друзьяшки паука(здесь и в следующих массивах это имена классов-агентов)
        self.enemies = ["Spider"]  # враги пауков
        self.preys = ["Apples"]    # добыча пауков
        self.spawn = []     # обьекты для состояния спавна
        self.searchState = SearchState(self)    # создания экземпляра класса состояния поиска
        self.prey = None
        logging.info(f'Объект {self.uri} был успешно инициализирован')
        all_update(f'Объект {self.uri} был успешно инициализирован')
        path = str(os.path.abspath('../../assets/icons/ant.png'))
        self.graphics_entity = GraphicsEntity(self.geo,
                                              path,
                                              self.u)

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

    def get_spiders(self, scene):  # Фукнция возвращает всех пауков из сцены
        spiders = []
        for spider in scene:
            if spider.name == 'Spider':
                spiders.append(spider)
        return spiders

    def get_ants(self, scene):  # Возвращает всех муравьев из сцены
        ants = []
        for ant in scene:
            if ant.name == 'Ant':
                ants.append(ant)
        return ants

    def get_apples(self, scene):  # Возвращает все яблоки из сцены
        apples = []
        for apple in scene:
            if apple.name == 'Apple':
                apples.append(apple)
        return apples

    def get_anthill(self, scene):  # Возвращает муравейники сцены(задел на будущее)
        anthill_1 = None
        for anthill in scene:
            if anthill.name == 'Anthill':
                anthill_1 = anthill
        return anthill_1
    
    def add_ant(self, scene, anthill):
        return Ant(scene, anthill)

    def body(self):  # Построение тела на карте
        # if self.charachter == 0:  # Трус - чуть поменьше
        #     s = random.randint(4, 5)
        #     return pygame.Rect(self.geo[0], self.geo[1], s,
        #                        s)  # Небольшая рандомизация размера каждый вызов даёт ощущения движения
        # elif self.charachter == 1:  # Доблестный - чуть побольше
        #     s = random.randint(7, 8)
        #     return pygame.Rect(self.geo[0], self.geo[1], s, s)  # Идентично
        if self.charachter == 0:
            surface = pygame.transform.rotate(self.ant_icon[0], math.degrees(self.u) - 90)
            surface = pygame.transform.scale(surface, (12, 12))
        if self.charachter == 1:
            surface = pygame.transform.rotate(self.ant_icon[1], math.degrees(self.u) - 90)
            surface = pygame.transform.scale(surface, (20, 20))
        return surface
        
    def get_nearest(self, agents):
        nearest_agent = agents[0]
        for agent in agents:
            if self.get_distance(agent) < self.get_distance(nearest_agent):
                nearest_agent = agent
        return nearest_agent

    def die(self, ant):  # Смерть
        try:  # Через try/except, потому что иногда выскакивают ошибки
            self.ants.remove(ant)
            self.scene.remove(ant)
            ant.status = 'dead'
        except:
            pass
        logging.info(f'{self} умер')
        all_update(f'{self} умер')

    def move(self, scene):
        killed = []
        self.scene = scene
        self.apples = self.get_apples(self.scene)
        self.ants = self.get_ants(self.scene)
        self.spiders = self.get_spiders(self.scene)
        # получение данных из сцены и запись, только данных в области обзора паука
        logging.info(f"{self} делает ход!")
        all_update(f"{self} делает ход!")

        if self.spiders:
            sorted(self.spiders,
                   key=lambda x: self.get_distance(x))  # Отсортированный по расстоянию к self список пауков
        if self.apples:
            sorted(self.apples, key=lambda x: self.get_distance(x))  # Отсортированный по расстоянию к self список яблок
            if self.apples[0] != self.get_nearest(self.apples):
                self.apples.append(self.apples[0])
                self.apples[0] = self.get_nearest(self.apples)

        if not self.prey:
            self.u = self.searchState.move(self)
            self.u_trig = [math.sin(self.u), math.cos(self.u)]
            if self.apples or self.spiders:
                self.prey = self.choose_prey()
                self.agent.create_group(self.prey, self)
        else:
            if self.prey.name == 'Apple':
                if self.get_distance(self.prey) >= self.speed - self.prey.speed:
                    self.set_vector_to_object(self.prey)
                    self.set_u()
                else:
                    self.set_vector_to_object(self.anthill)
                    self.set_u()
            elif self.prey.name == 'Spider' and self.group:
                self.set_vector_to_object(self.prey)
                if not self.attack:
                    if self == self.group.leader:
                        self.u_trig[0] = -self.u_trig[0]
                        self.u_trig[1] = -self.u_trig[1]
                        self.set_u()
                    else:
                        self.set_vector_to_object(self.group.leader)
                        self.set_u()
                else:
                    self.set_vector_to_object(self.prey)
                    self.set_u()

        if self.energy <= 0:
            self.die(self)
            killed.append(self.get_uri())
        self.run()
        return killed

    def choose_prey(self):
        """
        Выбирает жертву
        """
        if self.spiders:
            best_prey = self.spiders[0]
            for spider in self.spiders:
                if spider.energy > best_prey.energy:
                    best_prey = spider
            return best_prey
        else:
            best_prey = self.apples[0]
            for apple in self.apples:
                if apple.energy > best_prey.energy:
                    best_prey = apple
            return best_prey

    def set_vector_to_object(self, entity):
        """
        Определяет направляющие векторы для движения к объекту
        :param entity:
        :return:
        """
        self.u_trig = [(entity.geo[1] - self.geo[1]) / self.get_distance(entity),
                       (entity.geo[0] - self.geo[0]) / self.get_distance(entity)]

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

    def get_distance(self, obj):
        """
        Возвращает информацию о расстоянии до объекта при помощи теоремы Пифагора
        """
        return math.sqrt((self.geo[0] - obj.geo[0]) ** 2 + (self.geo[1] - obj.geo[1]) ** 2)

    def accept_message(self, param, obj):  # Функция принятия сообщения. 0 - принятия просьбы о помощи
        if param == 0:
            if self.charachter == 0:
                if self.state[0] != 2 and self.get_distance(obj) <= self.r * 3:
                    self.state = [2, obj]
                elif obj in self.spiders:
                    self.state = [4, obj]
            elif self.charachter == 1:
                if self.state[0] != 2 and self.get_distance(obj) <= self.r * 3:
                    self.state = [2, obj]
                elif obj in self.spiders:
                    self.state = [4, obj]

    def send_message_to_radius(self, param, ants,
                               obj=0):  # Функция разослать сообщение всем в радиусе. param = 0 - помогите убить паука
        if param == 0:
            if len(ants) > 3:
                for ant in ants:
                    ant.accept_message(param, obj)
                return True
            else:
                return False

    def profit(self, ants, agent_resource):
        speed = agent_resource.speed + 0.000001
        their_profit = (agent_resource.energy/10)/len(ants) - self.get_distance(self.anthill)/speed*self.energy_consumption
        # Если они толкают без меня!!!
        
        new_speed = (agent_resource.speed*agent_resource.weight + self.speed*self.weight)/agent_resource.weight
        our_profit = (agent_resource.energy/10)/(len(ants)+1) - self.get_distance(self.anthill)/new_speed*self.energy_consumption #Если они толкали со мной
        return our_profit - their_profit

    def get_scene(self, scene):
        # возвращает обьекты из сцены, в радиусе обзора паука
        scene1 = set()
        for obj in scene:
            if obj.name == "Ant":
                if (abs(obj.geo[0] - self.geo[0]) <= self.r * 1.5) and (abs(obj.geo[1] - self.geo[1]) <= self.r * 1.5):
                    scene1.add(obj)
            elif obj.name == "Apple":
                if (abs(obj.geo[0] - self.geo[0]) <= self.r * 2) and (abs(obj.geo[1] - self.geo[1]) <= self.r * 2):
                    scene1.add(obj)
            else:
                if (abs(obj.geo[0] - self.geo[0]) <= self.r) and (abs(obj.geo[1] - self.geo[1]) <= self.r):
                    scene1.add(obj)
        return scene1

    def run(self):
        # метод, который перемещает муравья в нужном направлении, после рассчета хода(сделан отдельно, т. к.  в будующем можно будет отделить планировщик от рендеринга)
        self.energy -= 0.001
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
        self.graphics_entity.setPos(QPointF(self.geo[0], self.geo[1]))
        self.graphics_entity.setRotation(math.degrees(self.u))
