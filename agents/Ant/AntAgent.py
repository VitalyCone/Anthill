"""Содержит агента паука с обработкой сообщений и переговорами"""
import logging

from agents.Base.BaseAgent import AgentBase
from Messages.Messages import MessageType
from agents.Ant.Ant import Ant
from states.AttackState import AttackState
from states.DefenseState import DefenseState
from states.InterectionState import InterectionState
from states.RunawayState import RunawayState

class AntAgent(AgentBase):
    """
    Класс агента паука
    """

    def __init__(self):
        
        super().__init__()
        self.entity: Ant
        self.name = 'Агент муравья'
        self.subscribe(MessageType.GIVE_CONTROL, self.handle_give_control)
        self.subscribe(MessageType.SCENE_RESPONSE, self.handle_scene_response)
        # Новые подписки
        self.subscribe(MessageType.ATTACK, AttackState(self.entity))
        self.subscribe(MessageType.DEFENSE, DefenseState(self.entity))
        self.subscribe(MessageType.INTERECTION, InterectionState(self.entity))
        self.subscribe(MessageType.RUNAWAY, RunawayState(self.entity))

    def handle_scene_response(self, message, sender):
        """
        Обработка полученной сцены
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'{self}: получена сцена от {sender}')
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
        scene_request_msg = (MessageType.SCENE_REQUEST, (self.entity.geo, self.entity.r))
        courier_address = self.dispatcher.reference_book.get_address(self.scene)
        self.send(courier_address, scene_request_msg)
