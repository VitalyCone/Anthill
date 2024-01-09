import datetime
import logging
from os import makedirs

from src.scene.Scene import Scene

from dataclasses import dataclass


@dataclass
class DataStatistics:
    data = {}
    all_logs = []
    info_logs = []


@dataclass
class Denotations:
    """
    Класс хранит в себе словарь uri каждой сущности, когда-либо существовавшей
    """
    uris = {
        'ant': [],
        'spider': [],
        'apple': [],
        'anthill': []
    }


def count_id(entity_class):
    """
    :param entity_class:
    Функция предназначена для выдачи новых id
    :return:
    """
    return len(Denotations.uris[entity_class])


n2 = str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M'))
makedirs('../../logs/' + n2, exist_ok=True)


def start(path):
    makedirs(path + n2, exist_ok=True)
    with open(path + n2 + '/all_logs.txt', 'w') as f:
        pass
    with open(path + n2 + '/info_logs.txt', 'w') as f:
        pass


def rewrite(arg):
    if arg == 0:
        with open('../../logs/' + n2 + '/all_logs.txt', 'a') as file:
            line = DataStatistics.all_logs[-1]
            file.write(line)
        with open('../../logs/' + n2 + '/info_logs.txt', 'a') as file:
            line = DataStatistics.info_logs[-1]
            file.write(line)
    elif arg == 1:
        with open('../../logs/' + n2 + '/all_logs.txt', 'a') as file:
            line = DataStatistics.all_logs[-1]
            file.write(line)


def debug_update(log):
    n = str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M_%S'))
    try:
        DataStatistics.all_logs.append(n + " " + "DEBUG" + " " + log + '\n')
        # rewrite(1)
    except:
        logging.info('Логирование не удалось')
        all_update('Логирование не удалось')


def all_update(log):
    if len(DataStatistics.data.get('Количество сообщений в системе')) < len(DataStatistics.data.get('Номер тика')):
        DataStatistics.data.get('Количество сообщений в системе').append(1)
    elif len(DataStatistics.data.get('Количество сообщений в системе')) > 0:
        DataStatistics.data.get('Количество сообщений в системе')[
            len(DataStatistics.data.get('Количество сообщений в системе')) - 1] += 1
    n = str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M_%S'))
    try:
        DataStatistics.all_logs.append(n + " " + "INFO" + " " + log + '\n')
        DataStatistics.info_logs.append(n + " " + "INFO" + " " + log + '\n')
        # rewrite(0)
    except:
        logging.info('Логирование не удалось')
        all_update('Логирование не удалось')


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
        self.f = []

        DataStatistics.data = {
            'Номер тика': self.teak,
            'Средние значения энергии всех муравьев': self.a,
            'Суммарные значения энергии муравьев': self.b,
            'Средние значения энергии пауков': self.c,
            'Суммарные значения энергии пауков': self.d,
            'Значения энергии муравейника': self.e,
            'Количество сообщений в системе': self.f
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
