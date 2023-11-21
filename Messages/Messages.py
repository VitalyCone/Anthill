""" Перечень сообщений, которыми обмениваются агенты"""
from enum import Enum


class MessageType(Enum):
    """
    Перечень сообщений взаимодействия агентов
    """
    # Инициализация агента
    INIT_MESSAGE = 'Инициализация'
    GIVE_CONTROL = 'Передать управление'
    RETURN_CONTROL = 'Вернуть управление'
    SCENE_REQUEST = 'Запрос сцены'
    SCENE_RESPONSE = 'Ответ на запрос сцены'
    ENTITY_REMOVE_REQUEST = 'Запрос на удаление существа'

