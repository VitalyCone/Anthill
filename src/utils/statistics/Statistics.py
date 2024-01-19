import datetime
import logging
from os import makedirs
import yaml

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
            entities = self.scene.get_entities_by_type(agent)
            if entities:
                for g in entities:
                    energy += g.energy
            else:
                energy = 0
            if agent == 'Ant':
                if energy == 0:
                    self.a.append(0)
                else:
                    try:
                        self.a.append(energy / len(entities))
                    except ZeroDivisionError:
                        self.a.append(0)
                    self.b.append(energy)
            elif agent == 'Spider':
                if energy == 0:
                    self.a.append(0)
                else:
                    try:
                        self.c.append(energy / len(entities))
                    except ZeroDivisionError or TypeError:
                        self.c.append(0)
                    self.d.append(energy)
            elif agent == 'Anthill':
                self.e.append(energy)
        self.teak.append(len(self.teak))
