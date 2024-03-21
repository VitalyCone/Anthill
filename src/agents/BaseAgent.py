"""Содержит базовую реализацию агента с обработкой сообщений"""
import logging
import traceback
from abc import ABC

from thespian.actors import Actor, ActorExitRequest

from src.utils.Messages.Messages import MessageType
from src.utils.statistics.Statistics import all_update, debug_update, Localization, Config


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
        self.locale = Config.dataset["locale"]
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
            msg = Localization.dataset["agent_base"]["subscribe_msg"][self.locale].format(msg_type=msg_type)
            logging.warning(msg)
            all_update(f'Resubscribe to message: {msg}')
        self.handlers[msg_type] = handler

    def handle_deleted(self, msg, sender):
        """
        :param msg:
        :param sender:
        :return:
        """
        log_data = Localization.dataset["agent_base"]["handle_deleted"][self.locale].format(self=self, msg=msg,
                                                                                            sender=sender)
        logging.info(log_data)
        all_update(log_data)

    def receiveMessage(self, msg, sender):
        """Обрабатывает сообщения - запускает их обработку в зависимости от типа.
        :param msg:
        :param sender:
        :return:
        """
        log_data = Localization.dataset["agent_base"]["receive_msg"][self.locale].format(name=self.name, msg=msg)
        logging.debug(log_data)
        debug_update(log_data)
        if isinstance(msg, ActorExitRequest):
            log_data = Localization.dataset["agent_base"]["receive_actor_exit_request"][self.locale].format(self=self, msg=msg)
            logging.info(log_data)
            all_update(log_data)
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
                log_data = Localization.dataset["agent_base"]["message_not_subscribed"][self.locale].format(
                    name=self.name, message_type=message_type)
                logging.warning(log_data)
                all_update(log_data)
        else:
            log_data = Localization.dataset["agent_base"]["invalid_msg"][self.locale].format(name=self.name, msg=msg)
            logging.error(log_data)
            all_update(log_data)
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
        log_data = Localization.dataset["agent_base"]["initialization_msg"][self.locale].format(self=self)
        logging.info(log_data)
        all_update(log_data)

    def handle_scene_response(self, message, sender):
        """
        Обработка полученной сцены
        :param message:
        :param sender:
        :return:
        """
        log_data = Localization.dataset["agent_base"]["handle_scene_response_msg"][self.locale].format(
            self=self, sender=sender)
        logging.info(log_data)
        all_update(log_data)
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
        log_data = Localization.dataset["agent_base"]["handle_give_control_msg"][self.locale].format(
            self=self, message=message, sender=sender)
        logging.info(log_data)
        all_update(log_data)
        scene_request_msg = (MessageType.SCENE_REQUEST, (self.entity.geo, self.entity.r))
        courier_address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(courier_address, scene_request_msg)
