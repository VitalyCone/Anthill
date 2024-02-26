"""Содержит агента группы с обработкой сообщений и переговорами"""
import logging

from src.agents.BaseAgent import AgentBase
from src.utils.Messages.Messages import MessageType
from src.entitites.Group import Group
from src.utils.statistics.Statistics import all_update


class GroupAgent(AgentBase):
    """
    Класс агента группы
    """

    def __init__(self):
        super().__init__()
        self.entity: Group
        self.name = 'Group agent'
        self.subscribe(MessageType.GIVE_CONTROL, self.handle_give_control)
        self.subscribe(MessageType.SCENE_RESPONSE, self.handle_scene_response)
        self.subscribe(MessageType.INVITE_RESPONSE, self.handle_invite_response)

    def handle_invite_response(self, message, sender):
        if message[1][0]:
            logging.info(
                f'Agent {sender} was successfully added to the group {self.entity.uri}'
            )
            all_update(
                f'Agent {sender} was successfully added to the group {self.entity.uri}'
            )
            self.entity.entities.append(message[1][1])
            message[1][1].group = self.entity
        else:
            logging.info(f'Failed to add {sender} to group {self}')
            all_update(f'Failed to add {sender} to group {self}')

    def handle_scene_response(self, message, sender):
        """
        Обработка полученной сцены
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'{self}: received scene from {sender}')
        all_update(f'{self}: received scene from {sender}')
        scene = message[1]
        self.entity.scene = scene
        self.send_invite_message()
        for entity in self.entity.entities:
            if entity.status == 'dead':
                self.entity.entities.remove(entity)
        if self.entity.aim.status == 'dead' or self.entity.leader.status == 'dead':
            self.remove_group()
        entities_ready_attack = []
        for entity in self.entity.entities:
            if entity.get_distance(self.entity.leader) <= entity.speed and not entity.attack:
                entities_ready_attack.append(entity)
        if (self.entity.aim.name == 'Spider'
                and len(entities_ready_attack) > 5):
            for entity in self.entity.entities:
                address = self.dispatcher.reference_book.get_address(entity)
                msg = (MessageType.ATTACK_REQUEST, True)
                self.send(address, msg)
        self.entity.make_damage()

    def remove_group(self):
        if self.entity.aim.name == 'Apple':
            if self.entity.aim.status == 'dead':
                self.entity.leader.anthill.energy += self.entity.aim.energy
        for entity in self.entity.entities:
            entity.prey = None
            entity.group = None
            entity.attack = False
            if self.entity.aim.status == 'dead':
                entity.energy += 1
        msg = (MessageType.ENTITY_REMOVE_REQUEST, [[self.entity.uri, self.entity.version]])
        address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(address, msg)

    def send_invite_message(self):
        if self.dispatcher.negotiations_on:
            if self.entity.aim.speed >= self.entity.leader.speed and self.entity.aim.name == 'Apple':
                return
            ants = self.entity.get_ants(self.entity.scene)
            for ant in ants:
                if self.entity.aim.speed >= self.entity.leader.speed and self.entity.aim.name == 'Apple':
                    break
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
        logging.info(f'{self}: received {message} from {sender}')
        all_update(f'{self}: received {message} from {sender}')
        scene_request_msg = (MessageType.SCENE_REQUEST, (self.entity.geo, self.entity.r))
        courier_address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(courier_address, scene_request_msg)

    def kill_aim(self):
        """
        Убийство цели
        :return:
        """
        msg = (MessageType.ENTITY_REMOVE_REQUEST, [self.entity.aim.uri])
        address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(address, msg)
