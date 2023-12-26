"""Содержит агента игры"""
import logging

from src.agents.BaseAgent import AgentBase

from src.Game.Game import Game
from src.utils.Messages.Messages import MessageType
from src.utils.statistics.Statistics import all_update


class GameAgent(AgentBase):
    """
    Класс агента игры
    """
    def __init__(self):
        super().__init__()
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
        logging.info(f'Получен запрос на рендеринг игры')
        all_update(f'Получен запрос на рендеринг игры')
        pause = self.entity.render_game()
        if self.entity.pause or self.entity.pause_agents:
            pause = True
        self.dispatcher.pause = pause
        self.send(sender, (MessageType.GAME_RENDERING_RESPONSE, pause))
