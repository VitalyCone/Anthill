import pygame

class Anthill:
    def __init__(self):
        self.name = __class__.__name__
        self.body = pygame.Rect(0,800,200,200)
        self.anth_font = pygame.font.Font(pygame.font.match_font('verdana'), size = 30)
        self.exit = False
        self.geo = [200,800]