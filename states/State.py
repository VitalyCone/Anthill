from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    
    def __init__(self, agent):
        self.agent = agent

    @abstractmethod
    def move(self, agent):
        pass
