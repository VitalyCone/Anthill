""" Перечень сообщений, которыми обмениваются агенты"""
from enum import Enum


class MessageType(Enum):
    """
    Перечень сообщений взаимодействия агентов
    """
    # Инициализация агента
    INIT_MESSAGE = 'Initialization'
    GIVE_CONTROL = 'Give control'
    RETURN_CONTROL = 'Return control'
    SCENE_REQUEST = 'Scene request'
    SCENE_RESPONSE = 'Scene response'
    ENTITY_REMOVE_REQUEST = 'Entity remove request'
    SHARE_INFORMATION = 'Share information'
    CREATE_GROUP_AGENT = 'Create group agent'
    INVITE_REQUEST = 'Invite request'
    INVITE_RESPONSE = 'Invite response'
    ATTACK_REQUEST = 'Attack request'
