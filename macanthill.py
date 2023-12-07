import pygame
import time
import matplotlib.pyplot as plt
from agents.Spider import Spider
from agents.Ant import Ant
from agents.Anthill import Anthill
from agents.Apple import Apple

pygame.init()
display_xy = (500,500)
display = pygame.display.set_mode(display_xy)
pygame.display.set_caption("ANTHILL")
clock = pygame.time.Clock()


running = True
pause = True
moving = False
intro = True
settings = False
menu_back = False
mouse_clicked = False
pause_agents = False
graphics_isopen = False
download_bot = False

intro_download = pygame.image.load("icons/intro_logo.png").convert_alpha()
backgr_download = pygame.image.load("icons/backgr.png").convert_alpha()

input_apple_hp = 10000
input_anthills = 1
input_apple = 3  
input_spdr = 3 
input_ant = 100 
anthills = [Anthill(input_apple_hp, input_apple, 0) for i in range(input_anthills)]
apples = [Apple(anthills[0]) for i in range(input_apple)]
ants = [Ant(apples, anthills[0]) for i in range(input_ant)]
spiders = [Spider(ants + apples) for i in range(input_spdr)]

input_spdr_speed = spiders[0].speed
#input_ant_speed = 3
input_ant_power = 1500

anthills = set(anthills)
apples = set(apples)
ants = set(ants)
spiders = set(spiders)
end = pygame.font.Font(pygame.font.match_font('verdana'), size=100)

text_for_settings = ''
text_for_settings_inp = False
text_event_enter = False
text_event_back = False

change_ant_speed = False
change_spider_speed = False
change_ant_power = False
change_apple_weight = False
change_list = [change_ant_speed, change_spider_speed, change_ant_power, change_apple_weight]

lastcallback = time.time()
total_seconds = 0.01
sec_list = []
apple_show_speed = []


def modify_scene(scene):  # метод, обрабатывающий измененную сцену, после хода агента
    mapples = set()
    mants = set()
    mspiders = set()
    for agent in scene:
        if agent.name == 'Apple':
            mapples.add(agent)
        elif agent.name == 'Ant':
            mants.add(agent)
        elif agent.name == 'Spider':
            mspiders.add(agent)
    global apples
    global ants
    global spiders
    apples = mapples
    ants = mants
    spiders = mspiders


def save_graphics(filename,xy):


    x_values = xy[0]
    y_values = xy[1]
    plt.plot(x_values, y_values, marker='o', linestyle='-')

    plt.xlabel('time')
    plt.ylabel('middle apple mass')
    plt.title(f'{filename}')
    plt.savefig(f"graphics/{filename}.png")

def show_graphics(filename,coord,xy):
    save_graphics(filename,xy)
    display.blit(pygame.transform.scale(pygame.image.load(f"graphics/{filename}.png"),(500,300)).convert_alpha(),coord)
    #pass

def apples_middle_speed():
    global apples
    total = 0
    if apples:
        for apple in apples:
            total+=apple.speed
        total = total/len(apples)
        return str(total)[:str(total).find('.')+4]
    return total


