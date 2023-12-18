"""Содержит агента группы с обработкой сообщений и переговорами"""
import logging

from src.agents.BaseAgent import AgentBase
from src.utils.Messages.Messages import MessageType
from src.entitites.Group import Group


class GroupAgent(AgentBase):
    """
    Класс агента группы
    """

    def __init__(self):
        super().__init__()
        self.entity: Group
        self.name = 'Агент группы'
        self.subscribe(MessageType.GIVE_CONTROL, self.handle_give_control)
        self.subscribe(MessageType.SCENE_RESPONSE, self.handle_scene_response)
        self.subscribe(MessageType.INVITE_RESPONSE, self.handle_invite_response)

    def handle_invite_response(self, message, sender):
        if message[1][0]:
            logging.info(f'Агент {sender} успешно добавлен в группу {self}')
            self.entity.entities.append(message[1][1])
        else:
            logging.info(f'Не удалось добавить {sender} в группу {self}')

    def handle_scene_response(self, message, sender):
        """
        Обработка полученной сцены
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'{self}: получена сцена от {sender}')
        scene = message[1]
        self.entity.scene = scene
        self.send_invite_message()
        # killed = self.entity.live(scene)
        # if killed:
        #     msg = (MessageType.ENTITY_REMOVE_REQUEST, killed)
        #     scene_address = self.dispatcher.reference_book.get_address(self.scene)
        #     self.send(scene_address, msg)

    def send_invite_message(self):
        ants = self.entity.get_ants(self.entity.scene)
        for ant in ants:
            if ant not in self.entity.entities:
                address = self.dispatcher.reference_book.get_address(ant)
                msg = (MessageType.INVITE_REQUEST, self.entity.aim)
                self.send(address, msg)

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