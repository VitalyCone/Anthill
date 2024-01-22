""" Реализация класса агента сцены"""
import logging
from src.agents.BaseAgent import AgentBase
from src.entitites.Group import Group

from src.utils.Messages.Messages import MessageType
from src.scene.Scene import Scene
from src.utils.statistics.Statistics import all_update, debug_update, count_id, Denotations


class SceneAgent(AgentBase):
    """
    Класс агента сцены
    """

    def __init__(self):
        # Сцена хранит массив из сущностей
        super().__init__()
        self.entity: Scene
        self.name = 'Агент сцены'
        self.subscribe(MessageType.SCENE_REQUEST, self.handle_scene_request_message)
        self.subscribe(MessageType.ENTITY_REMOVE_REQUEST, self.handle_entity_remove_request)
        self.subscribe(MessageType.CREATE_GROUP_AGENT, self.handle_create_group_agent)

    def handle_create_group_agent(self, message, sender):
        group = Group(message[1][1].scene, count_id("group"), message[1][0], message[1][1])
        Denotations.uris['group'].append(group.uri)
        logging.info(f"Группа {group} была создана")
        all_update(f"Группа {group} была создана")
        self.dispatcher.add_entity(group)

    def handle_scene_request_message(self, message, sender):
        """
        Обработка запроса сцены по заданному радиусу
        :param message:
        :param sender:
        :return:
        """
        logging.info(f'{self}: получен запрос сцены от {sender}')
        all_update(f'{self}: получен запрос сцены от {sender}')
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
        for uri in message[1]:
            self.entity.remove_entity_by_uri(uri)
            logging.info(f'{uri} был(а) удален(а) из сцены агентом {sender}')
            all_update(f'{uri} был(а) удален(а) из сцены агентом {sender}')