while running:
    #print(len(sec_list),len(apple_show_speed))
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(len(ants))
            running = False
            quit()

        
        # if  event.type == pygame.MOUSEBUTTONDOWN:
        #     if anthill.rect.collidepoint(pygame.mouse.get_pos()):
        #         moving = True
        #         anthill.change_moving(moving)

        # elif  event.type == pygame.MOUSEBUTTONUP:
        #     moving = False
        #     anthill.change_moving(moving)
        #     print(f'x={anthill.rect.x}, y={anthill.rect.y}, w={anthill.rect.w}, h={anthill.rect.h}')
        #     print(f'left={anthill.rect.left}, top={anthill.rect.top}, right={anthill.rect.right}, bottom={anthill.rect.bottom}')
        #     print(f'center={anthill.rect.center}')

        # elif  event.type == pygame.MOUSEMOTION and moving:
        #     anthill.rect.move_ip(event.rel)
        #     print(11111)
        #     print(event.rel)
        

        # if moving:
        #     pygame.draw.rect(display, "Blue" ,anthill.body())

         
    
        # pygame.display.flip()


        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            # print(spiders[0].geo)
            # print(spiders[0].get_need(spiders[0].u))
            # print(pygame.mouse.get_pos())
            pause = True

        if event.type == pygame.KEYUP and event.key == pygame.K_f:
            pygame.display.toggle_fullscreen()

        if event.type == pygame.KEYUP and event.key == pygame.K_q:
            pause = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            for i in range(10):
                i = Ant()
                ants.add(i)
            pause = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            apples.append(Apple())
            for el in ants:
                el.isready = False
            list(anthills[0]).exit = False
            pause = False

        if event.type == pygame.KEYUP and event.key in range(pygame.K_0, pygame.K_9 + 1):
            if text_for_settings == 'enter the number':
                text_for_settings = ''
            text_for_settings+= event.unicode
        
        if event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE:
            text_for_settings = text_for_settings[:len(text_for_settings)-1]

        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            text_event_enter = True


    if intro:
        display.blit(pygame.transform.scale(intro_download,(display_xy)),(0,0))
        antvssp = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 25).render("ANTS VS SPIDERS", True, 'Black')
        run_game = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("play", True, 'Black')
        sett = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("settings", True, 'Black')
        exit_from_game = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("exit", True, 'Black')

        if run_game.get_rect(topleft = (0,75)).collidepoint(mouse):
            display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("play", True, 'White'),(0,75))
            if pygame.mouse.get_pressed()[0]:
                intro = False
                pause = False 
        else:
            display.blit(run_game,(0,75))
        
        if sett.get_rect(topleft = (0,100)).collidepoint(mouse):
            display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("settings", True, 'White'),(0,100))
            if pygame.mouse.get_pressed()[0]:
                intro = False
                menu_back = True
                settings = True
        else:
            display.blit(sett,(0,100))
        
        if exit_from_game.get_rect(topleft = (0,125)).collidepoint(mouse):
            display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("exit", True, 'White'),(0,125))
            if pygame.mouse.get_pressed()[0]:
                quit()
        else:
            display.blit(exit_from_game,(0,125))

        display.blit(antvssp,(0,25))


    if settings:
        display.blit(pygame.transform.scale(intro_download,(display_xy)),(0,0))
        if menu_back:
            back_to_menu = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("back", True, 'Black')
            #set_ant_speed = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 30).render(f"ants speed: {input_ant_speed}", True, 'Black')
            set_ant_power = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render(f"ants power: {input_ant_power}", True, 'Black')
            set_spider_speed = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render(f"spider speed: {input_spdr_speed}", True, 'Black')
            # set_apple_weight = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 30).render(f"apple weight: {input_apple_hp}", True, 'Black')

            if back_to_menu.get_rect(topleft = (50,0)).collidepoint(mouse):

                display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("back", True, 'White'),(50,0))
                if pygame.mouse.get_pressed()[0]:
                    for i in range(len(change_list)):
                        change_list[i] = False
                    text_event_back = True
                    intro = True
                    menu_back = False
                    settings = False
            else:
                display.blit(back_to_menu,(50,0))
            

            # if set_ant_speed.get_rect(topleft = (100,300)).collidepoint(mouse) and not change_ant_speed:
            #     display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 30).render(f"ants speed: {input_ant_speed}", True, 'White'),(100,300))
            #     if pygame.mouse.get_pressed()[0] and not change_spider_speed and not change_ant_power and not change_apple_weight:
            #         text_for_settings = 'enter the number'
            #         change_ant_speed = True
            # elif change_ant_speed:
            #     display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 30).render(f"ants speed: {input_ant_speed}", True, 'White'),(100,300))
            #     if type(text_for_settings) != "enter the number":
            #             input_ant_speed = text_for_settings
            #             if text_event_enter:
            #                 input_ant_speed = int(input_ant_speed)
            #                 if ants:
            #                     for ant in ants:
            #                         ant.speed = input_ant_speed
            #                 change_ant_speed = False
            #                 text_event_enter = False
            #     else:
            #         input_ant_speed = text_for_settings
            # else:
            #     display.blit(set_ant_speed,(100,300))
            

            if set_spider_speed.get_rect(topleft = (50,200)).collidepoint(mouse) and not change_spider_speed:
                display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render(f"spider speed: {input_spdr_speed}", True, 'White'),(50,200))
                if pygame.mouse.get_pressed()[0] and not change_ant_speed and not change_ant_power and not change_apple_weight:
                    text_for_settings = 'enter the number'
                    change_spider_speed = True
            elif change_spider_speed:
                display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render(f"spider speed: {input_spdr_speed}", True, 'White'),(50,200))
                if type(text_for_settings) != "enter the number":
                        input_spdr_speed = text_for_settings
                        if text_event_enter:
                            input_spdr_speed = int(input_spdr_speed)
                            for spider in spiders:
                                spider.speed = input_spdr_speed
                            change_spider_speed = False
                            text_event_enter = False
                else:
                    input_spdr_speed = text_for_settings
            else:
                display.blit(set_spider_speed,(50,200))
            

            if set_ant_power.get_rect(topleft = (50,175)).collidepoint(mouse) and not change_ant_power:
                display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render(f"ants power: {input_ant_power}", True, 'White'),(50,175))
                if pygame.mouse.get_pressed()[0] and not change_ant_speed and not change_spider_speed and not change_apple_weight:
                    text_for_settings = 'enter the number'
                    change_ant_power = True
            elif change_ant_power:
                display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render(f"ants power: {input_ant_power}", True, 'White'),(50,175))
                if type(text_for_settings) != "enter the number":
                        input_ant_power = text_for_settings
                        if text_event_enter:
                            input_ant_power = int(input_ant_power)
                            if ants:
                                for ant in ants:
                                    ant.power = input_ant_power
                            change_ant_power = False
                            text_event_enter = False
                        
                else:
                    input_ant_power = text_for_settings
            else:
                display.blit(set_ant_power,(50,175))

            # if set_apple_weight.get_rect(topleft = (100,450)).collidepoint(mouse) and not change_apple_weight:
            #     display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 30).render(f"apple weight: {input_apple_hp}", True, 'White'),(100,450))
            #     if pygame.mouse.get_pressed()[0] and not change_ant_speed and not change_spider_speed and not change_ant_power:
            #         text_for_settings = 'enter the number'
            #         change_apple_weight = True
            # elif change_apple_weight:
            #     display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 30).render(f"apple weight: {input_apple_hp}", True, 'White'),(100,450))
            #     if type(text_for_settings) != "enter the number":
            #         input_apple_hp = text_for_settings
            #         if text_event_enter:
            #             input_apple_hp = int(input_apple_hp)
            #             if apples:
            #                 for apple in apples:
            #                     apple.weight = input_apple_hp
            #             change_apple_weight = False
            #             text_event_enter = False
            #     else:
            #         input_apple_hp = text_for_settings
            # else:
            #     display.blit(set_apple_weight,(100,450))


    if not pause:
        if graphics_isopen:
            display.fill('white')
        display.blit(pygame.transform.scale(backgr_download,(display_xy)),(0,0))

        sett = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("settings", True, 'Black')
        menu = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("menu", True, 'Black')
        graphics = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("graphics", True, 'Black')
        download_to_exel = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("download to exel", True, 'Black')
        #pause_ingame = pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("pause", True, 'Black')

        if menu.get_rect(topleft = (0,0)).collidepoint(mouse):
            display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("menu", True, 'White'),(0,0))
            if pygame.mouse.get_pressed()[0]:
                intro = True
                pause = True
        else:
            display.blit(menu,(0,0))
        
        if sett.get_rect(topleft = (0,25)).collidepoint(mouse):
            display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("settings", True, 'White'),(0,25))
            if pygame.mouse.get_pressed()[0]:
                intro = False
                pause = True
                menu_back = True
                settings = True
        else:
            display.blit(sett,(0,25))
        
        if graphics.get_rect(topleft = (0,50)).collidepoint(mouse):
            display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("graphics", True, 'White'),(0,50))
            if pygame.mouse.get_pressed()[0]:
                if not graphics_isopen:
                    display = pygame.display.set_mode((display_xy[0]*2,display_xy[1]))
                    graphics_isopen = True
                    download_bot = True

                else:
                    display = pygame.display.set_mode(display_xy)
                    graphics_isopen = False
                    download_bot = False
        else:
            display.blit(graphics,(0,50))
        
        if download_bot:
            if download_to_exel.get_rect(topleft = (display_xy[0]*2-150,display_xy[1]-50)).collidepoint(mouse):
                display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("download to exel", True, 'green'),(display_xy[0]*2-150,display_xy[1]-50))
                if pygame.mouse.get_pressed()[0]:
                    plt.savefig("exel/grapgh.png")
            else:
                display.blit(download_to_exel,(display_xy[0]*2-150,display_xy[1]-50))

        
        if graphics_isopen:
            if apple:
                #sec_list.append(str(total_seconds)[:5])
                if len(sec_list)<5:
                    show_graphics('applegraph',(display_xy[0],0),(sec_list,apple_show_speed))
                else:
                    show_graphics('applegraph',(display_xy[0],0),(sec_list[:-5],apple_show_speed[:-5]))
        
        # if pause_ingame.get_rect(topleft = (0,50)).collidepoint(mouse):
        #     display.blit(pygame.font.Font(pygame.font.match_font('MV Boli'), size = 15).render("pause", True, 'White'),(0,50))
        #     if pygame.mouse.get_pressed()[0]:
        #         if pause_agents:
        #             pause_agents = False
        #         else:
        #             pause_agents = True
        # else:
        #     display.blit(sett,(0,50))

        for anthill_index, anthill in enumerate(anthills):
            scene = anthill.move(ants | spiders | apples | anthills)
            modify_scene(scene) 
            anthill.run()
            if anthill.body().get_rect(topleft = anthill.geo).collidepoint(mouse):
                if pygame.mouse.get_pressed()[0]:
                    anthill.geo = pygame.mouse.get_pos()
            display.blit(anthill.body(),anthill.geo)

        for ant_index, ant in enumerate(ants):
            scene = ant.move(ants | spiders | apples)  # теперь в параметрах, при ходе, каждому агенту передается сцена(массив из объектов-агентов)
            modify_scene(scene)  # изменение сцены, после хода агента                      #(добавить муравейник)
            ant.run()
            #pygame.draw.rect(display, 'Black', ant.body())
            display.blit(ant.body(),ant.geo)

        for spider_index, spider in enumerate(spiders):
            scene = spider.move(ants | spiders | apples)  # то же самое, что и в коде ходов муравьев
            modify_scene(scene)
            spider.run()
            #pygame.draw.rect(display, 'purple', spider.body())
            display.blit(spider.body(),spider.geo)

        for apple_index, apple in enumerate(apples):
            scene = apple.move(ants | spiders | apples)
            modify_scene(scene)
            apple.run()
            #pygame.draw.rect(display, 'red', apple.body())
            display.blit(apple.body(),apple.geo)

        if not apples:
            list(anthills)[0].exit = True
            win = end.render("THE ANTS WON", True, 'Black')
            display.blit(win, (50, 490))
            # if len([ant for ant in ants if ant.isready==True]) == len(ants):
        if not ants and apples:
            loose = end.render("SPIDERS WON", True, 'Black')
            display.blit(loose, (80, 490))
    #print(sec_list,apple_show_speed)
    seconds = int(str(total_seconds)[:str(total_seconds).find('.')])
    #print(seconds)
    if seconds not in sec_list:
        if seconds != '':
            sec_list.append(seconds)
            apple_show_speed.append(apples_middle_speed())

    total_seconds = time.time()-lastcallback
    pygame.display.update()
    clock.tick(50)
