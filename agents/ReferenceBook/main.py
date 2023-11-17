from agents.Ant.Ant import Ant
from agents.Spider.Spider import Spider

from agents.Dispatcher.AgentDispatcher import AgentDispatcher

from Messages.Messages import MessageType
from agents.ReferenceBook.ReferenceBook import ReferenceBook
from agents.Scene.SceneAgent import Scene

input_spider_num = 10
input_ant_num = 100


if __name__ == "__main__":
    scene = Scene()
    agent_dispatcher = AgentDispatcher(scene)
    # TODO: Описать создание агентов, добавить uri в reference_book, scene - массив uri, Entity - метод get_uri()
