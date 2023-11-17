import math
import random
import pygame
from states.SearchState import SearchState

#### ИИ + МОШКИ = DIGITAL МОШКИ
class Ant:
    def __init__(self, scene, anthill):
        self.name = __class__.__name__
        self.geo = [random.randint(10, 490), random.randint(10, 490)]  # [50,344]
        self.isready = False
        self.state = [0, 0]  # Параметр, содержащий состояние state[0] и объект, связанный с состоянием state[1]
        # state[0] = 0 - в поиске яблока, 1 - нашел яблоко, тащит в муравейник,
        # 2 - атакует паук, нужно вместе его забороть, 3 - конец игры. нужно идти с муравейнику.
        # 4 - Убегает от паука, поскольку рядом нет товарищей/не способны оказать должное
        # Сопротивление пауку
        self.charachter = random.randint(0, 1)  # Характер. 0 - трусливый, 1 - доблестный
        self.u = random.uniform(0, 4 * math.pi)  # Случайный угол по x
        self.speed = 0
        self.r = 0
        most_apple = None
        self.energy_consumption = 1/100
        if self.charachter == 0:  # Если трус, то выше скорость, но ниже радиус обзора
            self.speed = 4
            self.r = 10
        elif self.charachter == 1:  # Если доблестный, то наоборот
            self.speed = 3  # Скорость муравья
            self.r = 20  # Радиус зрения муравья
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
        # 1. друзья  2.враги 3.добыча 4.угол отклонения 5.внутри карты
        self.weights = [0.2, -0.3, 0.3, 0.2, 1]  # весовые коэфициенты многофактроной целевой функции поиска
        self.friends = ["Ant"] # друзьяшки паука(здесь и в следующих массивах это имена классов-агентов)
        self.enemies = ["Spider"] # враги пауков
        self.preys = ["Apples"]    # добыча пауков
        self.spawn = []     #обьекты для состояния спавна
        self.searchState = SearchState(self)    # создания экземпляра класса состояния поиска
        self.prey = None
        self.ant_icon = (pygame.image.load("icons/ant.png").convert_alpha(),pygame.image.load("icons/big_ant.png").convert_alpha())


    # TODO: Вычистить код, убрать дублирующие переменные и дублирующие проверки

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
    
    def add_ant(self,scene, anthill):
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
            return pygame.transform.scale(self.ant_icon[0],(12,12))
        if self.charachter == 1:
            return pygame.transform.scale(self.ant_icon[1],(20,20))
        
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
            print("Убить не получилось!")

    def self_determination(self, state, ants, spiders, apples):  # Самоопределение.
        # Самоопределение ответственно только за анализ ситуации и возвращение состояния муравья
        # Самое первое - если есть опасность, надо либо от нее убежать,
        # либо ее победить. Уже после идут всё остальное. Разумеется, это пока что, и
        # в планах разработать систему удовлетворенность и противовесов.

        if self.anthill.exit == True:  # Если конец игры, то возвращается значение,
            if spiders != []:  # если таки встретился паучара, ему не сдобровать!
                return [2, spiders[0]]
            else:
                return [3, 0]  # сзывающее в муравейник.

        if state[0] == 4:  # Если параметр равен 4, то убегать от паука(см. комментрий к переменной state)
            if len(ants) < 5 and spiders != []:  # Если окружающих мурававьев < 5 и список окружающих пауков не пуст, то
                return [4, spiders[0]]  # Возвращается значение "бегство!"
            if state[
                1] not in spiders:  # если преследующего паука больше нет в радиусе, то отменить бегство и приняться
                return [0, 0]  # искать яблоки

        if state[0] == 2:  # Если параметр равен 2, то идет проверка, а существует ли еще такой паук в радиусе
            if self.charachter == 0 and state[
                1] not in spiders:  # Разделение я думал с небольшим потенциалом, "на вырост" то есть
                return [0, 0]
            elif self.charachter == 1 and state[1] not in spiders:
                return [0, 0]

        if state[0] == 1:  # Если параметр равен 1
            if len(ants) < 5 and spiders != []:  # Есть ли вокруг пауки и меньше ли вокруг муравьев, чем 5
                return [4, spiders[0]]  # Если да, то возвращается статус бегство!
            elif len(ants) > 5 and spiders != []:  # А если больше, то муравей вызывает подмогу
                consensus = self.send_message_to_radius(0, ants, spiders[0])
                if consensus == True:
                    self.state = [2, spiders[0]]
                elif consensus == False:
                    self.state = [4, spiders[0]]


            elif apples != [] and self.prey!=None:  # Если пауков нет -> если есть яблоки
                return [1, self.prey]  # А если нет, то возвращается параметр к тасканию яблока и  яблоко
            elif apples !=[] and self.prey==None:
                system_profits = []
                for apple in apples:
                    apples_ants = []
                    new_speed = (apple.speed*apple.weight + self.speed*self.weight)/apple.weight
                    for ant in ants:
                        if (ant.get_distance(apple)<=ant.speed - apple.speed):
                            apples_ants.append(ant)
                    try:
                        my_profit = ((apple.energy/10)/(len(apples_ants)+1)) - self.get_distance(self.anthill)/new_speed*self.energy_consumption
                    except:
                        my_profit = ((apple.energy/10)/(len(apples_ants)+1)) - self.get_distance(self.anthill)/new_speed*self.energy_consumption
                    system_profit = [my_profit, apple]
                    for ant in apples_ants:
                        profit = self.profit(apples_ants, apple)
                        system_profit[0]+=profit
                    if system_profit[0]>0: system_profits.append(system_profit)
                if system_profits!=[]:
                    most_apple = max(system_profits, key=lambda x: x[0])[1]
                    print(len(apples_ants))
                    return [1, most_apple]  # А если нет, то возвращается параметр к тасканию яблока и  яблоко
                    
            else:
                return [0, 0]  # если ничего из этого не прошло, то просто поиск яблока


        if state[0] == 0:  # Если состояние - простой поиск яблока
            if len(ants) < 5 and spiders != []:  # Если нет муравьев  и есть пауки - бегство
                return [4, spiders[0]]
            elif len(ants) > 5 and spiders != []:  # Если муравьев много - призыв к бойне!
                consensus = self.send_message_to_radius(0, ants, spiders[0])
                if consensus == True:
                    self.state = [2, spiders[0]]
                elif consensus == False:
                    self.state = [4, spiders[0]]
            elif apples != []:  # ну авось если яблочки есть, то извольте-с его тащить
                if self.get_distance(apples[0]) <= 5: return [1, apples[0]]
        return state

    def live_by_self_determination(self, geo, state, ants, spiders, apples):  # Жить по самоопределению
        if state[0] == 0:
            if spiders != []:
                consensus = self.send_message_to_radius(0, ants, spiders[0])
                if consensus == True:
                    self.state = [2, spiders[0]]
                elif consensus == False:
                    self.state = [4, spiders[0]]
            #Если вокруг есть яблоки и нет уже заданной жертвы
            elif apples != [] and self.prey == None:
                system_profits = []
                for apple in apples:
                    apples_ants = []
                    new_speed = (apple.speed*apple.weight + self.speed*self.weight)/apple.weight
                    for ant in ants:
                        if (ant.get_distance(apple)<=ant.speed - apple.speed):
                            apples_ants.append(ant)
                    try:
                        my_profit = ((apple.energy/10)/(len(apples_ants)+1)) - self.get_distance(self.anthill)/new_speed*self.energy_consumption
                    except:
                        my_profit = ((apple.energy/10)/(len(apples_ants)+1)) - self.get_distance(self.anthill)/new_speed*self.energy_consumption
                    system_profit = [my_profit, apple]
                    for ant in apples_ants:
                        profit = self.profit(apples_ants, apple)
                        system_profit[0]+=profit
                    if system_profit[0]>0: system_profits.append(system_profit)
                if system_profits!=[]:
                    most_apple = max(system_profits, key=lambda x: x[0])[1]
                    print(len(apples_ants))
                    try:
                        self.u_trig = [(most_apple.geo[1] - geo[1]) / self.get_distance(most_apple), (most_apple.geo[0] - geo[0]) / self.get_distance(most_apple)]
                        self.u = math.acos((most_apple.geo[0] - geo[0]) / self.get_distance(most_apple))
                    except:
                        pass
                #Если жертва уже была выбрана
                elif self.prey!=None:
                    try:
                        self.u_trig = [(self.prey.geo[1] - geo[1]) / self.get_distance(self.prey), (self.prey.geo[0] - geo[0]) / self.get_distance(self.prey)]
                        self.u = math.acos((self.prey.geo[0] - geo[0]) / self.get_distance(self.prey))
                    except:
                        pass
                else: 
                    self.u = self.searchState.move(self)
                    self.u_trig = [math.sin(self.u), math.cos(self.u)]
            else:
                self.u = self.searchState.move(self)
                self.u_trig = [math.sin(self.u), math.cos(self.u)]
        #Если яблоко уже было выбрано 
        elif state[0] == 1:
            if self.prey!=None:
                if state[1]!=self.prey: 
                    state[1]=self.prey
                    if spiders != [] and ants != 0:
                        consensus = self.send_message_to_radius(0, ants, spiders[0])
                        if consensus == True:
                            self.state = [2, spiders[0]]
                        elif consensus == False:
                            self.state = [4, spiders[0]]
                    elif state[1] in self.anthill.get_apples(self.anthill.scene):
                        try:
                            state[1].geo = geo
                            state[1].travelset.add(self)
                            self.u = math.acos((self.anthill.geo[0] - geo[0]) / self.get_distance(self.anthill))
                            self.usin = math.asin((self.anthill.geo[1] - geo[1]) / self.get_distance(self.anthill))
                            self.u_trig[0] = (self.anthill.geo[1] - geo[1]) / self.get_distance(self.anthill)
                            self.u_trig[1] = (self.anthill.geo[0] - geo[0]) / self.get_distance(self.anthill)
                        except:
                            f = 1
                        self.scene = state[1].move(self.scene)
                    elif self in state[1].travelset and state[1] not in apples:
                        state[1].travelset.remove(self)
            elif(self.state[1]!=None and self.prey==None):
                if spiders != [] and ants != 0:
                    consensus = self.send_message_to_radius(0, ants, spiders[0])
                    if consensus == True:
                        self.state = [2, spiders[0]]
                    elif consensus == False:
                        self.state = [4, spiders[0]]
                elif state[1] in self.anthill.get_apples(self.anthill.scene):
                    try:
                        state[1].geo = geo
                        state[1].travelset.add(self)
                        self.u = math.acos((self.anthill.geo[0] - geo[0]) / self.get_distance(self.anthill))
                        self.usin = math.asin((self.anthill.geo[1] - geo[1]) / self.get_distance(self.anthill))
                        self.u_trig[0] = (self.anthill.geo[1] - geo[1]) / self.get_distance(self.anthill)
                        self.u_trig[1] = (self.anthill.geo[0] - geo[0]) / self.get_distance(self.anthill)
                    except:
                        f = 1
                    self.scene = state[1].move(self.scene)
                elif self in state[1].travelset and state[1] not in apples:
                    state[1].travelset.remove(self)

            
        elif state[0] == 2:
            self.u_trig = [(state[1].geo[1] - geo[1]) / self.get_distance(state[1]), (state[1].geo[0] - geo[0]) / self.get_distance(state[1])]
            self.u = math.acos((state[1].geo[0] - geo[0]) / self.get_distance(state[1]))
        elif state[0] == 3:
            self.u_trig = [(self.anthill.geo[1] - geo[1]) / self.get_distance(self.anthill), (self.anthill.geo[0] - geo[0]) / self.get_distance(self.anthill)]
            self.u = math.acos((self.anthill.geo[0] - geo[0]) / self.get_distance(self.anthill))
            if self.get_distance(self.anthill) <= 4: self.die(self)
        elif state[0] == 4:
            self.u_trig = [(self.anthill.geo[1] - geo[1]) / self.get_distance(self.anthill), (self.anthill.geo[0] - geo[0]) / self.get_distance(self.anthill)]
            self.u = math.pi - math.acos((self.anthill.geo[0] - geo[0]) / self.get_distance(self.anthill))

    def move(self, scene):
        full_scene = scene
        self.scene = self.get_scene(scene)
        self.apples = self.get_apples(self.scene)
        self.ants = self.get_ants(self.scene)
        self.spiders = self.get_spiders(self.scene)
        for agent in self.scene:
            full_scene.remove(agent)  # получение данных из сцены и запись, только данных в области обзора паука

        if self.spiders != []:
            sorted(self.spiders,
                   key=lambda x: self.get_distance(x))  # Отсортированный по расстоянию к self список пауков
        if self.apples != []:
            sorted(self.apples, key=lambda x: self.get_distance(x))  # Отсортированный по расстоянию к self список яблок
            if self.apples[0] != self.get_nearest(self.apples):
                self.apples.append(self.apples[0])
                self.apples[0] = self.get_nearest(self.apples)
        

        self.state = self.self_determination(self.state, self.ants, self.spiders, self.apples)

        self.live_by_self_determination(self.geo, self.state, self.ants, self.spiders, self.apples)

        self.energy -= 0.001
        if self.energy <=0:
            self.die(self)


        for agent in self.scene:
            full_scene.add(
                agent)  # после окончания хода, паук передает в сцену изменившиеся данные и возвращает ее диспетчеру вместе с ходом(простите, без элементарного диспетчера не получался нормальный паук)
        return full_scene

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
        their_profit = (agent_resource.energy/10)/len(ants) - self.get_distance(self.anthill)/speed*self.energy_consumption #Если они толкают без меня!!! 
        
        new_speed = (agent_resource.speed*agent_resource.weight + self.speed*self.weight)/agent_resource.weight
        our_profit = (agent_resource.energy/10)/(len(ants)+1) - self.get_distance(self.anthill)/new_speed*self.energy_consumption #Если они толкали со мной
        return our_profit - their_profit
    

    def get_scene(self, scene):  # возвращает обьекты из сцены, в радиусе обзора паука
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

    def run(self):  # метод, который перемещает муравья в нужном направлении, после рассчета хода(сделан отдельно, т. к.  в будующем можно будет отделить планировщик от рендеринга)
        self.geo[0] += self.speed * self.u_trig[1]
        self.geo[1] += self.speed * self.u_trig[0]
