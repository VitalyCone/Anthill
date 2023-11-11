from states.State import State


class SpawnState(State):
    
    def move(self, agent):
        num = agent.energy/10
        if agent.tic % 20 == 0:
            for i in range(int(num)):
                ant = list(agent.ants)[0].add_ant(agent.scene, agent)
                agent.scene.add(ant)
        return agent.scene