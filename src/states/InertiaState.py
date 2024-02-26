import math
from src.states.State import State


class InertiaState(State):

    def calculate_impulce(self):
        impulce = 0
        agent = self.agent
        i = []
        for other_agent in agent.scene:
            if agent != other_agent and other_agent.name == 'Ant' and agent.get_distance(other_agent) <= other_agent.speed:
                # ПЕРЕПИСАТЬ, чтобы никаких исключений, для пауков
                impulce += other_agent.weight*other_agent.speed
                i.append(other_agent)
        return [impulce, i]

    def move(self, agent):
        self.agent = agent
        f = self.calculate_impulce() 
        speed = f[0] / agent.weight
        agent.speed = speed
        if agent.ants:
            agent.u_trig = [(agent.ants[0].anthill.geo[1] - agent.geo[1])/agent.get_distance(agent.ants[0].anthill),
                            (agent.ants[0].anthill.geo[0] - agent.geo[0])/agent.get_distance(agent.ants[0].anthill)]
            agent.u = math.acos(agent.u_trig[1])  # Чтобы никаких муравейников!!! пусть летит в направлении муравьев!!!
            agent.scene.append(agent)

        return [agent.scene, f[1]]
        # Можно вообще взять и собирать проекции скорости на оси сразу
