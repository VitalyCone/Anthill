import random

import pygame


class Anthill:
    def __init__(self):
        self.name = __class__.__name__
        self.anth_font = pygame.font.Font(pygame.font.match_font('verdana'), size=30)
        self.exit = False
        self.geo = [200, 800]
        self.deaths_of_spider = 0
        self.f = 0

    def body(self):
        self.f += 1
        if 20 >= self.f >= 11:
            if self.f == 20:
                self.f = 0
            return pygame.Rect(-5, 790, 220, 220)
        elif 0 <= self.f <= 10:
            return pygame.Rect(5, 800, 200, 200)
