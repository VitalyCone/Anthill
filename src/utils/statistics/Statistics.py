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
            energy = 0
            for g in self.scene.get_entities_by_type(agent):
                energy += g.energy
            if agent == 'Ant':
                try:
                    self.a.append(energy / len(self.scene.get_entities_by_type(agent)))
                except ZeroDivisionError:
                    self.c.append(0)
                self.b.append(energy)
            elif agent == 'Spider':
                try:
                    self.c.append(energy / len(self.scene.get_entities_by_type(agent)))
                except ZeroDivisionError:
                    self.c.append(0)
                self.d.append(energy)
            elif agent == 'Anthill':
                self.e.append(energy)
        self.teak.append(len(self.teak))
