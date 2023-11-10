import random
import pygame
import math
from states.InertiaState import InertiaState


class Apple:
    def __init__(self, anthill):
        self.name = __class__.__name__
        self.geo = [random.randint(10, 970), random.randint(10, 970)]
        self.apl_font = pygame.font.Font(pygame.font.match_font('verdana'), 15)
        self.travelset = set()
        self.scene = None
        self.apples = None
        self.anthill = anthill
        self.ants = None
        self.spiders = None
        self.energy = 1
        self.distance = ((self.anthill.geo[0] - self.geo[0]) ** 2 + (self.anthill.geo[1] - self.geo[1]) ** 2) ** 0.5
        self.weight = 3
        self.speed = 0
        self.inertiaState = InertiaState(self)

    def body(self):
        s = random.randint(28, 30)
        return pygame.Rect(self.geo[0], self.geo[1], s, s)

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

    def die(self, apple):
        self.apples.remove(apple)
        self.scene.remove(apple)
        self.anthill.get_food_apple(apple)


    def find_travel_speed(self):
        quantity_ants = len(self.travelset)
        normal_speed = 3
        normal_weight = self.weight / self.ants[0].power
        floor1 = [self.distance, normal_speed]
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
    
    def get_distance(self, obj):  # возвращает информацию о расстоянии до обьекта при помощи любимой теоремы Пифагора
        return math.sqrt((self.geo[0] - obj.geo[0]) ** 2 + (self.geo[1] - obj.geo[1]) ** 2)

    def move(self, scene):
        self.scene = scene
        self.apples = self.get_apples(self.scene)  # диспетчер переопределяет сцену
        self.ants = self.get_ants(self.scene)
        self.spiders = self.get_spiders(self.scene)
        self.anthill = self.get_anthill(self.scene)

        scene = self.inertiaState.move(self)

        distance = ((self.anthill.geo[0] - self.geo[0]) ** 2 + (self.anthill.geo[1] - self.geo[1]) ** 2) ** 0.5
        if distance <= 15:
            self.die(self)
        return self.scene
    
    def run(self):
        self.geo[0] += self.speed * self.u_trig[1]
        self.geo[1] += self.speed * self.u_trig[0]

