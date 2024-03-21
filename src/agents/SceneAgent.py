""" Реализация класса агента сцены"""
import logging
from src.agents.BaseAgent import AgentBase
from src.entitites.Group import Group

from src.utils.Messages.Messages import MessageType
from src.scene.Scene import Scene
from src.utils.statistics.Statistics import all_update, debug_update, count_id, Denotations, Localization, Config


class SceneAgent(AgentBase):
    """
    Класс агента сцены
    """

    def __init__(self):
        # Сцена хранит массив из сущностей
        super().__init__()
        self.entity: Scene
        self.name = 'Scene agent'
        self.locale = Config.dataset["locale"]
        self.subscribe(MessageType.SCENE_REQUEST, self.handle_scene_request_message)
        self.subscribe(MessageType.ENTITY_REMOVE_REQUEST, self.handle_entity_remove_request)

    def handle_scene_request_message(self, message, sender):
        """
        Обработка запроса сцены по заданному радиусу
        :param message:
        :param sender:
        :return:
        """
        log_data = Localization.dataset["scene_agent"]["handle_request_scene_msg"][self.locale].format(
            self=self.name, sender=sender)
        logging.info(log_data)
        all_update(log_data)
        entities_in_radius = []
        geo = message[1][0]
        radius = message[1][1]
        for entity_list in self.entity.entities.values():
            for entity in entity_list:
                if abs(entity.geo[0] - geo[0]) <= radius and abs(entity.geo[1] - geo[1]) <= radius:
                    entities_in_radius.append(entity)
        msg = (MessageType.SCENE_RESPONSE, entities_in_radius)
        self.send(sender, msg)

    def handle_entity_remove_request(self, message, sender):
        """
        Oбработка запроса на удаление существа из сцены
        :param message:
        :param sender:
        :return:
        """
        for entity in message[1]:
            uri = entity[0]
            # version = entity[1]
            entity = self.entity.get_entity_by_uri(uri)
            if entity:
                # if self.entity.get_entity_by_uri(uri).version == version:
                log_data = Localization.dataset["scene_agent"]["handle_entity_remove_request_msg"][self.locale].format(
                    uri=uri, sender=sender)
                self.entity.remove_entity_by_uri(uri)
                logging.info(log_data)
                all_update(log_data)
