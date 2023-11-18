"""Содержит агента паука с обработкой сообщений и переговорами"""
import logging

from agents.Base.BaseAgent import AgentBase
from Messages.Messages import MessageType
from agents.Spider.Spider import Spider


class SpiderAgent(AgentBase):
    """
    Класс агента паука
    """

    def __init__(self):
        super().__init__()
        self.entity: Spider
        self.name = 'Агент паука'
        self.subscribe(MessageType.GIVE_CONTROL, self.handle_give_control)

    def handle_give_control(self, message, sender):
        """
        Обработка сообщения о передаче управления
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'{self}: получен {message} от {sender}')
        self.entity.live()
