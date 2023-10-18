import random
import pygame

class Ant:
    def __init__(self, scene, anthill):
        self.name = __class__.__name__
        self.geo = [random.randint(10,990),random.randint(10,990)]  #[50,344]
        self.isready = False
        self.speed = 3
        self.intravel = False
        self.power = 1500
        self.energy = 1
        self.scene = scene
        self.apples = self.get_apples(self.scene)
        self.anthill = anthill
        self.ants = self.get_ants(self.scene)
        self.spiders = self.get_spiders(self.scene)

    def get_spiders(self, scene):
        spiders = []
        for spider in scene:
            if spider.name == 'Spider':
                spiders.append(spider)
        return spiders
 
    def get_ants(self, scene):
        ants = []
        for ant in scene:
            if ant.name == 'Ant':
                ants.append(ant)
        return ants
    
    def get_apples(self, scene):
        apples = []
        for apple in scene:
            if apple.name == 'Apple':
                apples.append(apple)
        return apples
    def get_anthill(self, scene):
        anthill_1 = None
        for anthill in scene:
            if anthill.name == 'Anthill':
                anthill_1 = anthill
        return anthill_1
    
    def body(self):
        return pygame.Rect(self.geo[0],self.geo[1],5,5)
    
    def die(self,ant):
        self.ants.remove(ant)
        self.scene.remove(ant)

    def closest_apple(self):
        dl = sorted([[((abs(round(apl.geo[0]-self.geo[0])**2 + (apl.geo[1]-self.geo[1])**2)**0.5)),apl] for apl in self.apples],key=lambda x: x[0])
        if dl:
            return dl[0][1]

    def move(self, scene):
        self.scene = scene
        self.apples = self.get_apples(self.scene)
        self.ants = self.get_ants(self.scene)
        self.spiders = self.get_spiders(self.scene)

        
        run = self.run_away_from_spiders()

        if run:
            my_apple = run[1]
        elif not self.anthill.exit:
            my_apple = self.closest_apple()
        else:
            my_apple = self.anthill

        if my_apple:
            distance = ((my_apple.geo[0]-self.geo[0])**2 + (my_apple.geo[1]-self.geo[1])**2)**0.5
            
            if distance <= 5:
                if my_apple.name == 'Apple':
                    self.intravel = True
                    my_apple.travelset.add(self)
                    self.scene = my_apple.move(self.scene)
                    for apple in self.apples:
                        if apple!=my_apple and self in apple.travelset:
                            apple.travelset.remove(self)

                if my_apple.name == 'Anthill':
                    self.isready = True
            try:
                vector = ((my_apple.geo[0]-self.geo[0])/distance,(my_apple.geo[1]-self.geo[1])/distance)
            except:
                vector = (0,0)

            if not run:
                self.geo[0]+=vector[0]*self.speed
                self.geo[1]+=vector[1]*self.speed

            else:
                self.geo[0]-=vector[0]*self.speed
                self.geo[1]-=vector[1]*self.speed
        return self.scene

    def run_away_from_spiders(self):
        distance = [[((spider.geo[0]-self.geo[0])**2 + (spider.geo[1]-self.geo[1])**2)**0.5,spider] for spider in self.spiders]
        for el in distance:
            if el[0] < 70:
                if not self.isready:
                    return el
        return False
        
    
    def closest_ant(self):
        dl = sorted([[((abs(round(ant.geo[0]-self.geo[0])**2 + (ant.geo[1]-self.geo[1])**2)**0.5)),ant] for ant in self.ants if not ant.isready],key=lambda x: x[0])
        spiders_goals = [spider.my_ant for spider in self.spiders]
        if dl:
            if len(dl) >= len(self.spiders):
                for el in dl:
                    if el[1] not in spiders_goals:
                        if 0<el[1].geo[0]<1000 and 0<el[1].geo[1]<1000:
                            return el[1]
                    elif el[1] == self.my_ant:
                        return self.my_ant
            else:
                return dl[0][1]

