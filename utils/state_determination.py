from math import sqrt

class state_determination:
    def __init__(self):
        pass

    def get_distance(agent1, agent2):  # возвращает информацию о расстоянии до обьекта при помощи любимой теоремы Пифагора
        return sqrt((agent1.geo[0] - agent2.geo[0]) ** 2 + (agent1.geo[1] - agent2.geo[1]) ** 2)

    def do(self, agent, enemies=[], friends=[], food_preys=[]): #я, предпочитаемые агенты, враги и друзья
        """

        это пока наброски, не обращайте внимания

        я думаю сделать несколько коэф. для эффективной работы определителя состояний
        во первых,

        у агентов заказчиков
            collectivism, где 0 - совершенные индивидуалисты, а 1 - совершенные коллективисты
            k, обозначающий 1/кол-во friends для убийства одного enemy
        у агентов ресурсов
            m - способность к передвижению
        """
        #сюда передается массив предпочитаемых агентов уже отсортированных по дальности
        #а также только тех, которых агент видит
        # if enemies!=[]:
        #     profit_attack = profit_attack() #вычисление выгоды от атаки(в группе или не в группе - высчитывается в фукнции)
        #     if profit_attack>=0:
        #         return "В АТАКУ"
        #     else:
        #         return "БЕЖИМ"
                
        # elif agents_preference!=[]: 
        #     l = self.get_distance(me, agents_preference[0]) #расстояние агента до предпочитаемого агента
        #     profit = profit() #тут должна вычисляться выгода агента
        #     if profit > 0:
        #         if l <= agents_preference[0].r:
        #             return "ВЗАИМОДЕЙСТВИЕ"
        #         else:
        #             return "СТРЕМИТСЯ К НАЙДЕННОМУ АГЕНТУ"
        st = []
        if len(friends)*agent.k>=len(enemies) and len(enemies)!=0: st.append([0, enemies[0].energy/(len(friends)+1)])
        if agent.anthill.help==1: st.append([1, 10000])
        if agent.prey != agent.enemy:
            if len(food_preys)!=0 and len(enemies)==0: 
                most_food = food_preys[0]
                speed = most_food.speed + 0.000000000000001
                if len(most_food.my_ants)!=0:
                    their_profit = (most_food.energy/10)/len() - agent.get_distance(agent.anthill)/speed*agent.energy_consumption
                else: 
                    their_profit = 0
                # Если они толкают без меня!!!
                new_speed = (most_food.speed*most_food.weight + agent.speed*agent.weight)/most_food.weight
                our_profit = (most_food.energy/10)/(len(agent)+1) - agent.get_distance(agent.anthill)/new_speed*agent.energy_consumption #Если они толкали со мной
                e = our_profit - their_profit
                st.append([2, e])
        if len(friends)*agent.k<len(enemies) and len(enemies)!=0: st.append([3, 0.125])
        if len(enemies)==0 and len(most_food)==0: st.append([4, 0])
        return st