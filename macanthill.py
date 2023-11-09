import pygame
import random
import math
import time
import datetime
from Spider import Spider
from Ant import Ant
from Anthill import Anthill
from Apple import Apple

"""
С опцией переноса яблок
"""

pygame.init()
display = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("ANTHILL")
clock = pygame.time.Clock()
running = True
pause = False

input_anthills = 1
input_apple = 15  # int(input('Введите количество яблок (~6): '))
input_apple_hp = 1000  # int(input('Введите количество жизней яблок (~1000): '))
anthills = [Anthill(input_apple_hp, input_apple, 0) for i in range(input_anthills)]
apples = [Apple(anthills[0]) for i in range(input_apple)]
input_ant = 100  # int(input('Введите количество муравьев (~300): '))
input_ant_speed = 3  # int(input('Введите скорость муравьев (~2): '))
ants = [Ant(apples, anthills[0]) for i in range(input_ant)]
input_spdr = 10  # int(input('Введите количество пауков (~3): '))
input_spdr_speed = 5  # int(input('Введите скорость пауков ~(3): '))
spiders = [Spider(ants + apples) for i in range(input_spdr)]
# pygame.display.toggle_fullscreen()
end = pygame.font.Font(pygame.font.match_font('verdana'), size=100)

lastcallback = time.time()


def modify_scene(scene):  # метод, обрабатывающий измененную сцену, после хода агента
    mapples = []
    mants = []
    mspiders = []
    for agent in scene:
        if agent.name == 'Apple':
            mapples.append(agent)
        elif agent.name == 'Ant':
            mants.append(agent)
        elif agent.name == 'Spider':
            mspiders.append(agent)
    global apples
    global ants
    global spiders
    apples = mapples
    ants = mants
    spiders = mspiders


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(len(ants))
            running = False
            quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            print(spiders[0].geo)
            print(spiders[0].get_need(spiders[0].u))
            pause = True

        if event.type == pygame.KEYUP and event.key == pygame.K_f:
            pygame.display.toggle_fullscreen()

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
            anthills[0].exit = False
            pause = False

    if not pause:
        display.fill((102, 255, 102))

        for anthill_index, anthill in enumerate(anthills):
            anthill_write = anthill.anth_font.render("Anthill", True, 'white')
            display.blit(anthill_write,(10,810))
            scene = anthill.move(ants+spiders+apples+anthills)
            modify_scene(scene)
            anthill.run()
            pygame.draw.rect(display, "Brown" ,anthill.body())

        for ant_index, ant in enumerate(ants):
            scene = ant.move(
                ants + spiders + apples)  # теперь в параметрах, при ходе, каждому агенту передается сцена(массив из объектов-агентов)
            modify_scene(scene)  # изменение сцены, после хода агента                      #(добавить муравейник)
            ant.run()
            pygame.draw.rect(display, 'Black', ant.body())

        for spider_index, spider in enumerate(spiders):
            scene = spider.move(ants + spiders + apples)  # то же самое, что и в коде ходов муравьев
            modify_scene(scene)
            spider.run()
            pygame.draw.rect(display, 'purple', spider.body())

        for apple_index, apple in enumerate(apples):
        #     scene = apple.move(scene)
        #     modify_scene(scene)
            pygame.draw.rect(display, 'red', apple.body())

        if not apples:
            anthills[0].exit = True
            win = end.render("THE ANTS WON", True, 'Black')
            display.blit(win, (50, 490))
            # if len([ant for ant in ants if ant.isready==True]) == len(ants):
        if not ants and apples:
            loose = end.render("SPIDERS WON", True, 'Black')
            display.blit(loose, (80, 490))

    pygame.display.update()
    clock.tick(10)
