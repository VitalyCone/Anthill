from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    @abstractmethod
    def move(self, agent):
        pass