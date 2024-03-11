import datetime
import logging
from os import makedirs

from dataclasses import dataclass

import yaml


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
        'anthill': [],
        'group': []
    }


@dataclass
class Config:
    dataset = {}


def setConfig(config_file_path='config.yml'):
    """
    Функция по заданному пути открывает yml конфиг
    и считывает как словарь.

    Пример:
    spider.r = Config.dataset['spider']['radius']
    ant.speed = Config.dataset['ant']['speed']

    Получается так, что dataset - это словарь,
    внутри которого (на данный момент) существуют
    три словаря - system, spider и ant.

    Функция вызывается один раз в main, в дальнейшем
    требуется использовать класс Config.
    """
    with open(config_file_path, 'r') as config_file:
        config_data = yaml.safe_load(config_file)
    Config.dataset = config_data


def null_uris():
    """
    Обнуляет словарь с занятыми ссылками
    """
    Denotations.uris = {
        'ant': [],
        'spider': [],
        'apple': [],
        'anthill': [],
        'group': []
    }


def count_id(entity_class):
    """
    :param entity_class:
    Функция предназначена для выдачи новых id
    :return:
    """
    return len(Denotations.uris[entity_class])


n2 = str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M'))


def write_logs():
    path = 'logs/'
    makedirs(path + n2, exist_ok=True)
    with open(path + n2 + '/all_logs.txt', 'w') as f:
        for log in DataStatistics.all_logs[::-1]:
            f.write(log)
    with open(path + n2 + '/info_logs.txt', 'w') as f:
        for log in DataStatistics.info_logs[::-1]:
            f.write(log)


def debug_update(log):
    n = str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M_%S'))
    try:
        DataStatistics.all_logs.append(n + " " + "DEBUG" + " " + log + '\n')
    except:
        logging.info('Logging failed')
        all_update('Logging failed')


def all_update(log):
    if len(DataStatistics.data.get('Number of messages')) > 0:
        DataStatistics.data.get('Number of messages')[
            len(DataStatistics.data.get('Number of messages')) - 1] += 1
    n = str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M_%S'))
    try:
        DataStatistics.all_logs.append(n + " " + "INFO" + " " + log + '\n')
        DataStatistics.info_logs.append(n + " " + "INFO" + " " + log + '\n')
    except:
        logging.info('Logging failed')
        all_update('Logging failed')


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
        self.g = []
        self.h = []
        self.i = []

        DataStatistics.data = {
            'Number of tic': self.teak,
            'Average energy of ant': self.a,
            'Accumulated energy of ants': self.b,
            'Average energy of spider': self.c,
            'Accumulated energy of spiders': self.d,
            'Energy of anthill': self.e,
            'Number of messages': self.f,
            'Number of ants': self.g,
            'Number of spiders': self.h,
            'Number of apples': self.i
        }

    def move(self):
        i = ['Ant', 'Anthill', 'Spider']
        for agent in i:
            energy = 0
            entities = self.scene.get_entities_by_type(agent)
            if entities:
                for g in entities:
                    energy += g.energy
            else:
                energy = 0
            if agent == 'Ant':
                self.g.append(len(entities))
                if energy == 0:
                    self.b.append(0)
                else:
                    try:
                        self.a.append(energy / len(entities))
                    except ZeroDivisionError:
                        self.a.append(0)
                    self.b.append(energy)
            elif agent == 'Spider':
                self.h.append(len(entities))
                if energy == 0:
                    self.d.append(0)
                else:
                    try:
                        self.c.append(energy / len(entities))
                    except ZeroDivisionError or TypeError:
                        self.c.append(0)
                    self.d.append(energy)
            elif agent == 'Anthill':
                self.i.append(len(entities))
                self.e.append(energy)
        self.teak.append(len(self.teak))
        self.f.append(0)
