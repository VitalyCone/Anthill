"""Содержит агента паука с обработкой сообщений и переговорами"""
import logging

from src.agents.BaseAgent import AgentBase
from src.utils.Messages.Messages import MessageType
from src.entitites.Spider import Spider
from src.utils.statistics.Statistics import all_update, debug_update


class SpiderAgent(AgentBase):
    """
    Класс агента паука
    """

    def __init__(self):
        super().__init__()
        self.entity: Spider
        self.name = 'Агент паука'
        self.subscribe(MessageType.GIVE_CONTROL, self.handle_give_control)
        self.subscribe(MessageType.SCENE_RESPONSE, self.handle_scene_response)
        self.subscribe(MessageType.SHARE_INFORMATION, self.handle_share_information)

    def send_information(self, spiders, ants):
        """
        Отправление информации другим паукам
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
        Обработка переданной информации о муравьях от других пауков
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'Получена информация от агента {sender}')
        all_update(f'Получена информация от агента {sender}')
        self.entity.process_information(message[1])

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
