import logging

from sys import displayhook
from typing import *
import pygame
import math
from states.SpawnState import SpawnState
from states.GrowthState import GrowthState
from tkinter import *
from pygame.locals import *


class Anthill:
    def __init__(self, input_apple_hp, input_ant, del_ants, id='0'):
        self.name = __class__.__name__
        self.input_apple_hp = input_apple_hp
        self.uri = self.name + str(id)
        self.r = 500
        self.input_ant = input_ant
        self.agent = None
        self.ants = del_ants
        self.energy = 50
        self.last_energy = self.energy
        self.energy_consumption = 0.01
        self.x = 100
        self.y = 400
        self.height = 50
        self.long = 50
        self.livelihood = 1000  # запасы пропитания
        self.anth_font = pygame.font.Font(pygame.font.match_font('verdana'), size=30)
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
        self.all = False
        self.moving = False
        # self.rect = Rect(self.geo[0],self.geo[1], self.height,self.long)
        self.anthill_icon = pygame.image.load("icons/anthill.png").convert_alpha()
        # print(f'x={self.rect.x}, y={self.rect.y}, w={self.rect.w}, h={self.rect.h}','dddddddddddddd')
        # print(f'left={self.rect.left}, top={self.rect.top}, right={self.rect.right}, bottom={self.rect.bottom}','kkkkkkkk')
        # print(f'center={self.rect.center}')

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

    def body(self):
        return pygame.transform.scale(self.anthill_icon,(self.height,self.long))
        # moving = self.moving
        # self.geo[0] = self.rect[0]
        # self.geo[1] = self.rect[1]
        # print(self.rect, '23223')
        # if not moving:
        #     return pygame.Rect(self.geo[0],self.geo[1], self.height,self.long)
        # else:
        #     return pygame.Rect(display, "Blue" ,anthill.body())
        
    def change_moving(self, new_moving):
        self.moving = new_moving
       
    
    def get_apples(self, scene):
        apples = set()
        for apple in scene:
            if apple.name == 'Apple':
                apples.add(apple)
        return apples
    
    def get_ants(self, scene,):  #метод, возвращающий всех муравьев в зоне обзора
        ants = set()

        for ant in scene:
            if ant.name == 'Ant':
                ants.add(ant)
        return ants

    def get_spiders(self, scene):  #метод, возвращающий всех пауков в зоне обзора
        spiders = set()
        for spider in scene:
            if spider.name == 'Spider':
                spiders.add(spider)
        return spiders
    
    def get_anthills(self, scene):
        anthills = set()
        for anthill in scene:
            if anthill.name == 'Anthill':
                anthills.add(anthill)
        return anthills
    
    def get_food_apple(self, apple):
        self.energy += apple.energy
        self.food_apple += 1

    def run(self):
        self.energy -= self.energy_consumption


    
    def move(self, scene):
        killed = []
        self.scene = scene
        self.anthills = self.get_anthills(scene)
        self.ants = self.get_ants(scene)
        self.apples = self.get_apples(scene)
        i = 0
        for a in self.ants:
            if a.state[0]==4:
                i+=1
        if i>0:
            scene = self.spawnState.move(self, True)
        else:
            scene = self.spawnState.move(self)
        scene = self.growthState.move(self)

        self.tic += 1

        return killed