from dataclasses import dataclass

from PySide6.QtWidgets import QDialog, QDialogButtonBox

from OntologyManager.OntologyManager import OntologyManager
from src.UI.forms.SimpleDiag import SimpleDiag
from src.UI.windows.ui_simple_dialog import Ui_SimpleDiag


@dataclass
class OntologyModel:
    ontology_model = None


def import_ontology_model():
    """
    Импортирует онтологию из СУЗ,
    обновляя данные в dataclass OntologyModel -
    создает dict с параметрами каждой сущности
    """
    onto_manager = OntologyManager()
    spiders = onto_manager.get_spiders()
    anthills = onto_manager.get_anthills()
    ants = onto_manager.get_ants()
    apples = onto_manager.get_apples()
    OntologyModel.ontology_model = {
        "Ant": ants,
        "Spider": spiders,
        "Apple": apples,
        "Anthill": anthills
    }
    simple_diag = SimpleDiag("Ontology model " + onto_manager.ontology_uri + " successfully imported")


def form_anthill_dict(anthill):
    """
    Создает dict муравейника для экспорта модели
    :param anthill: Anthill
    :return anthill_dict: dict
    """
    anthill_dict = {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Anthill",
        "label": anthill.uri,
        "Weight": anthill.weight,
        "Geoposition": ", ".join(str(geo) for geo in anthill.geo),
        "Energy": anthill.energy,
        "MovementSpeed": anthill.speed,
        "EnergyConsumption": anthill.energy_consumption
    }
    return anthill_dict


def form_spider_dict(spider):
    """
    Создает dict паука для экспорта модели
    :param spider: Spider
    :return spider_dict: dict
    """
    spider_dict = {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Spider",
        "label": spider.uri,
        "Weight": spider.weight,
        "Geoposition": ", ".join(str(geo) for geo in spider.geo),
        "Energy": spider.energy,
        "MovementSpeed": spider.speed,
        "EnergyConsumption": spider.energy_consumption,
        "VisionRadius": spider.r
    }
    return spider_dict


def form_apple_dict(apple):
    """
    Создает dict яблока для экспорта модели
    :param apple: Apple
    :return apple_dict: dict
    """
    apple_dict = {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Apple",
        "label": apple.uri,
        "Weight": apple.weight,
        "Geoposition": ", ".join(str(geo) for geo in apple.geo),
        "Energy": apple.energy,
        "MovementSpeed": apple.speed,
        "EnergyConsumption": apple.energy_consumption
    }
    return apple_dict


def form_ant_dict(ant):
    """
    Создает dict муравья для экспорта модели
    :param ant: Ant
    :return ant_dict: dict
    """
    ant_dict = {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Ant",
        "label": ant.uri,
        "Weight": ant.weight,
        "Geoposition": ", ".join(str(geo) for geo in ant.geo),
        "Energy": ant.energy,
        "MovementSpeed": ant.speed,
        "EnergyConsumption": ant.energy_consumption,
        "VisionRadius": ant.r,
        "LivingIn":
            {
                "uri": "http://www.kg.ru/ants_versus_spiders_v2#Anthill",
                "label": ant.anthill.uri
            }
    }
    return ant_dict


def export_ontology_model(scene):
    """
    Экспортирует текущие параметры игры в СУЗ модели игры Ants vs Spiders
    :param scene:
    """
    onto_manager = OntologyManager()

    ants = scene.get_entities_by_type("Ant")
    anthills = scene.get_entities_by_type("Anthill")
    spiders = scene.get_entities_by_type("Spider")
    apples = scene.get_entities_by_type("Apple")

    anthill_responces = [onto_manager.create_anthill(form_anthill_dict(anthill)) for anthill in anthills]
    apple_responces = [onto_manager.create_apple(form_apple_dict(apple)) for apple in apples]
    spider_responces = [onto_manager.create_spider(form_spider_dict(spider)) for spider in spiders]
    ant_responces = [onto_manager.create_ant(form_ant_dict(ant)) for ant in ants]

    simple_diag = SimpleDiag("Ontology model successfully exported to model: " + onto_manager.ontology_uri)
