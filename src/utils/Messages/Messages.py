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
    SHARE_INFORMATION = 'Поделиться информацией'
    GAME_RENDERING_REQUEST = 'Запрос на отрисовку игрового поля'
    GAME_RENDERING_RESPONSE = 'Ответ на запрос на отрисовку игрового поля'
    CREATE_GROUP_AGENT = 'Создать агента группы'
    INVITE_REQUEST = 'Приглашение'
    INVITE_RESPONSE = 'Ответ на приглашение'
    ATTACK_REQUEST = 'Запрос атаки'
