"""Содержит агента яблока с обработкой сообщений"""
import logging

from src.agents.BaseAgent import AgentBase
from src.entitites.Apple import Apple

from src.utils.Messages.Messages import MessageType
from src.utils.statistics.Statistics import all_update, debug_update


class AppleAgent(AgentBase):
    """
    Класс агента яблока
    """
    def __init__(self):
        super().__init__()
        self.entity: Apple
        self.name = 'Apple agent'
