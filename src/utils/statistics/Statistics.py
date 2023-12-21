#from src.entitites.Spider import Spider
#from src.entitites.Ant import Ant
#Sfrom src.entitites.Anthill import Anthill
import logging

from src.scene.Scene import Scene

from dataclasses import dataclass

@dataclass
class DataStatistics:
    data = {}
class StatisticsAlfa:

    def __init__(self, scene):
        self.scene = scene
        self.tic = 0
        self.teak = []
        self.a = []
        self.b = []
        self.c = []
        self.d = []
        self.e = []

        DataStatistics.data = {
            'Номер тика': self.teak,
            'Средние значения энергии всех муравьев': self.a,
            'Суммарные значения энергии муравьев': self.b,
            'Средние значения энергии пауков': self.c,
            'Суммарные значения энергии пауков': self.d,
            'Значения энергии муравейника': self.e
        },

    def move(self):
        i = ['Ant', 'Anthill', 'Spider']
        for agent in i:
            energe = 0
            for g in self.scene.get_entities_by_type(agent):
                energe += g.energy
            if agent == 'Ant':
                self.a.append(energe / len(self.scene.get_entities_by_type(agent)))
                self.b.append(energe)
            elif agent == 'Spider':
                self.c.append(energe / len(self.scene.get_entities_by_type(agent)))
                self.d.append(energe)
            elif agent == 'Anthill':
                self.e.append(energe)
        self.teak.append(len(self.teak))
        logging.warning(DataStatistics.data)