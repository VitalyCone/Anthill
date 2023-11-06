import random
import math
import pygame


class Spider:
    def __init__(self, scene):
        self.name = __class__.__name__  # в каждом классе определил переменную-имя класса, чтобы агентам не надо было импортровать друг друга, чтобы не появлялась circular import error
        self.geo = [random.randint(10, 990), random.randint(10, 990)]
        self.speed = 6
        self.u = math.pi * 3 / 2  # угол направления паука-вектора
        self.gamma = math.pi / 6  # угол в радиусе которого допускается отклонение
        self.r = 50  # радиус обзора муравья
        self.energy = 1  # энергия муравья/паука, пока что у всех она -- 1
        self.scene = self.get_scene(scene)  # метод, который получает данные о всех обЪектах в области обзора паука
        self.chasing = False  # булевое значение, которое контролирует переход между состояниями(изначально - паук не преследует никакого муравья)
        self.my_ant = None
        # рядом паук-конкурент   #рядом много муравьев   #угол поворота близок к исходному
        self.array_of_key = [-0.2, 0.3, 0.2,
                             0.6]  # коэфициенты потребностей(переписать их, чтобы сумма была равна единице)

    def body(self):
        s = random.randint(14, 20)
        return pygame.Rect(self.geo[0], self.geo[1], s, s)

    def get_num_of_spiders_around(self,
                                  geo):  # метод, который обрабатывает сцену, и ищет в ней количество пауков, в радиусе от заданных координат
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

    def get_need(self, u):
        chasing = False
        geo = [self.geo[0] + self.speed * math.cos(u), self.geo[1] + self.speed * math.sin(u)]
        sum_of_needs = 0
        num_of_spiders = self.get_num_of_spiders_around(geo)  # получает количество пауков из сцены, в радиусе обзора
        num_of_ants = self.get_num_of_ants_around(geo)  # получает количество муравьев из сцены, в радиусе обзора паука
        needs = []  # энергия входит в функцию расчета удовлетворенности
        if num_of_spiders != 0:
            needs.append(
                1)  # рассчет коэфициента для выбора направления из количество пауков. Есть другие пауки - 0, нет - 1
        else:
            needs.append(0)
        if num_of_ants > 5:
            needs.append(1)  # если рядом много муравьев(сейчас больше 5), то паук доволен
        else:
            needs.append(0)
        if (abs(self.u - u) <= self.gamma):
            needs.append(1)
        else:  # если угол предлагаемого поворота входит в допустимое отклонение угла от направления вектора, паук доволен(если пауку меньше надо поворачиваться, он доволен)
            needs.append(0)
        if (geo[0] < 0 or geo[0] > 995) or (geo[1] < 0 or geo[1] > 995):
            needs.append(0)  # если паук в результате перемещения не выходит за границы карты, он доволен
        else:
            needs.append(1)
        for i in range(0, len(self.array_of_key)):
            sum_of_needs += needs[i] * self.array_of_key[
                i]  # рассчет удовлетворенности паука, учитывая весовые коэфициенты каждого параметра.
        return [sum_of_needs, chasing, u]

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

    def move(self, scene):  # метод для рассчета действий для хода муравья
        full_scene = scene
        self.scene = self.get_scene(scene)
        for agent in self.scene:
            full_scene.remove(agent)  # получение данных из сцены и запись, только данных в области обзора паука
        ants = self.get_ants(self.scene)  # все муравьи в радиусе обзора паука

        #############

        fighters = []
        for ant in ants:
            if ant.state == [2, self] and self.get_distance(ant) <= 20:
                fighters.append(ant)
        if len(fighters) != 0:
            if len(fighters) <= 2:
                for i in range(0, len(fighters) - len(fighters) // 6):
                    a = random.choice(fighters)
                    a.die(a)
            elif 3 <= len(fighters) <= 5:
                for i in range(0, len(fighters) - len(fighters) // 4):
                    a = random.choice(fighters)
                    a.die(a)

                print(self.name, "умер!")
                self.die()
            elif 6 <= len(fighters):
                for i in range(0, len(fighters) - len(fighters) // 2):
                    a = random.choice(fighters)
                    a.die(a)
                print(self.name, "умер!")
                self.die()

        #############
        if len(ants) == 0:  # если вокруг паука нет муравьев, то он продолжает находиться в состоянии поиска
            self.chasing = False
            self.my_ant = None
            best_moves = []
            best_move = self.get_need(0)
            best_moves.append(best_move)
            a = 0
            while a < math.pi * 2:  # вычисляем лучшие углы поворота, при помощи метода get_need()
                a += 0.01
                move1 = self.get_need(a)
                if move1[0] > best_move[0]:
                    best_move = move1
                    best_moves.clear()
                    best_moves.append(move1)
                elif move1[0] == best_move[0]:
                    best_moves.append(move1)
            choice = random.choice(
                best_moves)  # если лучших ходов несколько, то выбираем случайный(чем больше параметров, тем меньше вероятность выбора случайного направления)
            self.u = choice[2]
            self.chasing = choice[1]
        else:  # если же вокруг паука есть муравьи - он начинает охоту
            self.chasing = True
            best_ant = ants[0]
            for ant in ants:  # каждый ход охоты идет проверка, точно ли выбранный муравей - лучший.
                if self.get_energy(ant) > self.get_energy(
                        best_ant):  # если полученная энергия больше полученной энергии при охоте за лучшим муравьем, тогда назначается новый лучший муравей
                    best_ant = ant
            self.my_ant = best_ant
            distance = self.get_distance(self.my_ant)
            self.u = math.acos((self.my_ant.geo[0] - self.geo[
                0]) / distance)  # назначается угол-направление в сторону лучшего муравья.
            for spider in self.get_spiders(self.scene):
                if self.my_ant != None and spider.my_ant != None:
                    if spider.my_ant == self.my_ant:
                        if spider.get_energy(self.my_ant) > self.get_energy(self.my_ant):
                            self.my_ant = None  # нечто вроде прототипа ПВ-сетей между пауками, при выборе муравья,если они выбрали одну цель, то они вступают в что-то вроде конфликта,
                            self.chasing = False  # решая, чей профит будет выше => выше прибыль системы. Этот кусочек еще не тестировал, но его надо развивать.

            try:
                if distance < (
                        self.speed + self.my_ant.speed) and self.my_ant != None:  # если же муравей оказался на дистанции меньшей, чем минимальное перемещение за ход, тогда муравей умирает
                    self.my_ant.die(self.my_ant)
                    self.scene.remove(self.my_ant)
                    self.my_ant = None
                    self.chasing = False  # муравей погибает и паук снова переходит в стадию поиска
            except:
                print("ашипка")
        for agent in self.scene:
            full_scene.append(
                agent)  # после окончания хода, паук передает в сцену изменившиеся данные и возвращает ее диспетчеру вместе с ходом(простите, без элементарного диспетчера не получался нормальный паук)
        return full_scene

    def get_energy(self, obj):  # возвращает энергию, полученную пауком.
        return self.energy + obj.energy - self.get_distance(obj) / (self.speed - obj.speed) * 0.01

    def get_distance(self, obj):  # возвращает информацию о расстоянии до обьекта при помощи любимой теоремы Пифагора
        return math.sqrt((self.geo[0] - obj.geo[0]) ** 2 + (self.geo[1] - obj.geo[1]) ** 2)

    def get_scene(self, scene):  # возвращает обьекты из сцены, в радиусе обзора паука
        scene1 = []
        for obj in scene:
            if (abs(obj.geo[0] - self.geo[0]) <= self.r) and (abs(obj.geo[1] - self.geo[1]) <= self.r):
                scene1.append(obj)
        return scene1

    def die(self):
        try:
            self.scene.remove(self)
        except:
            f = 1

    def run(self):  # метод, который перемещает муравья в нужном направлении, после рассчета хода(сделан отдельно, т. к.  в будующем можно будет отделить планировщик от рендеринга)
        self.geo[0] += self.speed * math.cos(self.u)
        self.geo[1] += self.speed * math.sin(self.u)
