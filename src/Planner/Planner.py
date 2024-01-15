from src.agents.AgentDispatcher import AgentDispatcher
from src.entitites.Ant import Ant
from src.entitites.Anthill import Anthill
from src.entitites.Apple import Apple
from src.entitites.Spider import Spider
from src.scene.Scene import Scene
from src.utils.statistics.Statistics import Denotations, count_id, null_uris


class Planner:
    def __init__(self, dispatcher: AgentDispatcher, scene: Scene,
                 anthill_num: int, apples_num: int, spdr_num: int, ants_num: int):
        self.dispatcher = dispatcher
        self.scene = scene
        self.anthill_num = anthill_num
        self.apples_num = apples_num
        self.spdr_num = spdr_num
        self.ants_num = ants_num

    def start_system(self):
        self.dispatcher.create_scene_agent(self.scene)
        for i in range(self.anthill_num):
            anthill = Anthill(0, count_id('anthill'))
            Denotations.uris['anthill'].append(anthill.uri)
            self.dispatcher.add_entity(anthill)
        # FIXME: Добавлять объекты сцены в инициализации, а не тут
        for i in range(self.apples_num):
            apple = Apple(self.scene.get_entities_by_type('Anthill')[0], count_id('apple'))
            Denotations.uris['apple'].append(apple.uri)
            self.dispatcher.add_entity(apple)
        for i in range(self.ants_num):
            ant = Ant(self.scene.get_entities_by_type('Apple'), self.scene.get_entities_by_type('Anthill')[0],
                      count_id('ant'))
            Denotations.uris['ant'].append(ant.uri)
            self.dispatcher.add_entity(ant)
        for i in range(self.spdr_num):
            spider = Spider(self.scene.get_entities_by_type('Spider') + self.scene.get_entities_by_type('Apple'),
                            count_id('spider'))
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
