from math import sqrt, abs, pow

class Status:
    def __init__(self):
        pass

    def get_distance(agent1, agent2):  # возвращает информацию о расстоянии до обьекта при помощи любимой теоремы Пифагора
        return sqrt((agent1.geo[0] - agent2.geo[0]) ** 2 + (agent1.geo[1] - agent2.geo[1]) ** 2)
    
   


    