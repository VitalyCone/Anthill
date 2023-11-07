from sys import displayhook
import pygame


class Anthill:
    def __init__(self,input_apple_hp, input_ant, del_ants):
        self.input_apple_hp = input_apple_hp
        self.input_ant = input_ant
        self.ants = del_ants
        self.name = __class__.__name__
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
        self.del_livelihood = 0
        self.pot_ant = 5
        self.pot_ants = len(self.ants)*self.pot_ant
        
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
    
    def get_food_apple(self):
        self.food_apple += 1
        return self.food_apple
    
    def move(self, scene):
        print('xxxxxxxxxxxxxxx') #
        full_scene = scene
        self.scene = scene
        self.anthills = self.get_anthills(scene)
        self.ants = self.get_ants(scene)
        self.apples = self.get_apples(scene)
        if self.height > 1:
            self.height -= 1
        if self.long > 1:
            self.long -= 1
        
        
        print(self.del_livelihood,'22')


        if self.food_apple >= self.s:
            self.s += 1
            print(self.s)
            self.livelihood += self.input_apple_hp
            self.del_livelihood = self.livelihood - self.del_livelihood
            

            if (self.livelihood > self.pot_ants):

                if ((self.livelihood - self.pot_ants) // 10) > 0:
                    k = 0
                    print(len(self.ants),'/////////////')
                    for i in range((self.livelihood - self.pot_ants) // 10):
                        k += 1
                        ANT = self.ants[0].add_ant(scene, self.anthills[0])
                        self.ants.append(ANT)
                        print(len(self.ants), '!!!!!!!!!!!!')
                        print(k,'67')
                        if k > ((self.livelihood - self.pot_ants) // 10):
                            break       
                if self.del_livelihood != 0:
                    self.height += self.del_livelihood//40
                    self.long += self.del_livelihood//40

        return scene