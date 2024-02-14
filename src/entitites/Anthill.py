import logging
import importlib.resources
import math
import os

from PySide6.QtCore import QPointF, QRectF

from src.GraphicsEntity.GrapicsEntity import GraphicsEntity
from src.states.SpawnState import SpawnState
from src.states.GrowthState import GrowthState
from src.utils.statistics.Statistics import all_update, Config
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
        self.exit = False
        self.geo = [self.x, self.y]
        self.scene = None
        self.ants = []
        self.spiders = []
        self.food_apple = 0
        self.s = 0
        self.del_livelihood = 200
        self.pot_ant = 5
        self.pot_ants = len(self.ants) * self.pot_ant
        self.tic = 0
        self.spawnState = SpawnState(self)
        self.growthState = GrowthState(self)
        self.spawn_gap = Config.dataset['system']['ant_spawn_time']
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

    def get_food_apple(self, apple):
        """
        Муравейник поглощает яблоко.
        :param apple:
        :return:
        """
        self.energy += apple.energy
        self.food_apple += 1

    def run(self):
        """
        Отрисовка муравейника.
        :return:
        """
        super().run()
        self.graphics_entity.setRect(QRectF(0, 0, self.long, self.height))

    def move(self, scene):
        """
        Функция представляет собой единичный шаг сущности.
        :param scene:
        :return:
        """
        super().move(scene)
        self.spawnState.move(self)
        self.growthState.move(self)

        self.tic += 1
        self.run()
        return self.removed

