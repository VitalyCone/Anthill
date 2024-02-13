"""Содержит в себе класс состояния охоты"""
from src.states.State import State


class HuntState(State):
    """
    Класс состояния охоты
    """

    @staticmethod
    def get_best_ant(agent):
        best_ant = agent.ants[0]
        for ant in agent.ants:  # каждый ход охоты идет проверка, точно ли выбранный муравей - лучший.
            if agent.get_energy(ant) > agent.get_energy(
                    best_ant):
                best_ant = ant
        return best_ant

    def move(self, agent):
        """
        Ход, при котором паук осматривается и выбирает себе жертву и направление к ней
        :param agent:
        :return agent.scene: List
        """

        agent.prey = agent.get_best_ant()  # Выбор лучшей жертвы
        agent.set_vector_to_object(agent.prey)  # Выбор направления до жертвы

        agent.try_give_in_prey()  # Если есть соперник, кому выгоднее данная жертва - уступает

        return agent.scene
