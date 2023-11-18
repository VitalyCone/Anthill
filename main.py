import pygame

from agents.Dispatcher.AgentDispatcher import AgentDispatcher

from Messages.Messages import MessageType
from agents.ReferenceBook.ReferenceBook import ReferenceBook
from agents.Scene.SceneAgent import Scene

from agents.Spider.Spider import Spider
from agents.Ant.Ant import Ant
from agents.Anthill.Anthill import Anthill
from agents.Apple.Apple import Apple

input_spider_num = 10
input_ant_num = 100

pygame.init()
display_xy = (500,500)
display = pygame.display.set_mode(display_xy)
pygame.display.set_caption("ANTHILL")


intro_download = pygame.image.load("icons/intro_logo.png").convert_alpha()
backgr_download = pygame.image.load("icons/backgr.png").convert_alpha()


if __name__ == "__main__":
    scene = Scene()
    agent_dispatcher = AgentDispatcher(scene)
    # При запуске происходит что-то непонятное мне, но нужное для фронта
    display.blit(pygame.transform.scale(intro_download, (display.get_width(), display.get_height())), (0, 0))
    antvssp = pygame.font.Font(pygame.font.match_font('MV Boli'), size=25).render("ANTS VS SPIDERS", True, 'Black')
    run_game = pygame.font.Font(pygame.font.match_font('MV Boli'), size=15).render("play", True, 'Black')
    sett = pygame.font.Font(pygame.font.match_font('MV Boli'), size=15).render("settings", True, 'Black')
    exit_from_game = pygame.font.Font(pygame.font.match_font('MV Boli'), size=15).render("exit", True, 'Black')
    # Входные данные для моделирования
    # TODO: Расширить входные данные для пауков, муравьев и т. д. с задачей множества параметров
    input_apple_hp = 10000
    input_anthills = 1
    input_apple = 3
    input_spdr = 3
    input_ant = 100
    # Создание агентов, добавление оных в диспетчер агентов
    for i in range(input_anthills):
        anthill = Anthill(input_apple_hp, input_apple, 0, i)
        agent_dispatcher.add_entity(anthill)
    # FIXME: Добавлять объекты сцены в инициализации, а не тут
    for i in range(input_apple):
        apple = Apple(scene.get_entities_by_type('Anthill')[0], i)
        agent_dispatcher.add_entity(apple)
    for i in range(input_ant):
        ant = Ant(scene.get_entities_by_type('Apple'), scene.get_entities_by_type('Anthill')[0], i)
        agent_dispatcher.add_entity(ant)
    for i in range(input_ant):
        ant = Ant(scene.get_entities_by_type('Apple'), scene.get_entities_by_type('Anthill')[0], i)
        agent_dispatcher.add_entity(ant)
    for i in range(input_spdr):
        spider = Spider(scene.get_entities_by_type('Spider') + scene.get_entities_by_type('Apple'), i)
        agent_dispatcher.add_entity(spider)
        print('aaa')
    while True:
        for entity in scene.entities:
            display.blit(entity.body(), entity.geo)
    # TODO: Описать создание агентов, добавить uri в reference_book, scene - массив uri, Entity - метод get_uri()
