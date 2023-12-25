"""Содержит агента игры"""
import logging

from src.agents.BaseAgent import AgentBase

from src.game.Game import Game
from src.utils.Messages.Messages import MessageType
from src.utils.statistics.Statistics import info_update


class GameAgent(AgentBase):
    """
    Класс агента игры
    """
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.entity: Game
        self.name = 'Агент игры'
        self.subscribe(MessageType.GAME_RENDERING_REQUEST, self.handle_game_rendering_request)
        # TODO: определить ответ на сообщение о запросе рендеринга игры
        # TODO: определить возвращаемое сообщение о продолжении планирования игры

    def handle_game_rendering_request(self, message, sender):
        """
        Обработка запроса на рендеринг игры
        :param message:
        :param sender:
        :return:
        """
        self.logger.info(f'Получен запрос на рендеринг игры')
        info_update('Получен запрос на рендеринг игры')
        pause = self.entity.render_game()
        self.dispatcher.pause = pause
        self.send(sender, (MessageType.GAME_RENDERING_RESPONSE, pause))
