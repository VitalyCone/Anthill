import pygame
import random


"""
С опцией переноса яблок
"""

pygame.init()
display = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("ANTHILL")
clock = pygame.time.Clock()
running = True
pause = False



class Ant:
    def __init__(self):
        self.geo = [random.randint(10,990),random.randint(10,990)]  #[50,344]
        self.isready = False
        self.speed = input_ant_speed
        self.intravel = False
        self.power = 1500

    def body(self):
        return pygame.Rect(self.geo[0],self.geo[1],5,5)
    
    def die(self,ant):
        ants.remove(ant)

    def closest_apple(self):
        dl = sorted([[((abs(round(apl.geo[0]-self.geo[0])**2 + (apl.geo[1]-self.geo[1])**2)**0.5)),apl] for apl in apples],key=lambda x: x[0])
        if dl:
            return dl[0][1]

    def move(self):
        
        run = self.run_away_from_spiders()

        if run:
            my_apple = run[1]
        elif not anthill.exit:
            my_apple = self.closest_apple()
        else:
            my_apple = anthill

        if my_apple:
            distance = ((my_apple.geo[0]-self.geo[0])**2 + (my_apple.geo[1]-self.geo[1])**2)**0.5
            
            if distance <= 5:
                if type(my_apple) == Apple:
                    self.intravel = True
                    my_apple.travelset.add(self)
                    my_apple.move()
                    for apple in apples:
                        if apple!=my_apple and self in apple.travelset:
                            apple.travelset.remove(self)

                if type(my_apple) == Anthill:
                    self.isready = True
            try:
                vector = ((my_apple.geo[0]-self.geo[0])/distance,(my_apple.geo[1]-self.geo[1])/distance)
            except:
                vector = (0,0)

            if not run:
                self.geo[0]+=vector[0]*self.speed
                self.geo[1]+=vector[1]*self.speed

            else:
                self.geo[0]-=vector[0]*self.speed
                self.geo[1]-=vector[1]*self.speed

    def run_away_from_spiders(self):
        distance = [[((spider.geo[0]-self.geo[0])**2 + (spider.geo[1]-self.geo[1])**2)**0.5,spider] for spider in spiders]
        for el in distance:
            if el[0] < 100:
                if not self.isready:
                    return el
        return False
        

class Spider:
    def __init__(self):
        self.geo = [random.randint(10,990),random.randint(10,990)]
        self.speed = input_spdr_speed
        self.my_ant = None
        
    
    def body(self):
        return pygame.Rect(self.geo[0],self.geo[1],15,15)

    def move(self):
        self.my_ant = self.closest_ant()
        
        if self.my_ant:
            distance = ((self.my_ant.geo[0]-self.geo[0])**2 + (self.my_ant.geo[1]-self.geo[1])**2)**0.5

            if distance <= 10 and not self.my_ant.isready:
                self.my_ant.die(self.my_ant)

            try:
                vector = ((self.my_ant.geo[0]-self.geo[0])/distance,(self.my_ant.geo[1]-self.geo[1])/distance)
            except:
                vector = (0,0)

            self.geo[0]+=vector[0]*self.speed
            self.geo[1]+=vector[1]*self.speed
    
    def closest_ant(self):
        dl = sorted([[((abs(round(ant.geo[0]-self.geo[0])**2 + (ant.geo[1]-self.geo[1])**2)**0.5)),ant] for ant in ants if not ant.isready],key=lambda x: x[0])
        spiders_goals = [spider.my_ant for spider in spiders]
        if dl:
            if len(dl) >= len(spiders):
                for el in dl:
                    if el[1] not in spiders_goals:
                        if 0<el[1].geo[0]<1000 and 0<el[1].geo[1]<1000:
                            return el[1]
                    elif el[1] == self.my_ant:
                        return self.my_ant
            else:
                return dl[0][1]



class Apple:
    def __init__(self):
        self.geo = [random.randint(10,970),random.randint(10,970)]
        self.apl_font = pygame.font.Font(pygame.font.match_font('verdana'), 15)
        self.travelset = set()
        self.distance = ((anthill.geo[0]-self.geo[0])**2 + (anthill.geo[1]-self.geo[1])**2)**0.5
        self.weight = 15000
    
    def body(self):
        return pygame.Rect(self.geo[0],self.geo[1],30,30)

    def die(self,apple):
        apples.remove(apple)
    
    def find_travel_speed(self):
        quantity_ants = len(self.travelset)
        normal_speed = 3
        normal_weight = self.weight/ants[0].power
        floor1 = [self.distance,normal_speed]
        speed = normal_speed * quantity_ants / normal_weight
        return speed
    
    def move(self):
        distance = ((anthill.geo[0]-self.geo[0])**2 + (anthill.geo[1]-self.geo[1])**2)**0.5
        speed = self.find_travel_speed()

        try:
            vector = ((anthill.geo[0]-self.geo[0])/distance,(anthill.geo[1]-self.geo[1])/distance)
        except:
            vector = (0,0)
        
        if distance <= 5:
            apples.remove(self)

        self.geo[0]+=vector[0]*speed
        self.geo[1]+=vector[1]*speed



class Anthill:
    def __init__(self):
        self.body = pygame.Rect(0,800,200,200)
        self.anth_font = pygame.font.Font(pygame.font.match_font('verdana'), size = 30)
        self.exit = False
        self.geo = [200,800]


anthill = Anthill()
input_apple = 6#int(input('Введите количество яблок (~6): '))
input_apple_hp = 1000#int(input('Введите количество жизней яблок (~1000): '))
apples = [Apple() for i in range(input_apple)]
input_ant = 500#int(input('Введите количество муравьев (~300): '))
input_ant_speed = 3#int(input('Введите скорость муравьев (~2): '))
ants = [Ant() for i in range(input_ant)]
input_spdr = 5#int(input('Введите количество пауков (~3): '))
input_spdr_speed = 5#int(input('Введите скорость пауков ~(3): '))
spiders = [Spider() for i in range(input_spdr)]

end = pygame.font.Font(pygame.font.match_font('verdana'), size = 100)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(len(ants))
            running = False
            quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pause = True

        if event.type == pygame.KEYUP and event.key == pygame.K_q:
            pause = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            for i in range(10):
                i = Ant()
                ants.append(i)
            pause = False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            apples.append(Apple())
            for el in ants:
                el.isready = False
            anthill.exit = False
            pause = False

    if not pause:
        display.fill((102,255,102))    
        print(spiders[0].geo)

        pygame.draw.rect(display, (153,76,0), anthill.body)
        anthill_write = anthill.anth_font.render("Anthill", True, 'white')
        display.blit(anthill_write,(10,810)) 

        for ant_index, ant in enumerate(ants):
            ant.move()
            pygame.draw.rect(display, 'Black', ant.body())
        
        for spider_index, spider in enumerate(spiders):
            pygame.draw.rect(display, 'Brown', spider.body())
            spider.move()
                
        for apple_index, apple in enumerate(apples):
            pygame.draw.rect(display, 'Red', apple.body())
        
        if not apples:
            anthill.exit = True
            win = end.render("THE ANTS WON", True, 'Black')
            display.blit(win,(50,490))
            #if len([ant for ant in ants if ant.isready==True]) == len(ants):
        if not ants and apples:
            loose = end.render("SPIDERS WON", True, 'Black')
            display.blit(loose,(80,490))


        
    pygame.display.update()
    clock.tick(10)