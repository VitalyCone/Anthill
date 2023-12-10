from math import sqrt
import state as Status

class state_determination(Status):
    def __init__(self):
        pass

    def do(self, me, agents_preference, enemies=[],  friends=[]): #я, предпочитаемые агенты, враги и друзья
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
        if enemies!=[]:
            profit_attack = profit_attack() #вычисление выгоды от атаки(в группе или не в группе - высчитывается в фукнции)
            if profit_attack>=0:
                return "В АТАКУ"
            else:
                return "БЕЖИМ"
                
        elif agents_preference!=[]: 
            l = self.get_distance(me, agents_preference[0]) #расстояние агента до предпочитаемого агента
            profit = profit() #тут должна вычисляться выгода агента
            if profit > 0:
                if l <= agents_preference[0].r:
                    return "ВЗАИМОДЕЙСТВИЕ"
                else:
                    return "СТРЕМИТСЯ К НАЙДЕННОМУ АГЕНТУ"