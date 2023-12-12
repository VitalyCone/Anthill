from states.State import State

class AttackState(State):
    def Attack(agent):
        """

        в качестве обозначения врагов можно либо с enemies, либо prey. 
        Но prey тогда придется передавать из класса определения состояния

        group можно сделать как списком, так и числом.
        в случае списка даже если убъет по факту кто-один, 
        то наносивший последний удар по факту распределит
        между всеми участниками энернию. а если делать их 
        эгоистами, то может получать всю энергию только тот,
        кто нанес последний удар.

        """

        agent.u_trig[0] = (agent.enemy_prey.geo[1] - agent.geo[1]) / agent.get_distance(agent.enemy_prey)
        agent.u_trig[1] = (agent.enemy_prey.geo[0] - agent.geo[0]) / agent.get_distance(agent.enemy_prey)
        if 5>agent.get_distance(agent.enemy_prey)>3:
            agent.enemy_prey.energy-=agent.damage
        elif agent.get_distance(agent.enemy_prey)<=3:
            agent.u_trig[0] = agent.math.sin(agent.math.pi + agent.math.asin((agent.enemy_prey[1] - agent.geo[1]) / agent.get_distance(agent.enemy_prey)))
            agent.u_trig[1] = agent.math.cos(agent.math.pi + agent.math.acos((agent.enemy_prey[0] - agent.geo[0]) / agent.get_distance(agent.enemy_prey)))
            agent.enemy_prey.energy-=agent.damage
            
        if agent.prey.energy<=0:
            for a in agent.group:
                a.energy+=(2/3)/len(agent.group)
        

