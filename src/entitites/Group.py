"""Реализация класса группы"""


class Group:
    def __init__(self, scene, id='0', aim=None, leader=None):
        self.name = __class__.__name__
        self.uri = self.name + str(id)
        self.scene = scene
        self.version = 0
        self.leader = leader
        self.leader.group = self
        self.leader.prey = aim
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

    def update_scene(self, scene):
        self.scene = scene

    def get_attack_entities(self):
        entities_ready_attack = []
        for entity in self.entities:
            if (entity.get_distance(self.leader) <= entity.speed and not entity.attack
                    and self.aim.name == 'Spider'):
                entities_ready_attack.append(entity)
        return entities_ready_attack

    def move(self, scene):
        self.update_scene(scene)
        for entity in self.entities:
            if entity.status == 'dead':
                self.entities.remove(entity)
        entities_ready_attack = self.get_attack_entities()
        return entities_ready_attack




