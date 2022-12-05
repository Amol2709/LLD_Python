from abc import ABC, abstractmethod

class WinningStrategy(ABC):

    @abstractmethod
    def setStrategy(self):
        pass