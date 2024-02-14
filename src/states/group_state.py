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
        preys = [agent for agent in self.agent.scene if agent.name in self.agent.group_preys]
        # elif len(apple_groups) > 0:
        #     best_group = max(apple_groups, key=lambda x: x.aim.energy)
        #     self.group = best_group
        #     self.group.entities.append(self)
        #     return best_group.aim
        if len(preys) > 0:
            self.agent.prey = max(preys, key=lambda x: x.energy)
            self.agent.agent.create_group(self.agent.prey, self.agent)

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

            self.agent.set_u()

        return self.agent.scene
