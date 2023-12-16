from states.State import State

class RunawayState(State):
    def move(self, agent):
        print("УБЕГАЮ")
        agent.u_trig[0] = agent.math.sin(agent.math.pi + agent.math.asin((agent.enemy_prey[1] - agent.geo[1]) / agent.get_distance(agent.enemy_prey)))
        agent.u_trig[1] = agent.math.cos(agent.math.pi + agent.math.acos((agent.enemy_prey[0] - agent.geo[0]) / agent.get_distance(agent.enemy_prey)))