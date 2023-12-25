"""Модуль игры"""
import pygame
import time
import matplotlib.pyplot as plt
import random
import importlib.resources
from src.scene.Scene import Scene
from src.utils.Export.Export import export_in_excel,data_in_game
from src.utils.statistics.Statistics import DataStatistics


class Game:

    def __init__(self, start_scene: Scene):
        """
        Запуск игры
        :param start_scene:
        :return:
        """
        MODULE_PATH = importlib.resources.files("assets")
        self.input_spdr_speed = 6
        # input_ant_speed = 3
        self.input_ant_power = 1500

        self.name = 'Game'

        self.text_for_settings = ''
        self.text_for_settings_inp = False
        self.text_event_enter = False
        self.text_event_back = False

        self.running = True
        self.pause = True
        self.moving = False
        self.intro = True
        self.settings = False
        self.menu_back = False
        self.mouse_clicked = False
        self.pause_agents = False
        self.graphics_isopen = False
        self.download_bot = False
        self.saveplt = False

        self.change_ant_speed = False
        self.change_spider_speed = False
        self.change_ant_power = False
        self.change_apple_weight = False
        self.change_list = [self.change_ant_speed, self.change_spider_speed, self.change_ant_power, self.change_apple_weight]

        self.lastcallback = time.time()
        self.total_seconds = 0.01
        self.sec_list = []
        self.spider_middle_energy_per_sec = []
        self.ant_middle_energy_per_sec = []
        self.anthill_middle_energy_per_sec = []
        self.already_shown = False

        self.scene = start_scene
        pygame.init()
        pygame.display.set_caption("ANTHILL")
        self.display_xy = (500, 500)
        self.display = pygame.display.set_mode(self.display_xy)
        self.intro_download = pygame.image.load(MODULE_PATH / "icons/intro_logo.png").convert_alpha()
        self.backgr_download = pygame.image.load(MODULE_PATH / "icons/backgr.png").convert_alpha()
        self.display.blit(pygame.transform.scale(self.backgr_download, (self.display.get_width(), self.display.get_height())), (0, 0))

    def save_graphics(self):
        data = DataStatistics.data
        export_in_excel(data)

    def show_graphics(self, pos, y_name, x_name='Номер тика'):
        self.already_shown = True
        data = DataStatistics.data
        data_in_game(data,y_name,x_name)

        self.display.blit(pygame.transform.scale(pygame.image.load(f"plot.png"),(500,500)).convert_alpha(),pos)

    def show_mas_graphic(self):
        tics = DataStatistics.data.get('Номер тика')
        num_of_messages = DataStatistics.data.get('Номер тика')  # FIXME: поменять
        self.display.blit(pygame.transform.scale(pygame.image.load(f"plot.png"), (500, 500)).convert_alpha(), (500, 500))

    def render_game(self):
        """
        Обновление игрового поля
        :return:
        """
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.pause = True

            if event.type == pygame.KEYUP and event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

            if event.type == pygame.KEYUP and event.key == pygame.K_q:
                self.pause = False

            if event.type == pygame.KEYUP and event.key in range(pygame.K_0, pygame.K_9 + 1):
                if self.text_for_settings == 'enter the number':
                    self.text_for_settings = ''
                self.text_for_settings += event.unicode

            if event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE:
                self.text_for_settings = self.text_for_settings[:len(self.text_for_settings) - 1]

            if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                self.text_event_enter = True


        #Графики
        if self.graphics_isopen:
            self.display.fill('white')

            self.pause = True
            self.settings = False
            self.intro = False


            self.show_graphics((0,0), 'Средние значения энергии всех муравьев')
            self.show_graphics((500,0), 'Средние значения энергии пауков')
            self.show_graphics((0,500), 'Значения энергии муравейника')
            self.show_graphics((500, 500), 'Количество сообщений в системе')


            #Кнопка back
            back_to_game = pygame.font.SysFont('MV Boli', 15).render("back", True, 'black')
            if back_to_game.get_rect(topleft=(0, 0)).collidepoint(mouse):
                self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render("back", True, 'black'),(0, 0))
                if pygame.mouse.get_pressed()[0]:
                    self.pause = False
                    self.graphics_isopen = False
                    self.display = pygame.display.set_mode((self.display_xy[0],self.display_xy[1]))
            else:
                self.display.blit(back_to_game, (0, 0))

            #Кнопка download to exel
            download_to_exel = pygame.font.SysFont('MV Boli', 15).render("download to exel", True, 'Black')
            if self.download_bot:
                if download_to_exel.get_rect(topleft = (0,25)).collidepoint(mouse):
                    self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render("download to exel", True, 'black'),(0,25))
                    if pygame.mouse.get_pressed()[0]:
                        self.save_graphics()
                else:
                    self.display.blit(download_to_exel,(0,25))

        #Игра
        if not self.pause:
            self.display.blit(pygame.transform.scale(self.backgr_download,(self.display_xy)),(0,0))

            #Кнопка меню
            menu = pygame.font.SysFont('MV Boli', 15).render("menu", True, 'Black')
            if menu.get_rect(topleft=(0, 0)).collidepoint(mouse):
                self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render("menu", True, 'black'),(0, 0))
                if pygame.mouse.get_pressed()[0]:
                    self.intro = True
                    self.pause = True
            else:
                self.display.blit(menu, (0, 0))

            #Кнопка settings
            sett = pygame.font.SysFont('MV Boli', 15).render("settings", True, 'Black')
            if sett.get_rect(topleft=(0, 25)).collidepoint(mouse):
                self.display.blit(pygame.font.SysFont('MV Boli', 15, bold='True', italic='True').render("settings", True, 'black'),(0, 25))
                if pygame.mouse.get_pressed()[0]:
                    self.intro = False
                    self.menu_back = True
                    self.settings = True
            else:
                self.display.blit(sett, (0, 25))

            #Кнопка graphics
            graphics = pygame.font.SysFont('MV Boli', 15).render("graphics", True, 'Black')
            if graphics.get_rect(topleft = (0,50)).collidepoint(mouse):
                self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render("graphics", True, 'black'),(0,50))
                if pygame.mouse.get_pressed()[0]:
                    if not self.graphics_isopen:
                        self.display = pygame.display.set_mode((self.display_xy[0]*2,self.display_xy[1]*2))
                        self.graphics_isopen = True
                        self.already_shown = True
                        self.download_bot = True

                    else:
                        self.display = pygame.display.set_mode(self.display_xy)
                        self.graphics_isopen = False
                        self.download_bot = False
            else:
                self.display.blit(graphics,(0,50))

            #Кнопка pause
            #Пауза странно работает
            pause_ingame = pygame.font.SysFont('MV Boli', 15).render("pause", True, 'Black')
            if pause_ingame.get_rect(topleft = (0,75)).collidepoint(mouse):
                self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render("pause", True, 'black'),(0,75))
                if pygame.mouse.get_pressed()[0]:
                    if self.pause_agents:
                        self.pause_agents = False
                    else:
                        self.pause_agents = True
            else:
                self.display.blit(pause_ingame,(0,75))

            #Кнопка exit
            exit_ingame = pygame.font.SysFont('MV Boli', 15).render("exit", True, 'Black')
            if exit_ingame.get_rect(topleft=(0, 100)).collidepoint(mouse):
                self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render("exit", True, 'black'),(0, 100))
                if pygame.mouse.get_pressed()[0]:
                    self.running = False
                    quit()
            else:
                self.display.blit(exit_ingame, (0, 100))

            for entities in self.scene.get_all_entities():
                if entities:
                    if entities[0].name != 'Group':
                        for entity in entities:
                            if not self.pause_agents:   #Причина плохой работы паузы тут скорее всего
                                entity.run()
                            self.display.blit(entity.body(), entity.geo)


        if self.settings:
            self.display.blit(pygame.transform.scale(self.intro_download, (self.display.get_width(), self.display.get_height())), (0, 0))
            if self.menu_back:
                back_to_menu = pygame.font.SysFont('MV Boli', 15).render("back", True,'Black')
                set_ant_power = pygame.font.SysFont('MV Boli', 15).render(f"ants power: {self.input_ant_power}", True, 'Black')
                set_spider_speed = pygame.font.SysFont('MV Boli', 15).render(f"spider speed: {self.input_spdr_speed}", True, 'Black')

                if back_to_menu.get_rect(topleft=(50, 0)).collidepoint(mouse):

                    self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render("back", True, 'black'),(50, 0))
                    if pygame.mouse.get_pressed()[0]:
                        for i in range(len(self.change_list)):
                            self.change_list[i] = False
                        self.text_event_back = True
                        self.intro = True
                        self.menu_back = False
                        self.settings = False
                else:
                    self.display.blit(back_to_menu, (50, 0))

                if set_spider_speed.get_rect(topleft=(50, 200)).collidepoint(mouse) and not self.change_spider_speed:
                    self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render(f"spider speed: {self.input_spdr_speed}", True, 'black'), (50, 200))
                    if pygame.mouse.get_pressed()[0] and not self.change_ant_speed and not self.change_ant_power and not self.change_apple_weight:
                        self.text_for_settings = 'enter the number'
                        self.change_spider_speed = True
                elif self.change_spider_speed:
                    self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render(f"spider speed: {self.input_spdr_speed}", True, 'black'), (50, 200))
                    if type(self.text_for_settings) != "enter the number":
                        input_spdr_speed = self.text_for_settings
                        if self.text_event_enter:
                            input_spdr_speed = int(input_spdr_speed)
                            for spider in self.spiders:
                                spider.speed = input_spdr_speed
                            self.change_spider_speed = False
                            self.text_event_enter = False
                    else:
                        self.input_spdr_speed = self.text_for_settings
                else:
                    self.display.blit(set_spider_speed, (50, 200))

                if set_ant_power.get_rect(topleft=(50, 175)).collidepoint(mouse) and not self.change_ant_power:
                    self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render(
                        f"ants power: {self.input_ant_power}", True, 'black'), (50, 175))
                    if pygame.mouse.get_pressed()[0
                        ] and not self.change_ant_speed and not self.change_spider_speed and not self.change_apple_weight:
                        self.text_for_settings = 'enter the number'
                        self.change_ant_power = True
                elif self.change_ant_power:
                    self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render(f"ants power: {self.input_ant_power}", True, 'black'), (50, 175))
                    if type(self.text_for_settings) != "enter the number":
                        input_ant_power = self.text_for_settings
                        if self.text_event_enter:
                            input_ant_power = int(input_ant_power)
                            if self.ants:
                                for ant in self.ants:
                                    ant.power = input_ant_power
                            self.change_ant_power = False
                            self.text_event_enter = False

                    else:
                        self.input_ant_power = self.text_for_settings
                else:
                    self.display.blit(set_ant_power, (50, 175))



        #Заствка
        if self.intro:
            self.display.blit(pygame.transform.scale(self.intro_download, (self.display.get_width(), self.display.get_height())), (0, 0))
            antvssp = pygame.font.SysFont('MV Boli', 25).render("ANTS VS SPIDERS", True,'Black')

            #Кнопка play
            run_game = pygame.font.SysFont('MV Boli', 15).render("play", True, 'Black')
            if run_game.get_rect(topleft=(0, 75)).collidepoint(mouse):
                self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render("play", True, 'black'),
                            (0, 75))
                if pygame.mouse.get_pressed()[0]:
                    self.intro = False
                    self.pause = False
            else:
                self.display.blit(run_game, (0, 75))

            #Кнопка settings
            sett = pygame.font.SysFont('MV Boli', 15).render("settings", True, 'Black')
            if sett.get_rect(topleft=(0, 100)).collidepoint(mouse):
                self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render("settings", True, 'black'),(0, 100))
                if pygame.mouse.get_pressed()[0]:
                    self.intro = False
                    self.menu_back = True
                    self.settings = True
            else:
                self.display.blit(sett, (0, 100))

            #Кнопка exit
            exit_from_game = pygame.font.SysFont('MV Boli', 15).render("exit", True, 'Black')
            if exit_from_game.get_rect(topleft=(0, 125)).collidepoint(mouse):
                self.display.blit(pygame.font.SysFont('MV Boli', 15,bold='True',italic='True').render("exit", True, 'black'),
                             (0, 125))
                if pygame.mouse.get_pressed()[0]:
                    quit()
            else:
                self.display.blit(exit_from_game, (0, 125))

            self.display.blit(antvssp, (0, 25))



            

        pygame.display.update()
        return self.pause


