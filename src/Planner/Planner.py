from src.agents.AgentDispatcher import AgentDispatcher
from src.entitites.Ant import Ant
from src.entitites.Anthill import Anthill
from src.entitites.Apple import Apple
from src.entitites.Spider import Spider
from src.scene.Scene import Scene
from src.utils.ontology_utils.ontology_utils import OntologyModel
from src.utils.statistics.Statistics import Denotations, count_id, null_uris


class Planner:
    def __init__(self, dispatcher: AgentDispatcher, scene: Scene,
                 anthill_num: int, apples_num: int, spdr_num: int, ants_num: int, entities_settings: dict):
        self.dispatcher = dispatcher
        self.scene = scene
        self.anthill_num = anthill_num
        self.apples_num = apples_num
        self.spdr_num = spdr_num
        self.ants_num = ants_num
        self.entities_settings = entities_settings

    def start_system_with_onto_model(self):
        """
        """
        self.dispatcher.create_scene_agent(self.scene)
        ants = OntologyModel.ontology_model["Ant"]
        spiders = OntologyModel.ontology_model["Spider"]
        apples = OntologyModel.ontology_model["Apple"]
        anthills = OntologyModel.ontology_model["Anthill"]
        self.import_anthills(anthills)
        self.import_ants(ants)
        self.import_spiders(spiders)
        self.import_apples(apples)

    def import_apples(self, apples):
        for apple_dict in apples:
            uri = apple_dict['data']['label']['value']
            geo = [int(x) for x in str(apple_dict['data']['Geoposition']['value']).split(', ')]
            energy_cons = apple_dict['data']['EnergyConsumption']['value']
            energy = apple_dict['data']['Energy']['value']
            speed = apple_dict['data']['MovementSpeed']['value']
            weight = apple_dict['data']['Weight']['value']
            apple = Apple(uri)
            apple.energy = energy
            apple.energy_consumption = energy_cons
            apple.speed = speed
            apple.geo = geo
            apple.weight = weight
            Denotations.uris['apple'].append(apple.uri)
            self.dispatcher.add_entity(apple)

    def import_spiders(self, spiders):
        for spider_dict in spiders:
            uri = spider_dict['data']['label']['value']
            geo = [int(x) for x in str(spider_dict['data']['Geoposition']['value']).split(', ')]
            energy_cons = spider_dict['data']['EnergyConsumption']['value']
            energy = spider_dict['data']['Energy']['value']
            speed = spider_dict['data']['MovementSpeed']['value']
            spider = Spider(uri)
            spider.r = self.entities_settings["Spider"]["radius"]
            spider.speed = speed
            spider.geo = geo
            spider.energy_consumption = energy_cons
            spider.energy = energy
            Denotations.uris['spider'].append(spider.uri)
            self.dispatcher.add_entity(spider)

    def import_anthills(self, anthills):
        for anthill_dict in anthills:
            uri = anthill_dict['data']['label']['value']
            geo = [int(x) for x in str(anthill_dict['data']['Geoposition']['value']).split(', ')]
            energy_cons = anthill_dict['data']['EnergyConsumption']['value']
            energy = anthill_dict['data']['Energy']['value']
            anthill = Anthill(uri)
            anthill.geo = geo
            anthill.energy_consumption = energy_cons
            anthill.energy = energy
            Denotations.uris['anthill'].append(anthill.uri)
            self.dispatcher.add_entity(anthill)

    def import_ants(self, ants):
        for ant_dict in ants:
            uri = ant_dict['data']['label']['value']
            geo = [int(x) for x in str(ant_dict['data']['Geoposition']['value']).split(', ')]
            energy_cons = ant_dict['data']['EnergyConsumption']['value']
            energy = ant_dict['data']['Energy']['value']
            weight = ant_dict['data']['Weight']['value']
            speed = ant_dict['data']['MovementSpeed']['value']
            anthill = self.scene.get_entity_by_uri(ant_dict['data']['LivingIn']['value']['label'])
            ant = Ant(anthill,
                      uri)
            ant.r = self.entities_settings["Ant"]["radius"]
            ant.speed = speed
            ant.weight = weight
            ant.energy = energy
            ant.energy_consumption = energy_cons
            ant.geo = geo
            Denotations.uris['ant'].append(ant.uri)
            self.dispatcher.add_entity(ant)

    def start_system(self):
        self.dispatcher.create_scene_agent(self.scene)
        for i in range(self.anthill_num):
            anthill = Anthill("Anthill" + str(count_id('anthill')))
            Denotations.uris['anthill'].append(anthill.uri)
            self.dispatcher.add_entity(anthill)
        # FIXME: Добавлять объекты сцены в инициализации, а не тут
        for i in range(self.apples_num):
            apple = Apple(count_id('apple'))
            Denotations.uris['apple'].append(apple.uri)
            self.dispatcher.add_entity(apple)
        for i in range(self.ants_num):
            ant = Ant(self.scene.get_entities_by_type('Anthill')[0],
                      count_id('ant'))
            ant.r = self.entities_settings["Ant"]["radius"]
            ant.speed = self.entities_settings["Ant"]["speed"]
            Denotations.uris['ant'].append(ant.uri)
            self.dispatcher.add_entity(ant)
        for i in range(self.spdr_num):
            spider = Spider(count_id('spider'))
            spider.r = self.entities_settings["Spider"]["radius"]
            spider.speed = self.entities_settings["Spider"]["speed"]
            Denotations.uris['spider'].append(spider.uri)
            self.dispatcher.add_entity(spider)

    def set_start_nums(self, anthill_num: int, apples_num: int, spdr_num: int, ants_num: int):
        self.anthill_num = anthill_num
        self.apples_num = apples_num
        self.spdr_num = spdr_num
        self.ants_num = ants_num

    def remove_all_data(self):
        self.scene.remove_all_entities()
        self.dispatcher.reference_book.clear_reference_book()
        null_uris()
