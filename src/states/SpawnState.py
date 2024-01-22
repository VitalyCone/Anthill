from src.states.State import State


class SpawnState(State):
    
    def move(self, agent, bool=False):
        num = agent.energy/20
        if not bool:
            if agent.tic % 50 == 0:
                for i in range(int(num)):
                    if agent.ants:
                        ant = agent.agent.dispatcher.create_ant()
                    # FIXME: IndexError: list index out of range
                        agent.scene.append(ant)
        
        return agent.scene
