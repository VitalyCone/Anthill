"""Содержит адресную книгу агентов"""
import logging
from src.utils.statistics.Statistics import all_update, debug_update


class ReferenceBook:
    """Адресная книга агентов с привязкой к сущностям"""
    def __init__(self):
        self.agents_entities = {}

    def clear_reference_book(self):
        self.agents_entities.clear()

    def add_agent(self, entity, agent_address):
        """
        Сохраняет адрес агента с привязкой с сущности
        :param entity:
        :param agent_address:
        :return:
        """
        self.agents_entities[entity] = agent_address

    def get_address(self, entity):
        """
        Возвращает адрес агента указанной сущности.
        :param entity:
        :return:
        """
        if entity not in self.agents_entities:
            logging.error(f'Agent {entity} is not in the reference book')
            all_update(f'Agent {entity} is not in the reference book')
            return None
        return self.agents_entities[entity]

    def clear(self):
        """
        Очищает адресную книгу
        :return:
        """
        self.agents_entities.clear()
