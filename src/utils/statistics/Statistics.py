import datetime
import logging
from os import makedirs

from src.scene.Scene import Scene

from dataclasses import dataclass


@dataclass
class DataStatistics:
    data = {}


@dataclass
class LogStatistics:
    all_logs = []
    info_logs = []
    n2 = str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M'))
    makedirs('../../logs/' + n2, exist_ok=True)

    def rewrite(self):
        makedirs('../../logs/' + self.n2, exist_ok=True)
        with open("../../logs/" + self.n2 + "/all_logs.txt", "w") as file:
            for line in self.all_logs:
                file.write(line)
        with open("../../logs/" + self.n2 + "/info_logs.txt", "w") as file:
            for line in self.info_logs:
                file.write(line)

    def debug_update(self, log):
        n = str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M'))
        self.all_logs.append(n + " " + "DEBUG" + " " + log)
        self.rewrite()

    def info_update(self, log):
        n = str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M'))
        self.all_logs.append(n + " " + "INFO" + " " + log)
        self.info_logs.append(n + " " + "INFO" + " " + log)
        self.rewrite()


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
        }

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
