"""Модуль игры"""
import pygame

from agents.Scene.Scene import Scene


class Game:

    def __init__(self, start_scene: Scene):
        """
        Запуск игры
        :param start_scene:
        :return:
        """
        self.scene = start_scene
        pygame.init()
        pygame.display.set_caption("ANTHILL")
        display_xy = (500, 500)
        self.display = pygame.display.set_mode(display_xy)
        self.intro_download = pygame.image.load("icons/intro_logo.png").convert_alpha()
        self.backgr_download = pygame.image.load("icons/backgr.png").convert_alpha()
        self.display.blit(pygame.transform.scale(self.backgr_download, (self.display.get_width(), self.display.get_height())), (0, 0))

    def render_game(self):
        """
        Обновление игрового поля
        :return:
        """
        self.display.blit(pygame.transform.scale(self.backgr_download, (self.display.get_width(), self.display.get_height())), (0, 0))
        for entities in self.scene.get_all_entities():
            for entity in entities:
                entity.run()
                self.display.blit(entity.body(), entity.geo)
        pygame.display.update()


