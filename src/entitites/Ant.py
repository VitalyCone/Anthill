import math
import random
import pygame
import logging
from src.states.SearchState import SearchState

#### ИИ + МОШКИ = DIGITAL МОШКИ
class Ant:
    def __init__(self, scene, anthill, id='0'):
        self.name = __class__.__name__
        self.uri = self.name + str(id)
        self.geo = [random.randint(10, 490), random.randint(10, 490)]  # [50,344]
        self.isready = False
        self.agent = None
        self.state = [0, 0]  # Параметр, содержащий состояние state[0] и объект, связанный с состоянием state[1]
        # state[0] = 0 - в поиске яблока, 1 - нашел яблоко, тащит в муравейник,
        # 2 - атакует паук, нужно вместе его забороть, 3 - конец игры. нужно идти с муравейнику.
        # 4 - Убегает от паука, поскольку рядом нет товарищей/не способны оказать должное
        # Сопротивление пауку
        self.charachter = random.randint(0, 1)  # Характер. 0 - трусливый, 1 - доблестный
        self.u = random.uniform(0, 4 * math.pi)  # Случайный угол по x
        self.speed = 6
        self.r = 70
        most_apple = None
        self.energy_consumption = 1/100
        if self.charachter == 0:  # Если трус, то выше скорость, но ниже радиус обзора
            self.speed = 4
            self.r = 50
        elif self.charachter == 1:  # Если доблестный, то наоборот
            self.speed = 3  # Скорость муравья
            self.r = 70  # Радиус зрения муравья
        self.intravel = False
        self.power = 1500
        self.energy = random.uniform(0.01, 1)
        self.scene = scene  # Сцена
        self.apples = self.get_apples(self.scene)  # Вообще все яблоки
        self.anthill = anthill  # Муравейник
        self.ants = self.get_ants(self.scene)  # Вообще все муравьи
        self.spiders = self.get_spiders(self.scene)  # Вообще все пауки
        self.weight = 0.2
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
        self.ant_icon = (pygame.image.load("assets/icons/ant.png").convert_alpha(),
                         pygame.image.load("assets/icons/big_ant.png").convert_alpha())
        logging.info(f'Объект {self.uri} был успешно инициализирован')

    def live(self, scene):
        """
        Обработка запроса на ход муравья
        :param scene:
        :return killed:
        """
        killed = self.move(scene)
        logging.info(f'Объект {self.uri} сделал ход, изменений в сцене: {len(killed)}')
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
            return pygame.transform.scale(self.ant_icon[0], (12, 12))
        if self.charachter == 1:
            return pygame.transform.scale(self.ant_icon[1], (20, 20))
        
    def get_nearest(self, agents):
        nearest_agent = agents[0]
        for agent in agents:
            if self.get_distance(agent) < self.get_distance(nearest_agent):
                nearest_agent = agent
        return agent

    def die(self, ant):  # Смерть
        try:  # Через try/except, потому что иногда выскакивают ошибки
            self.ants.remove(ant)
            self.scene.remove(ant)
        except:
            pass
        logging.info(f'{self} умер')

    def move(self, scene):
        killed = []
        self.scene = scene
        self.apples = self.get_apples(self.scene)
        self.ants = self.get_ants(self.scene)
        self.spiders = self.get_spiders(self.scene)
        # получение данных из сцены и запись, только данных в области обзора паука

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
            if self.apples:
                self.prey = self.apples[0]
        else:
            if self.prey:
                if self.get_distance(self.prey) >= self.speed - self.prey.speed:
                    self.u_trig = [(self.prey.geo[1] - self.geo[1]) / self.get_distance(self.prey),
                                   (self.prey.geo[0] - self.geo[0]) / self.get_distance(self.prey)]
                else:
                    self.u_trig = [(self.anthill.geo[1] - self.geo[1]) / self.get_distance(self.anthill),
                                   (self.anthill.geo[0] - self.geo[0]) / self.get_distance(self.anthill)]

        self.energy -= 0.001
        if self.energy <= 0:
            self.die(self)
            killed.append(self.get_uri())

        return killed

    def get_distance(self, obj):  # возвращает информацию о расстоянии до обьекта при помощи любимой теоремы Пифагора
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
        self.geo[0] += self.speed * self.u_trig[1]
        self.geo[1] += self.speed * self.u_trig[0]
