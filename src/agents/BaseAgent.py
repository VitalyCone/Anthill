"""Содержит базовую реализацию агента с обработкой сообщений"""
import logging
import traceback
from abc import ABC

from thespian.actors import Actor, ActorExitRequest

from src.utils.Messages.Messages import MessageType
from src.utils.statistics.Statistics import all_update, debug_update


class AgentBase(ABC, Actor):
    """
    Базовая реализация агента
    """

    def __init__(self):
        self.name = 'Base agent'
        super().__init__()
        self.handlers = {}
        self.scene = None
        self.dispatcher = None
        self.entity = None
        self.subscribe(MessageType.INIT_MESSAGE, self.handle_init_message)
        self.subscribe(MessageType.GIVE_CONTROL, self.handle_give_control)
        self.subscribe(MessageType.SCENE_RESPONSE, self.handle_scene_response)

    def subscribe(self, msg_type: MessageType, handler):
        """
        Подписка на события определенного типа
        :param msg_type: Тип события
        :param handler: Обработчик сообщения заданного типа
        :return:
        """
        if msg_type in self.handlers:
            logging.warning('Resubscribe to message: %s', msg_type)
            all_update(f'Resubscribe to message: {msg_type}')
        self.handlers[msg_type] = handler

    def handle_deleted(self, msg, sender):
        """
        :param msg:
        :param sender:
        :return:
        """
        logging.info(f'{self} received message {msg} from: {sender}')
        all_update(f'{self} received message {msg} from: {sender}')

    def receiveMessage(self, msg, sender):
        """Обрабатывает сообщения - запускает их обработку в зависимости от типа.
        :param msg:
        :param sender:
        :return:
        """
        logging.debug('%s received message: %s', self.name, msg)
        debug_update(f'{self.name} received messageе: {msg}')
        if isinstance(msg, ActorExitRequest):
            logging.info(f'{self} received message {msg} - ActorExitRequest')
            all_update(f'{self} received message {msg} - ActorExitRequest')
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
                logging.warning('%s Message not subscribed: %s', self.name, message_type)
                all_update(f'{self.name} Message not subscribed: {message_type}')
        else:
            logging.error('%s Invalid message format: %s', self.name, msg)
            all_update(f'{self.name} Invalid message format: {msg}')
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
        self.entity.agent = self
        self.name = self.name + ' ' + self.entity.name
        logging.info(f'{self} initialized')
        all_update(f'{self} initialized')

    def handle_scene_response(self, message, sender):
        """
        Обработка полученной сцены
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'{self}: scene received from {sender}')
        all_update(f'{self}: scene received from {sender}')
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
        logging.info(f'{self}: received {message} from {sender}')
        all_update(f'{self}: received {message} from {sender}')
        scene_request_msg = (MessageType.SCENE_REQUEST, (self.entity.geo, self.entity.r))
        courier_address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(courier_address, scene_request_msg)
