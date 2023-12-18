from src.states.State import State

class GrowthState(State):

    def move(self, agent):
        agent.scene.remove(agent)
        agent.height += (agent.energy - agent.last_energy)*10
        agent.long += (agent.energy - agent.last_energy)*10
        agent.last_energy = agent.energy 
        agent.scene.append(agent)
        return agent.scene