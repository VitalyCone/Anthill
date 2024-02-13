"""Содержит класс агента муравейника с обработкой сообщений"""
import logging

from src.entitites.Anthill import Anthill
from src.agents.BaseAgent import AgentBase

from src.utils.Messages.Messages import MessageType
from src.utils.statistics.Statistics import debug_update, all_update


class AnthillAgent(AgentBase):
    """
    Класс агента муравейника
    """
    def __init__(self):
        super().__init__()
        self.entity: Anthill
        self.name = 'Агент муравейника'
