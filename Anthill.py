import pygame
from states.SpawnState import SpawnState
from states.GrowthState import GrowthState

class Anthill:
    def __init__(self,input_apple_hp, input_ant, del_ants):
        self.input_apple_hp = input_apple_hp
        self.input_ant = input_ant
        self.ants = del_ants
        self.name = __class__.__name__
        self.energy = 50
        self.last_energy = self.energy
        self.energy_consumption = 0.01
        self.x = 100
        self.y = 800
        self.height = 50
        self.long = 50
        self.livelihood = 1000 #запасы пропитания
        self.anth_font = pygame.font.Font(pygame.font.match_font('verdana'), size = 30)
        self.exit = False
        self.geo = [self.x,self.y]
        self.scene = None
        self.ants = []
        self.anthills = []
        self.spiders = []
        self.food_apple = 0
        self.s = 0
        self.del_livelihood = 200
        self.pot_ant = 5
        self.pot_ants = len(self.ants)*self.pot_ant
        self.tic = 0
        self.spawnState = SpawnState(self)
        self.growthState = GrowthState(self)
        
    def body(self):
        return pygame.Rect(self.geo[0],self.geo[1], self.height,self.long)
       
    
    def get_apples(self, scene):
        apples = []
        for apple in scene:
            if apple.name == 'Apple':
                apples.append(apple)
        return apples
    
    def get_ants(self, scene,):  #метод, возвращающий всех муравьев в зоне обзора
        ants = []

        for ant in scene:
            if ant.name == 'Ant':
                ants.append(ant)
        return ants

    def get_spiders(self, scene):  #метод, возвращающий всех пауков в зоне обзора
        spiders = []
        for spider in scene:
            if spider.name == 'Spider':
                spiders.append(spider)
        return spiders
    
    def get_anthills(self, scene):
        anthills = []
        for anthill in scene:
            if anthill.name == 'Anthill':
                anthills.append(anthill)
        return anthills
    
    def get_food_apple(self, apple):
        self.energy += apple.energy
        self.food_apple += 1

    def run(self):
        self.energy -= self.energy_consumption


    
    def move(self, scene):
        print('xxxxxxxxxxxxxxx') #
        full_scene = scene
        self.scene = scene
        self.anthills = self.get_anthills(scene)
        self.ants = self.get_ants(scene)
        self.apples = self.get_apples(scene)
        
        
        scene = self.spawnState.move(self)

        scene = self.growthState.move(self)

        self.tic += 1


        return scene