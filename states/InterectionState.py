from states.State import State

class InterectionState(State):
    def move(self, agent):
        """
        if state[1] in self.anthill.get_apples(self.anthill.scene):
            try:
                state[1].geo = geo
                state[1].travelset.add(self)
                self.u = math.acos((self.anthill.geo[0] - geo[0]) / self.get_distance(self.anthill))
                self.usin = math.asin((self.anthill.geo[1] - geo[1]) / self.get_distance(self.anthill))
                self.u_trig[0] = (self.anthill.geo[1] - geo[1]) / self.get_distance(self.anthill)
                self.u_trig[1] = (self.anthill.geo[0] - geo[0]) / self.get_distance(self.anthill)
            except:
                f = 1
            self.scene = state[1].move(self.scene)
        elif self in state[1].travelset and state[1] not in apples:
            state[1].travelset.remove(self)
        """
        print("ВЗАИМОДЕЙСТВУЮ")
        try: 
            agent.food_pray.travelset.add(agent)
            agent.u_trig[0] = (agent.anthill.geo[1] - agent.food_pray.geo[1]) / agent.get_distance(agent.anthill)
            agent.u_trig[1] = (agent.anthill.geo[0] - agent.food_pray.geo[0]) / agent.get_distance(agent.anthill)
            agent.scene = agent.food_pray.move(agent.scene)
        except:
            try:
                agent.logging.info(f'Агент {agent.uri} взаимодействовал с агентом {agent.food_pray.uri} и это вызвало ошибку')
            except:
                agent.logging.info(f'Агент {agent.uri} взаимодействовал с несуществующим агентом')