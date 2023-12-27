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
        self.name = 'Базовый агентfrom src.utils.statistics.Statistics import all_update, debug_update'
        super().__init__()
        self.handlers = {}
        self.scene = None
        self.dispatcher = None
        self.entity = None
        self.subscribe(MessageType.INIT_MESSAGE, self.handle_init_message)

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
        self.entity.agent = self
        self.name = self.name + ' ' + self.entity.name
        logging.info(f'{self} проинициализирован')
        all_update(f'{self} проинициализирован')
