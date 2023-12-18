from src.states.State import State


class SpawnState(State):
    
    def move(self, agent, bool=False):
        num = agent.energy/10
        if not bool:
            if agent.tic % 20 == 0:
                for i in range(int(num)):
                    ant = list(agent.ants)[0].add_ant(agent.scene, agent)
                    # FIXME: IndexError: list index out of range
                    agent.scene.append(ant)
        
        return agent.scene
