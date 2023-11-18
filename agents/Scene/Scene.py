""" Реализация класса сцены"""
from collections import defaultdict


class Scene:
    """
    Класс сцены
    """

    def __init__(self):
        # Сцена хранит массив из сущностей
        self.entities = defaultdict(list)

    def get_entities_by_type(self, entity_type):
        """
        Возвращает список сущностей заданного типа
        :param entity_type:
        :return:
        """
        return self.entities.get(entity_type, [])

    def get_entity_by_uri(self, uri):
        """
        Возвращает сущность по URI.
        :param uri:
        :return:
        """
        for entity_list in self.entities.values():
            for entity in entity_list:
                if entity.get_uri() == uri:
                    return entity
        return None

    def get_all_entities(self):
        """
        Возвращает все сущности в сцене
        :return entities_list -> list:
        """
        return self.entities.values()

    def remove_entity_by_uri(self, uri):
        """
        Удаляет сущность по URI.
        :param uri:
        :return:
        """
        for key in self.entities.keys():
            for entity in self.entities.get(key):
                if entity.get_uri() == uri:
                    self.entities.get(key).remove(entity)
                    return True
        return False
