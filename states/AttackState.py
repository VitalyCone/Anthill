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

        agent.prey.energy-=agent.damage
            
        if agent.prey.energy<=0:
            for a in agent.group:
                a.energy+=(2/3)/len(agent.group)
        

