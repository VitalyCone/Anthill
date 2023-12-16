import math
import random
from states.State import State

class SearchState(State):

    def get_angle(self):
        trig = self.agent.u_trig
        u = math.acos(trig[1])
        if u == math.asin(trig[0]):
            return u                #функция получает массив[синус, косинус] и находит угол, учитывая 
        else:       
            u += math.pi
            return u
        
    def get_geo(self, u):
        agent = self.agent
        return [agent.geo[0] + agent.speed * math.cos(u), agent.geo[1] + agent.speed * math.sin(u)]
        
    def get_k_friends(self, u):
        geo = self.get_geo(u)
        for agent in self.agent.scene:
            if agent.name in self.agent.friends and (abs(geo[0] - agent.geo[0]) <= agent.r) and (abs(geo[0] - agent.geo[0]) <= agent.r):
                return 1
        return 0

    def get_k_enemies(self, u):
        geo = self.get_geo(u)
        for agent in self.agent.scene:
            if agent.name in self.agent.enemies and agent != self.agent and (abs(geo[0] - agent.geo[0]) <= agent.r) and (abs(geo[0] - agent.geo[0]) <= agent.r):
                return 1
        return 0
    
    def get_k_preys(self, u):
        geo = self.get_geo(u)
        for agent in self.agent.scene:
            if agent.name in self.agent.preys and (abs(geo[0] - agent.geo[0]) <= agent.r) and (abs(geo[0] - agent.geo[0]) <= agent.r):
                return 1
        return 0
    
    def get_k_error(self, u):
        if abs(self.agent.u - u) <= self.agent.error:
            return 1
        return 0             
    
    def get_k_in_scope(self, u):
        geo = self.get_geo(u)
        if (geo[0] > 10 and geo[0] < 490) and (geo[1] > 10 and geo[1] < 490):
            return 1
        return 0

    def move(self, agent):
        u = 0
        i = 0
        odds = []
        while u < 2*math.pi and u >= 0:
            k_friend = self.get_k_friends(u)  #высчитывает коэфициент союзников, по заданному направлению
            k_enemy = self.get_k_enemies(u)    #высчитывает коэфициент врагов/конкурентов, по заданному направлению
            k_prey = self.get_k_preys(u)    #высчитывыет коэфициент жертвы, по заданному направлению
            k_error = self.get_k_error(u)   #высчитывает коэфициент блуждания
            k_in_scope = self.get_k_in_scope(u) #высчитывыет коэфициент нахождения внутри экрана
            weights = agent.weights
            k = k_friend*weights[0] + k_enemy*weights[1] + k_prey*weights[2] + k_error*weights[3] + k_in_scope*weights[4]
            odds.append([k, u])
            u +=0.01      #перебор угла, имитирующий как существо осматривается
            i += 1
        best_odds = []
        best_odds.append(odds[0])
        for odd in odds:
            if odd[0] > best_odds[0][0]:
                best_odds.clear()
                best_odds.append(odd)
            elif odd[0] == best_odds[0][0]:
                best_odds.append(odd)
        u = random.choice(best_odds)[1]
        
        return u

