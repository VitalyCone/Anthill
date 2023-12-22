"""Содержит агента паука с обработкой сообщений и переговорами"""
import logging

from src.agents.BaseAgent import AgentBase
from src.utils.Messages.Messages import MessageType
from src.entitites.Ant import Ant


class AntAgent(AgentBase):
    """
    Класс агента паука
    """

    def __init__(self):
        super().__init__()
        self.entity: Ant
        self.name = 'Агент муравья'
        self.subscribe(MessageType.GIVE_CONTROL, self.handle_give_control)
        self.subscribe(MessageType.SCENE_RESPONSE, self.handle_scene_response)
        self.subscribe(MessageType.INVITE_REQUEST, self.handle_invite_request)
        self.subscribe(MessageType.ATTACK_REQUEST, self.handle_attack_request)

    def handle_attack_request(self, message, sender):
        """
        Обработка запроса на атаку агента
        :param message:
        :param sender:
        :return:
        """
        self.entity.attack = message[1]

    def handle_invite_request(self, message, sender):
        """
        Обработка приглашения в группу
        :param message:
        :param sender:
        :return:
        """
        if self.entity.prey is None or self.entity.prey.energy <= message[1].energy:
            self.entity.prey = message[1]
            msg = (MessageType.INVITE_RESPONSE, (True, self.entity))
        else:
            msg = (MessageType.INVITE_RESPONSE, (False, None))
        self.send(sender, msg)

    def handle_scene_response(self, message, sender):
        """
        Обработка полученной сцены
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'{self}: получена сцена от {sender}')
        scene = message[1]
        killed = self.entity.live(scene)
        if killed:
            msg = (MessageType.ENTITY_REMOVE_REQUEST, killed)
            scene_address = self.dispatcher.reference_book.get_address(self.scene)
            self.send(scene_address, msg)

    def handle_give_control(self, message, sender):
        """
        Обработка сообщения о передаче управления
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'{self}: получен {message} от {sender}')
        scene_request_msg = (MessageType.SCENE_REQUEST, (self.entity.geo, self.entity.r))
        courier_address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(courier_address, scene_request_msg)

    def create_group(self, aim, leader):
        """
        Отправка сообщений о созданиии группы
        :param aim:
        :param leader:
        :return:
        """
        scene_request_msg = (MessageType.CREATE_GROUP_AGENT, (aim, leader))
        address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(address, scene_request_msg)

