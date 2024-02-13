"""Содержит универсальную реализацию агента с обработкой сообщений"""
import logging
import traceback
from abc import ABC

from thespian.actors import Actor, ActorExitRequest

from src.entitites import BaseEntity
from src.utils.Messages.Messages import MessageType
from src.utils.statistics.Statistics import all_update, debug_update


class Agent(ABC, Actor):
    """
    Универсальная реализация агента
    """

    def __init__(self):
        super().__init__()
        self.name = 'Агент'
        self.handlers = {}
        self.entity: BaseEntity
        self.scene = None
        self.dispatcher = None
        self.entity = None
        self.subscribe(MessageType.INIT_MESSAGE, self.handle_init_message)
        self.subscribe(MessageType.GIVE_CONTROL, self.handle_give_control)
        self.subscribe(MessageType.SCENE_RESPONSE, self.handle_scene_response)
        self.subscribe(MessageType.INVITE_REQUEST, self.handle_invite_request)
        self.subscribe(MessageType.ATTACK_REQUEST, self.handle_attack_request)
        self.subscribe(MessageType.SHARE_INFORMATION, self.handle_share_information)

    def send_information(self, spiders, ants):
        """
        Отправление информации другим агентам-союзникам
        :param spiders:
        :param ants:
        :return:
        """
        if self.dispatcher.negotiations_on:
            for spider in spiders:
                message = (MessageType.SHARE_INFORMATION, ants)
                spider_address = self.dispatcher.reference_book.get_address(spider)
                logging.info(f'{self} поделился информацией с {spider_address}')
                all_update(f'{self} поделился информацией с {spider_address}')
                self.send(spider_address, message)

    def handle_share_information(self, message, sender):
        """
        Обработка переданной информации о сцене от других агентов-союзников
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'Получена информация от агента {sender}')
        all_update(f'Получена информация от агента {sender}')
        self.entity.process_information(message[1])

    def subscribe(self, msg_type: MessageType, handler):
        """
        Подписка на события определенного типа
        :param msg_type: Тип события
        :param handler: Обработчик сообщения заданного типа
        :return:
        """
        if msg_type in self.handlers:
            logging.warning('Повторная подписка на сообщение: %s', msg_type)
            all_update(f'Повторная подписка на сообщение: {msg_type}')
        self.handlers[msg_type] = handler

    def handle_deleted(self, msg, sender):
        """
        :param msg:
        :param sender:
        :return:
        """
        logging.info(f'{self} получил сообщение {msg}, от: {sender}')
        all_update(f'{self} получил сообщение {msg}, от: {sender}')

    def receiveMessage(self, msg, sender):
        """Обрабатывает сообщения - запускает их обработку в зависимости от типа.
        :param msg:
        :param sender:
        :return:
        """
        logging.debug('%s получил сообщение: %s', self.name, msg)
        debug_update(f'{self.name} получил сообщение: {msg}')
        if isinstance(msg, ActorExitRequest):
            logging.info(f'{self} получил сообщение {msg} - ActorExitRequest')
            all_update(f'{self} получил сообщение {msg} - ActorExitRequest')
            self.handle_deleted(msg, sender)
            return

        if isinstance(msg, tuple):

            message_type, message_data = msg
            if message_type in self.handlers:
                try:
                    self.handlers[message_type](msg, sender)
                except Exception as ex:
                    traceback.print_exc()
                    logging.error(ex)
                    all_update(traceback.format_exc())
            else:
                logging.warning('%s Отсутствует подписка на сообщение: %s', self.name, message_type)
                all_update(f'{self.name} Отсутствует подписка на сообщение: {message_type}')
        else:
            logging.error('%s Неверный формат сообщения: %s', self.name, msg)
            all_update(f'{self.name} Неверный формат сообщения: {msg}')
            super().receiveMessage(msg, sender)

    def __str__(self):
        return self.name

    def handle_init_message(self, message, sender):
        """
        Обработка сообщения с инициализацией - сохранение присланных данных в агенте.
        :param message:
        :param sender:
        :return:
        """
        self.scene = message[1].get('scene')
        self.dispatcher = message[1].get('dispatcher')
        self.entity = message[1].get('entity')
        self.name += " " + self.entity.name
        self.entity.agent = self
        self.name = self.name + ' ' + self.entity.name
        logging.info(f'{self} проинициализирован')
        all_update(f'{self} проинициализирован')

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
        all_update(f'{self}: получен {message} от {sender}')
        scene_request_msg = (MessageType.SCENE_REQUEST, (self.entity.geo, self.entity.r))
        courier_address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(courier_address, scene_request_msg)

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
