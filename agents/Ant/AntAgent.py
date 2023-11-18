"""Содержит агента паука с обработкой сообщений и переговорами"""
import logging

from agents.Base.BaseAgent import AgentBase
from Messages.Messages import MessageType
from agents.Ant.Ant import Ant


class AntAgent(AgentBase):
    """
    Класс агента паука
    """

    def __init__(self):
        super().__init__()
        self.entity: Ant
        self.name = 'Агент муравья'
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
