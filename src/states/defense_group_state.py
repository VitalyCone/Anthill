"""Содержит в себе класс состояния защиты группы"""
from src.entitites import BaseEntity
from src.states.State import State


class DefenseGroupState(State):
    """
    Класс состояния групповой защиты
    """

    def try_to_choose_prey(self):
        """
        Выбирает жертву
        """
        groups = self.agent.get_specific_entities(self.agent.scene, "Group")
        preys = [agent for agent in self.agent.scene if agent.name in self.agent.defensible_enemies]
        # if len(spider_groups) > 0:
        #     best_group = max(spider_groups, key=lambda x: x.aim.energy)
        #     self.group = best_group
        #     self.group.entities.append(self)
        #     return best_group.aim
        if len(preys) > 0:
            self.agent.prey = max(preys, key=lambda x: x.energy)
            self.agent.agent.create_group(self.agent.prey, self.agent)

    def move(self, agent):
        """
        Ход, при котором агент следует за лидером группы или выбирает местоположение сам являясь таковым
        :param agent:
        :return agent.scene: List
        """
        self.agent = agent

        if not self.agent.prey:
            self.try_to_choose_prey()

        if self.agent.prey and self.agent.prey.name in self.agent.defensible_enemies:
            self.agent.set_vector_to_object(self.agent.prey)
            if not self.agent.attack:
                if self == self.agent.group.leader:
                    self.agent.u_trig[0] = -self.agent.u_trig[0]
                    self.agent.u_trig[1] = -self.agent.u_trig[1]
                else:
                    self.agent.set_vector_to_object(self.agent.group.leader)
            else:
                self.agent.set_vector_to_object(self.agent.prey)

            self.agent.set_u()

        return self.agent.scene