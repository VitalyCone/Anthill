from src.states.State import State


class GrowthState(State):

    def move(self, agent):
        agent.scene.remove(agent)
        agent.height += (agent.energy - agent.last_energy)
        agent.long += (agent.energy - agent.last_energy)
        if agent.height < 20:
            agent.height = 20
        if agent.long < 20:
            agent.long = 20
        agent.last_energy = agent.energy 
        agent.scene.append(agent)
        return agent.scene
