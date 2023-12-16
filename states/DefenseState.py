from states.State import State

class DefenseState(State):
    def move(self, agent):
        if agent.defense_prey.uri == agent.anthill.uri:

            """

            Если сущность идет к своей матке, то она идет напрямую.
            Если же к чужой, например, или к соплеменнику,
            то лишь примерно знает, откуда зовет.

            """
            print("ЗАЩИЩАЮ")
            if agent.get_distance(agent.defense_prey)<=10:
                agent.attackState(agent)
            else:
                agent.u_trig[0] = (agent.anthill.geo[1] - agent.geo[1]) / agent.get_distance(agent.anthill)
                agent.u_trig[1] = (agent.anthill.geo[0] - agent.geo[0]) / agent.get_distance(agent.anthill)
            
            