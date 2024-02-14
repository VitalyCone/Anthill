"""Реализация класса группы"""
from src.utils.statistics.Statistics import all_update, debug_update


class Group:
    def __init__(self, scene, id='0', aim=None, leader=None):
        self.name = __class__.__name__
        # в каждом классе определил переменную-имя класса
        # , чтобы агентам не надо было импортровать друг друга, чтобы не появлялась circular import error
        self.uri = self.name + str(id)
        self.scene = scene
        self.leader = leader
        leader.group = self
        self.agent = None
        self.aim = aim
        self.r = leader.r
        self.geo = leader.geo
        self.entities = [leader]

    def get_uri(self):
        """
        :return: uri
        """
        return self.uri

    def get_ants(self, scene):
        """
        :return: list of ants
        """
        ants = []
        for ant in scene:
            if ant.name == 'Ant':
                ants.append(ant)
        return ants

    def make_damage(self):
        if self.aim.name == 'Spider':
            num_of_entities = 0
            for entity in self.entities:
                if entity.attack and entity.get_distance(self.aim) <= 20:
                    num_of_entities += 1
            self.aim.energy -= num_of_entities*self.leader.damage
            if self.aim.energy <= 0:
                self.aim.die()
                self.agent.kill_aim()
