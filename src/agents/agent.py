"""Содержит универсальную реализацию агента с обработкой сообщений"""
import logging
import traceback
from abc import ABC

from thespian.actors import Actor, ActorExitRequest

from src.agents.BaseAgent import AgentBase
from src.entitites import BaseEntity
from src.utils.Messages.Messages import MessageType
from src.utils.statistics.Statistics import all_update, debug_update


class Agent(AgentBase):
    """
    Универсальная реализация агента
    """

    def __init__(self):
        super().__init__()
        self.name = 'Agent'
        self.entity: BaseEntity
        self.subscribe(MessageType.INVITE_REQUEST, self.handle_invite_request)
        self.subscribe(MessageType.ATTACK_REQUEST, self.handle_attack_request)
        self.subscribe(MessageType.SHARE_INFORMATION, self.handle_share_information)

    def send_information(self, spiders, ants):
        """
        Отправление информации другим агентам-союзникам
        :param spiders:
        :param ants:
        :return:
        """
        if self.dispatcher.negotiations_on:
            for spider in spiders:
                message = (MessageType.SHARE_INFORMATION, ants)
                spider_address = self.dispatcher.reference_book.get_address(spider)
                logging.info(f'{self} shared information with {spider_address}')
                all_update(f'{self} shared information with {spider_address}')
                self.send(spider_address, message)

    def handle_share_information(self, message, sender):
        """
        Обработка переданной информации о сцене от других агентов-союзников
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'Info received from agent {sender}')
        all_update(f'Info received from agent{sender}')
        self.entity.process_information(message[1])

    def handle_attack_request(self, message, sender):
        """
        Обработка запроса на атаку агента
        :param message:
        :param sender:
        :return:
        """
        self.entity.attack = message[1]

    def handle_invite_request(self, message, sender):
        """
        Обработка приглашения в группу
        :param message:
        :param sender:
        :return:
        """
        if self.entity.prey is None or self.entity.prey.energy <= message[1].energy:
            self.entity.prey = message[1]
            msg = (MessageType.INVITE_RESPONSE, (True, self.entity))
        else:
            msg = (MessageType.INVITE_RESPONSE, (False, None))
        self.send(sender, msg)

    def create_group(self, aim, leader):
        """
        Отправка сообщений о созданиии группы
        :param aim:
        :param leader:
        :return:
        """
        self.dispatcher.create_group(aim, leader)

    def connect_to_group(self, group_uri):
        """
        Отправка запроса на присоединение к группе
        """
        group_entity = self.dispatcher.scene.get_entity_by_uri(group_uri)
        address = self.dispatcher.reference_book.get_address(group_entity)
        msg = (MessageType.INVITE_RESPONSE, (True, self.entity))
        self.send(address, msg)

