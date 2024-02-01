import logging
import importlib.resources
import math
import os

from PySide6.QtCore import QPointF, QRectF

from src.GraphicsEntity.GrapicsEntity import GraphicsEntity
from src.states.SpawnState import SpawnState
from src.states.GrowthState import GrowthState
from src.utils.statistics.Statistics import all_update
from src.entitites.BaseEntity import EntityBase


class Anthill(EntityBase):
    def __init__(self, del_ants, id='0'):
        super().__init__()
        MODULE_PATH = importlib.resources.files("assets")
        self.name = __class__.__name__
        self.status = 'alive'
        self.uri = self.name + str(id)
        self.r = 500
        self.agent = None
        self.ants = del_ants
        self.energy = 50
        self.last_energy = self.energy
        self.energy_consumption = 0.005
        self.x = 100
        self.y = 400
        self.u = 0
        self.height = 50
        self.long = 50
        self.livelihood = 1000  # запасы пропитания
        self.exit = False
        self.geo = [self.x, self.y]
        self.scene = None
        self.ants = []
        self.anthills = []
        self.spiders = []
        self.food_apple = 0
        self.s = 0
        self.del_livelihood = 200
        self.pot_ant = 5
        self.pot_ants = len(self.ants) * self.pot_ant
        self.tic = 0
        self.spawnState = SpawnState(self)
        self.growthState = GrowthState(self)
        self.all = False
        self.moving = False
        # self.rect = Rect(self.geo[0],self.geo[1], self.height,self.long)
        # print(f'x={self.rect.x}, y={self.rect.y}, w={self.rect.w}, h={self.rect.h}','dddddddddddddd')
        # print(f'left={self.rect.left}, top={self.rect.top}, right={self.rect.right}, bottom={self.rect.bottom}','kkkkkkkk')
        # print(f'center={self.rect.center}')
        logging.info(f'Объект {self.uri} был успешно инициализирован')
        all_update(f'Объект {self.uri} был успешно инициализирован')
        path = str(os.path.abspath('../../assets/icons/anthill.png'))
        self.graphics_entity = GraphicsEntity(self.geo,
                                              path,
                                              self.u)
        self.graphics_entity.setRect(QRectF(0, 0, self.long, self.height))

    def body(self):
        pass

    def change_moving(self, new_moving):
        self.moving = new_moving

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
        self.graphics_entity.setRect(QRectF(0, 0, self.long, self.height))

    def render(self):
        self.graphics_entity.setPos(QPointF(self.geo[0], self.geo[1]))
        self.graphics_entity.setRotation(math.degrees(self.u))

    def move(self, scene):
        killed = []
        self.scene = scene
        self.anthills = self.get_anthills(scene)
        self.ants = self.get_ants(scene)
        self.apples = self.get_apples(scene)
        scene = self.spawnState.move(self)
        scene = self.growthState.move(self)

        self.tic += 1
        self.run()
        return killed

    def die(self, obj):  # Смерть
        try:  # Через try/except, потому что иногда выскакивают ошибки
            self.scene.remove(obj)
            obj.status = 'dead'
        except:
            pass
        logging.info(f'{self} умер')
        all_update(f'{self} умер')
