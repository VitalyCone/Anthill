"""Содержит агента группы с обработкой сообщений и переговорами"""
import logging

from src.agents.BaseAgent import AgentBase
from src.utils.Messages.Messages import MessageType
from src.entitites.Group import Group
from src.utils.statistics.Statistics import all_update, debug_update

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
            all_update(f'Агент {sender} успешно добавлен в группу {self}')
            self.entity.entities.append(message[1][1])
            message[1][1].group = self.entity
        else:
            logging.info(f'Не удалось добавить {sender} в группу {self}')
            all_update(f'Не удалось добавить {sender} в группу {self}')

    def handle_scene_response(self, message, sender):
        """
        Обработка полученной сцены
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'{self}: получена сцена от {sender}')
        all_update(f'{self}: получена сцена от {sender}')
        scene = message[1]
        self.entity.scene = scene
        if len(self.entity.entities) <= 10:
            self.send_invite_message()
        for entity in self.entity.entities:
            if entity.status == 'dead':
                self.entity.entities.remove(entity)
        if self.entity.aim.status == 'dead' or self.entity.leader.status == 'dead':
            for entity in self.entity.entities:
                entity.prey = None
                entity.group = None
                entity.attack = False
            msg = (MessageType.ENTITY_REMOVE_REQUEST, [self.entity.uri])
            address = self.dispatcher.reference_book.get_address(self.scene)
            self.send(address, msg)
        entities_ready_attack = []
        for entity in self.entity.entities:
            if entity.get_distance(self.entity.leader) <= entity.speed and not entity.attack:
                entities_ready_attack.append(entity)
        if self.entity.aim.name == 'Spider' and len(entities_ready_attack) > 3:
            for entity in self.entity.entities:
                address = self.dispatcher.reference_book.get_address(entity)
                msg = (MessageType.ATTACK_REQUEST, True)
                self.send(address, msg)
        self.entity.make_damage()

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
        all_update(f'{self}: получен {message} от {sender}')
        scene_request_msg = (MessageType.SCENE_REQUEST, (self.entity.geo, self.entity.r))
        courier_address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(courier_address, scene_request_msg)

    def kill_aim(self):
        msg = (MessageType.ENTITY_REMOVE_REQUEST, [self.entity.aim.uri])
        address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(address, msg)
