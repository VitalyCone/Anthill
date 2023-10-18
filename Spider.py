import random
import math
import pygame

class Spider:
    def __init__(self, scene):
        self.name = __class__.__name__
        self.geo = [random.randint(10,990),random.randint(10,990)]
        print(self.geo)
        self.speed = 7
        self.u = math.pi*3/2 #угол направления паука-вектора
        self.gamma = math.pi/6 
        self.r = 50 #ПОЛОВИНА радиуса обзора муравья!!!!!!
        self.energy = 1 #сцена(на данный момент - массив из всех муравьев и пауков)
        self.scene = self.get_scene(scene)
        self.chasing = False
        self.my_ant = None
                             #рядом паук-конкурент   #рядом много муравьев   #угол поворота близок к исходному
        self.array_of_key = [-0.2,                   0.3,                 0.2,  0.6] #коэфициенты потребностей(их сумма всегда равна 1)


    def body(self):
        return pygame.Rect(self.geo[0],self.geo[1],15,15)
    
    def get_num_of_spiders_around(self, geo):
        num_of_spiders = 0
        for spider in self.scene:
            if spider.name == Spider:
                if spider.geo == self.geo:
                    continue
                else:
                    num_of_spiders += 1
        return num_of_spiders

    def get_num_of_ants_around(self, geo):
        num_of_ants = 0
        for ant in self.scene:
            if ant.name == 'Ant':
                num_of_ants += 1
        return num_of_ants
    
    def get_all_spiders(self):
        num = 0
        for spider in self.scene:
            if spider.name == 'Spider':
                num += 1
        return num

    def get_need(self, u):
        chasing = False
        geo = [self.geo[0]+self.speed*math.cos(u), self.geo[1]+self.speed*math.sin(u)]
        sum_of_needs = 0
        num_of_spiders = self.get_num_of_spiders_around(geo) #получает количество пауков в радиусе обзора
        num_of_ants = self.get_num_of_ants_around(geo) #получает количество муравьев в радиусе обзора
        needs = [] #энергия входит в функцию расчета удовлетворенности
        if num_of_spiders != 0:
            needs.append(1) #вводится процент от общего количества пауков рядом (паук недоволен если рядом много конкурентов)
        else:
            needs.append(0)
        if num_of_ants > 5:
            needs.append(1) #если рядом много муравьев(сейчас больше 15), то паук доволен
        else: 
            needs.append(0)
        if(abs(self.u - u) <= self.gamma):
            needs.append(1)
        else:               #если угол предлагаемого поворота входит в допустимое отклонение угла от направления вектора, паук доволен(если пауку меньше надо поворачиваться, он доволен)
            needs.append(0)
        if (geo[0] < 0 or geo[0] > 995) or (geo[1] < 0 or geo[1] > 995):
            needs.append(0)
        else:
            needs.append(1)
        for i in range(0, len(self.array_of_key)):
            sum_of_needs += needs[i]*self.array_of_key[i]
        return [sum_of_needs, chasing, u]

    def get_ants(self, scene):
        ants = []
        for ant in scene:
            if ant.name == 'Ant':
                ants.append(ant)
        return ants

    def move(self, scene):
        full_scene = scene
        self.scene = self.get_scene(scene)
        for agent in self.scene:
            full_scene.remove(agent)
        ants = self.get_ants(self.scene)
        if len(ants) == 0:
                self.chasing = False
                self.my_ant = None
                best_moves = []
                best_move = self.get_need(0)
                best_moves.append(best_move)
                a = 0
                while a < math.pi*2: #вычисляем лучшие углы поворота
                    a += 0.01
                    move1 = self.get_need(a)
                    if move1[0] > best_move[0]:
                        best_move = move1
                        best_moves.clear()
                        best_moves.append(move1)
                    elif move1[0] == best_move[0]:
                        best_moves.append(move1)
                choice = random.choice(best_moves)
                self.u = choice[2]  #используем случайный из лучших(чем больше факторов, тем меньше одинаково хороших ходов)
                self.chasing = choice[1] 
        else:
                self.chasing = True
                best_ant = ants[0]
                for ant in ants:
                    if self.get_energy(ant) > self.get_energy(best_ant):
                        best_ant = ant
                self.my_ant = best_ant
                if self.get_distance(self.my_ant) < self.speed+self.my_ant.speed:
                    self.my_ant.die(self.my_ant)
                    self.scene.remove(self.my_ant)
                    self.my_ant = None
                    self.chasing = False
        for agent in self.scene:
            full_scene.append(agent)
        return full_scene

    def get_energy(self,obj):
        return self.energy + obj.energy - self.get_distance(obj)/(self.speed-obj.speed)*0.01
    def get_distance(self, obj):
        return math.sqrt((self.geo[0]-obj.geo[0])**2 + (self.geo[1] - obj.geo[1])**2)
                
    def get_scene(self, scene):
        scene1 =[]
        for obj in scene:
            if (abs(obj.geo[0] - self.geo[0]) <= self.r) and (abs(obj.geo[1] - self.geo[1]) <= self.r):
                scene1.append(obj)
        return scene1
    def die(self):
        if self.energy < 0:
            print("tut chto-to budet")

    def run(self):
        if not(self.chasing):
            self.geo[0] += self.speed*math.cos(self.u)
            self.geo[1] += self.speed*math.sin(self.u)
        else:
            distance = math.sqrt((self.geo[0]-self.my_ant.geo[0])**2 + (self.geo[1] - self.my_ant.geo[1])**2)
            if distance > self.speed+self.my_ant.speed:
                self.u = math.acos((self.my_ant.geo[0]-self.geo[0])/distance)
                vector = ((self.my_ant.geo[0]-self.geo[0])/distance,(self.my_ant.geo[1]-self.geo[1])/distance)
                self.geo[0]+=vector[0]*self.speed
                self.geo[1]+=vector[1]*self.speed
            else:
                self.my_ant.die(self.my_ant)
                self.scene.remove(self.my_ant)
                self.my_ant = None
                self.chasing = False