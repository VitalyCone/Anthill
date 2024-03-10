"""Содержит в себе класс состояния движения с группой"""
from src.states.State import State


class GroupState(State):
    """
    Класс состояния движения/пребывания в группе
    """

    def try_to_choose_prey(self):
        """
        Выбирает жертву
        """
        groups = self.agent.get_specific_entities(self.agent.scene, "Group")
        groups_preys = [group.aim for group in groups]
        preys = [agent for agent in self.agent.scene if agent.name in self.agent.group_preys]
        if len(preys) > 0:
            self.agent.prey = max(preys, key=lambda x: x.energy)
            if self.agent.prey in groups_preys:
                self.agent.group = groups[groups_preys.index(self.agent.prey)]
                self.agent.prey = None
                self.agent.agent.connect_to_group(self.agent.group.uri)
                # self.agent.group.entities.append(self.agent)
            else:
                self.agent.agent.create_group(self.agent.prey, self.agent)
                self.agent.prey = None

    def move(self, agent):
        """
        Ход, при котором агент группы ведут жертву к муравейнику
        :param agent:
        :return agent.scene: List
        """
        self.agent = agent

        if not self.agent.prey:
            self.try_to_choose_prey()

        if self.agent.prey and self.agent.prey.name in self.agent.group_preys:
            if self.agent.get_distance(self.agent.prey) >= self.agent.speed:

                self.agent.set_vector_to_object(self.agent.prey)
            else:
                self.agent.set_vector_to_object(self.agent.anthill)

                if self.agent.prey.speed == 0:
                    self.agent.prey = None
                    self.agent.group = None

            self.agent.set_u()

        return self.agent.scene
