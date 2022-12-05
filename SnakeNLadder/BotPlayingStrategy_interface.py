from abc import ABC, abstractmethod

class BotPlayingStrategy(ABC):
    
    @abstractmethod
    def play(self):
        pass