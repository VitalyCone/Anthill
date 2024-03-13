# """Модуль игры"""
# from copy import copy
#
# import time
# import matplotlib.pyplot as plt
# import random
# import importlib.resources
# from src.scene.Scene import Scene
# from src.utils.Export.Export import export_in_excel
# from src.utils.statistics.Statistics import DataStatistics
# from abc import ABC, abstractmethod
#
# class Game:
#
#     def __init__(self, start_scene: Scene):
#         """
#         Запуск игры
#         :param start_scene:
#         :return:
#         """
#         MODULE_PATH = importlib.resources.files("assets")
#         self.input_spdr_speed = 6
#         # input_ant_speed = 3
#         self.input_ant_energy = 1
#         self.input_spdr_energy = 1
#         self.input_ant_speed = 4
#
#         self.anim_x = -100
#         self.anim_num = 0
#         self.anim_num_past = 0
#         self.anim_count = 0
#
#         self.name = 'Game'
#
#         self.text_for_settings = ''
#         self.text_for_settings_inp = False
#         self.text_event_enter = False
#         self.text_event_back = False
#
#         self.running = True
#         self.pause = True
#         self.moving = False
#         self.intro = True
#         self.settings = False
#         self.menu_back = False
#         self.mouse_clicked = False
#         self.pause_agents = False
#         self.graphics_isopen = False
#         self.download_bot = False
#         self.saveplt = False
#
#         self.change_ant_speed = False
#         self.change_spider_speed = False
#         self.change_ant_power = False
#         self.change_apple_weight = False
#         self.change_list = [self.change_ant_speed, self.change_spider_speed, self.change_ant_power, self.change_apple_weight]
#
#         self.lastcallback = time.time()
#         self.total_seconds = 0.01
#         self.sec_list = []
#         self.spider_middle_energy_per_sec = []
#         self.ant_middle_energy_per_sec = []
#         self.anthill_middle_energy_per_sec = []
#         self.already_shown = False
#
#         self.scene = start_scene
#         pygame.init()
#         pygame.display.set_caption("ANTHILL")
#         self.display_xy = (500, 500)
#         self.display = pygame.display.set_mode(self.display_xy)
#         self.intro_download = pygame.image.load(MODULE_PATH / "icons/intro_logo.png").convert_alpha()
#         self.backgr_download = pygame.image.load(MODULE_PATH / "icons/backgr.png").convert_alpha()
#         self.anim_download = [
#             pygame.image.load(MODULE_PATH / "anim/1.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/2.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/3.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/4.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/5.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/6.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/7.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/8.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/9.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/10.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/11.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/12.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/13.png").convert_alpha(),
#             pygame.image.load(MODULE_PATH / "anim/14.png").convert_alpha(),
#             ]
#         self.display.blit(pygame.transform.scale(self.backgr_download, (self.display.get_width(), self.display.get_height())), (0, 0))
#
#     def save_graphics(self):
#         data = DataStatistics.data
#         export_in_excel(data)
#
#     def show_graphics(self, pos, y_name, x_name='Номер тика'):
#         self.already_shown = True
#         data = DataStatistics.data
#         # data_in_game(data, y_name, x_name)
#         self.display.blit(pygame.transform.scale(pygame.image.load(f"plot.png"),(500,500)).convert_alpha(),pos)
#
#     def show_mas_graphic(self):
#         tics = DataStatistics.data.get('Номер тика')
#         num_of_messages = DataStatistics.data.get('Номер тика')  # FIXME: поменять
#         self.display.blit(pygame.transform.scale(pygame.image.load(f"plot.png"), (500, 500)).convert_alpha(), (500, 500))
#
#     def render_game(self):
#         """
#         Обновление игрового поля
#         :return:
#         """
#         mouse = pygame.mouse.get_pos()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#                 quit()
#
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
#                 self.pause = True
#
#             if event.type == pygame.KEYUP and event.key == pygame.K_f:
#                 pygame.display.toggle_fullscreen()
#
#             if event.type == pygame.KEYUP and event.key == pygame.K_q:
#                 self.pause = False
#
#             if event.type == pygame.KEYUP and event.key in range(pygame.K_0, pygame.K_9 + 1):
#                 if self.text_for_settings == 'enter the number':
#                     self.text_for_settings = ''
#                 self.text_for_settings += event.unicode
#
#             if event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE:
#                 self.text_for_settings = self.text_for_settings[:len(self.text_for_settings) - 1]
#
#             if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
#                 self.text_event_enter = True
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if self.pauseButtonColision:
#                     self.pause_agents = not self.pause_agents #инвертировать состояние
#                 if self.menuButtonCollision:
#                     self.intro = True
#                     self.pause = True
#                     self.anim_x = -100
#                     self.anim_num = 0
#                     self.anim_num_past = 0
#                     self.anim_count = 0
#
#
#
#
#         #Графики
#         if self.graphics_isopen:
#             self.display.fill('white')
#
#             self.pause = True
#             self.settings = False
#             self.intro = False
#
#
#             self.show_graphics((0,0), 'Средние значения энергии всех муравьев')
#             self.show_graphics((500,0), 'Средние значения энергии пауков')
#             self.show_graphics((0,500), 'Значения энергии муравейника')
#             self.show_graphics((500, 500), 'Количество сообщений в системе')
#
#             #Кнопка back
#             back_to_game = pygame.font.SysFont('broadway', 15).render("back to menu", True, 'black')
#             if back_to_game.get_rect(topleft=(0, 0)).collidepoint(mouse):
#                 self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render("back to menu", True, 'black'),(0, 0))
#                 if pygame.mouse.get_pressed()[0]:
#                     self.graphics_isopen = False
#                     self.download_bot = False
#                     self.intro = True
#                     self.display = pygame.display.set_mode((self.display_xy[0],self.display_xy[1]))
#                     self.anim_x = -100
#                     self.anim_num = 0
#                     self.anim_num_past = 0
#                     self.anim_count = 0
#             else:
#                 self.display.blit(back_to_game, (0, 0))
#
#             #Кнопка download to export
#             download_to_exel = pygame.font.SysFont('broadway', 15).render("download to export", True, 'Black')
#             if self.download_bot:
#                 if download_to_exel.get_rect(topleft = (0,25)).collidepoint(mouse):
#                     self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render("download to export", True, 'black'),(0,25))
#                     if pygame.mouse.get_pressed()[0]:
#                         self.save_graphics()
#                 else:
#                     self.display.blit(download_to_exel,(0,25))
#
#         #Игра
#         if not self.pause:
#             self.display.blit(pygame.transform.scale(self.backgr_download,(self.display_xy)),(0,0))
#
#             #Кнопка меню
#             menu = pygame.font.SysFont('broadway', 15).render("menu", True, 'Black')
#             if menu.get_rect(topleft=(0, 0)).collidepoint(mouse):
#                 self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render("menu", True, 'black'),(0, 0))
#                 self.menuButtonCollision = True
#
#             else:
#                 self.menuButtonCollision = False
#                 self.display.blit(menu, (0, 0))
#
#             #Кнопка pause
#             #Пауза странно работает
#             pause_ingame = pygame.font.SysFont('broadway', 15).render("pause", True, 'Black')
#             if pause_ingame.get_rect(topleft = (0,25)).collidepoint(mouse):
#                 self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render("pause", True, 'black'),(0,25))
#                 self.pauseButtonColision = True
#             else:
#                 self.pauseButtonColision = False
#                 self.display.blit(pause_ingame,(0,25))
#
#             for entities in self.scene.get_all_entities():
#                 if entities:
#                     if entities[0].name != 'Group':
#                         for entity in entities:
#                             if not self.pause_agents:   #Причина плохой работы паузы тут скорее всего
#                                 entity.run()
#                             self.display.blit(entity.body(), entity.geo)
#
#
#         if self.settings:
#             self.pause_agents = True
#             self.display.blit(pygame.transform.scale(self.intro_download, (self.display.get_width(), self.display.get_height())), (0, 0))
#             if self.menu_back:
#                 back_to_menu = pygame.font.SysFont('broadway', 15).render("back", True,'Black')
#                 set_ant_power = pygame.font.SysFont('broadway', 15).render(f"ants energy: {self.input_ant_energy}", True, 'Black')
#                 set_ant_speed = pygame.font.SysFont('broadway', 15).render(f"ants speed: {self.input_ant_speed}", True,'Black')
#                 set_spider_energy = pygame.font.SysFont('broadway', 15).render(f"spiders energy: {self.input_spdr_energy}", True, 'Black')
#                 set_spider_speed = pygame.font.SysFont('broadway', 15).render(f"spider speed: {self.input_spdr_speed}", True, 'Black')
#
#                 if back_to_menu.get_rect(topleft=(50, 0)).collidepoint(mouse):
#
#                     self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render("back", True, 'black'),(50, 0))
#                     if pygame.mouse.get_pressed()[0]:
#                         for i in range(len(self.change_list)):
#                             self.change_list[i] = False
#                         self.text_event_back = True
#                         self.intro = True
#                         self.menu_back = False
#                         self.settings = False
#                         self.pause_agents = False
#                         self.anim_x = -100
#                         self.anim_num = 0
#                         self.anim_num_past = 0
#                         self.anim_count = 0
#                 else:
#                     self.display.blit(back_to_menu, (50, 0))
#
#                 if set_spider_speed.get_rect(topleft=(50, 200)).collidepoint(mouse) and not self.change_spider_speed:
#                     self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render(f"spider speed: {self.input_spdr_speed}", True, 'black'), (50, 200))
#                     if pygame.mouse.get_pressed()[0] and not self.change_ant_speed and not self.change_ant_power and not self.change_apple_weight:
#                         self.text_for_settings = 'enter the number'
#                         self.change_spider_speed = True
#                 elif self.change_spider_speed:
#                     self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render(f"spider speed: {self.input_spdr_speed}", True, 'black'), (50, 200))
#                     if type(self.text_for_settings) != "enter the number":
#                         input_spdr_speed = self.text_for_settings
#                         if self.text_event_enter:
#                             input_spdr_speed = int(input_spdr_speed)
#                             for spider in self.scene.get_entities_by_type('Spider'):
#                                 spider.speed = input_spdr_speed
#                             self.change_spider_speed = False
#                             self.text_event_enter = False
#                     else:
#                         self.input_spdr_speed = self.text_for_settings
#                 else:
#                     self.display.blit(set_spider_speed, (50, 200))
#
#                 if set_ant_speed.get_rect(topleft=(50, 175)).collidepoint(mouse) and not self.change_ant_power:
#                     self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render(
#                         f"ants speed: {self.input_ant_speed}", True, 'black'), (50, 175))
#                     if pygame.mouse.get_pressed()[0
#                         ] and not self.change_spider_speed:
#                         self.text_for_settings = 'enter the number'
#                         self.change_ant_speed = True
#                 elif self.change_ant_speed:
#                     self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render(f"ants speed: {self.input_ant_power}", True, 'black'), (50, 175))
#                     if type(self.text_for_settings) != "enter the number":
#                         input_ant_speed = self.text_for_settings
#                         if self.text_event_enter:
#                             input_ant_speed = int(input_ant_speed)
#                             if self.scene.entities:
#                                 for ant in self.scene.get_entities_by_type('Ant'):
#                                     ant.speed = input_ant_speed
#                             self.change_ant_power = False
#                             self.text_event_enter = False
#                     else:
#                         self.input_ant_speed = self.text_for_settings
#                 else:
#                     self.display.blit(set_ant_speed, (50, 175))
#
#                 if set_ant_power.get_rect(topleft=(50, 150)).collidepoint(mouse) and not self.change_ant_power:
#                     self.display.blit(pygame.font.SysFont('broadway', 15, bold='True', italic='True').render(
#                         f"ants energy: {self.input_ant_energy}", True, 'black'), (50, 150))
#                     if pygame.mouse.get_pressed()[0
#                     ] and not self.change_spider_speed:
#                         self.text_for_settings = 'enter the number'
#                         self.change_ant_speed = True
#                 elif self.change_ant_speed:
#                     self.display.blit(pygame.font.SysFont('broadway', 15, bold='True', italic='True').render(
#                         f"ants energy: {self.input_ant_energy}", True, 'black'), (50, 150))
#                     if type(self.text_for_settings) != "enter the number":
#                         input_ant_energy = self.text_for_settings
#                         if self.text_event_enter:
#                             input_ant_energy = int(input_ant_energy)
#                             if self.scene.entities:
#                                 for ant in self.scene.get_entities_by_type('Ant'):
#                                     ant.energy = input_ant_energy
#                             self.change_ant_power = False
#                             self.text_event_enter = False
#                     else:
#                         self.input_ant_energy = self.text_for_settings
#                 else:
#                     self.display.blit(set_ant_power, (50, 150))
#
#                 if set_spider_energy.get_rect(topleft=(50, 125)).collidepoint(mouse) and not self.change_ant_power:
#                     self.display.blit(pygame.font.SysFont('broadway', 15, bold='True', italic='True').render(
#                         f"spider energy: {self.input_spdr_speed}", True, 'black'), (50, 125))
#                     if pygame.mouse.get_pressed()[0
#                     ] and not self.change_spider_speed:
#                         self.text_for_settings = 'enter the number'
#                         self.change_ant_speed = True
#                 elif self.change_ant_speed:
#                     self.display.blit(pygame.font.SysFont('broadway', 15, bold='True', italic='True').render(
#                         f"spider energy: {self.input_spdr_speed}", True, 'black'), (50, 125))
#                     if type(self.text_for_settings) != "enter the number":
#                         input_spider_energy = self.text_for_settings
#                         if self.text_event_enter:
#                             input_spider_energy = int(input_spider_energy)
#                             if self.scene.entities:
#                                 for ant in self.scene.get_entities_by_type('Spider'):
#                                     ant.energy = input_spider_energy
#                             self.change_ant_power = False
#                             self.text_event_enter = False
#
#                     else:
#                         self.input_spdr_speed = self.text_for_settings
#                 else:
#                     self.display.blit(set_spider_energy, (50, 125))
#
#
#
#         #Заствка
#         if self.intro:
#             #self.display.blit(pygame.transform.scale(self.intro_download, (self.display.get_width(), self.display.get_height())), (0, 0))
#             self.display.fill('white')
#
#             #анимация в меню
#             self.display.blit(self.anim_download[self.anim_num],(self.anim_x,400))
#             if self.anim_x<400:
#                 self.anim_x+=0.5
#                 self.anim_count+=1
#                 if self.anim_count == 50:
#                     self.anim_num+=1
#                     self.anim_count = 0
#                 if self.anim_num == 9:
#                     self.anim_num = 0
#                 if self.anim_x>=400:
#                     self.anim_count = 0
#                     self.anim_num = 10
#                     self.anim_past = 9
#             else:
#                 self.anim_count+=1
#                 if self.anim_count == 50:
#                     if self.anim_num == 13 and self.anim_past == 12:
#                         self.anim_num=12
#                         self.anim_past=13
#                     elif self.anim_num == 12 and self.anim_past == 13:
#                         self.anim_num=11
#                         self.anim_past=12
#                     elif self.anim_num == 11 and self.anim_past == 12:
#                         self.anim_num=12
#                         self.anim_past=11
#                     elif self.anim_num == 12 and self.anim_past == 11:
#                         self.anim_num=13
#                         self.anim_past=12
#                     else:
#                         self.anim_num +=1
#                         self.anim_past +=1
#                     self.anim_count=0
#
#             # else:
#             #     self.anim_count_second+=1
#             #     self.anim_num = self.anim_num_second
#             #     if self.anim_num_second == 14 and self.anim_count_second == 50:
#             #         self.anim_num_second = 12
#             #     if self.anim_num_second == 50:
#             #         self.anim_num_second+=1
#             #         self.anim_num_second = 0
#
#
#
#             #Кнопка play
#             run_game = pygame.font.SysFont('broadway', 15).render("play", True, 'Black')
#             if run_game.get_rect(topleft=(self.display.get_width()/2-round((4*19.95)/4), 75)).collidepoint(mouse):
#                 self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render("play", True, 'black'),(self.display.get_width()/2-round((4*19.95)/4), 75))
#                 if pygame.mouse.get_pressed()[0]:
#                     self.intro = False
#                     self.pause = False
#             else:
#                 self.display.blit(run_game, (self.display.get_width()/2-round((4*19.95)/4), 75))
#
#             #Кнопка settings
#             sett = pygame.font.SysFont('broadway', 15).render("settings", True, 'Black')
#             if sett.get_rect(topleft=(self.display.get_width()/2-round((8*19.95)/4), 100)).collidepoint(mouse):
#                 self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render("settings", True, 'black'),(self.display.get_width()/2-round((8*19.95)/4),100))
#                 if pygame.mouse.get_pressed()[0]:
#                     self.intro = False
#                     self.menu_back = True
#                     self.settings = True
#             else:
#                 self.display.blit(sett, (self.display.get_width()/2-round((8*19.95)/4), 100))
#
#             #Кнопка graphics
#             graphics = pygame.font.SysFont('broadway', 15).render("graphics", True, 'Black')
#             if graphics.get_rect(topleft = (self.display.get_width()/2-round((8*19.95)/4),125)).collidepoint(mouse):
#                 self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render("graphics", True, 'black'),(self.display.get_width()/2-round((8*19.95)/4),125))
#                 if pygame.mouse.get_pressed()[0]:
#                     if not self.graphics_isopen:
#                         self.display = pygame.display.set_mode((self.display_xy[0]*2,self.display_xy[1]*2))
#                         self.graphics_isopen = True
#                         self.already_shown = True
#                         self.download_bot = True
#                         self.pause = True
#
#                     else:
#                         self.display = pygame.display.set_mode(self.display_xy)
#                         self.graphics_isopen = False
#                         self.download_bot = False
#             else:
#                 self.display.blit(graphics, (self.display.get_width()/2-round((8*19.95)/4),125))
#
#             #Кнопка exit
#             exit_from_game = pygame.font.SysFont('broadway', 15).render("exit", True, 'Black')
#             if exit_from_game.get_rect(topleft=(self.display.get_width()/2-round((4*19.95)/4), 150)).collidepoint(mouse):
#                 self.display.blit(pygame.font.SysFont('broadway', 15,bold='True',italic='True').render("exit", True, 'black'),(self.display.get_width()/2-round((4*19.95)/4), 150))
#                 if pygame.mouse.get_pressed()[0]:
#                     quit()
#             else:
#                 self.display.blit(exit_from_game, (self.display.get_width()/2-round((4*19.95)/4), 150))
#
#             antvssp = pygame.font.SysFont('broadway', 25).render("ANTS VS SPIDERS", True,'Black')
#             self.display.blit(antvssp, (self.display.get_width()/2-round((15*33.25)/4), 25))
#
#
#
#
#
#         pygame.display.update()
#         # if self.pause_agents or self.pause:
#         #     return True
#         # else:
#         #     return False
#         return False
#
#
