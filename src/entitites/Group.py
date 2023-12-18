"""Реализация класса группы"""


class Group:
    def __init__(self, scene, id='0', aim=None, leader=None):
        self.name = __class__.__name__
        # в каждом классе определил переменную-имя класса
        # , чтобы агентам не надо было импортровать друг друга, чтобы не появлялась circular import error
        self.uri = self.name + str(id)
        self.scene = scene
        self.leader = leader
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