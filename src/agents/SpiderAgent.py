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
        self.name = 'Spider Agent'
