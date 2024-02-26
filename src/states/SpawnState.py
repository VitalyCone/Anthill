from src.states.State import State


class SpawnState(State):
    
    def move(self, agent, bool=True):
        num = agent.energy/20 + 1
        if not bool:
            if agent.tic > agent.spawn_gap:
                agent.tic = 0
                for i in range(int(num)):
                    if agent.ants:
                        ant = agent.agent.dispatcher.create_ant(agent)
                    # FIXME: IndexError: list index out of range
                        agent.scene.append(ant)
        
        return agent.scene
