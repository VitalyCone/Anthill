import random
import pygame

class Apple:
    def __init__(self, anthill):
        self.name = __class__.__name__
        self.geo = [random.randint(10,970),random.randint(10,970)]
        self.apl_font = pygame.font.Font(pygame.font.match_font('verdana'), 15)
        self.travelset = set()
        self.weight = 15000
        self.scene = None
        self.apples = None
        self.anthill = anthill
        self.ants = None
        self.spiders = None
        self.distance = ((self.anthill.geo[0]-self.geo[0])**2 + (self.anthill.geo[1]-self.geo[1])**2)**0.5
    
    def body(self):
        return pygame.Rect(self.geo[0],self.geo[1],30,30)
    
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

    def die(self,apple):
        self.apples.remove(apple)
    
    def find_travel_speed(self):
        quantity_ants = len(self.travelset)
        normal_speed = 3
        normal_weight = self.weight/self.ants[0].power
        floor1 = [self.distance,normal_speed]
        speed = normal_speed * quantity_ants / normal_weight
        return speed
    def get_anthill(self, scene):
        for anthill in scene:
            if anthill.name == 'Anthill':
                return anthill
        return self.anthill

    def get_spiders(self, scene):
        spiders = []
        for spider in scene:
            if spider.name == 'Spider':
                spiders.append(spider)
        return spiders

    def move(self, scene):
        self.scene = scene
        self.apples = self.get_apples(self.scene)  #диспетчер переопределяет сцену
        self.ants = self.get_ants(self.scene)
        self.spiders = self.get_spiders(self.scene)
        self.anthill = self.get_anthill(self.scene)

        distance = ((self.anthill.geo[0]-self.geo[0])**2 + (self.anthill.geo[1]-self.geo[1])**2)**0.5
        speed = self.find_travel_speed()

        try:
            vector = ((self.anthill.geo[0]-self.geo[0])/distance,(self.anthill.geo[1]-self.geo[1])/distance)
        except:
            vector = (0,0)
        
        if distance <= 5:
            self.apples.remove(self)

        self.geo[0]+=vector[0]*speed
        self.geo[1]+=vector[1]*speed
        return self.apples + self.ants + self.spiders + [self.anthill]
