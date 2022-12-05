from abc import ABC, abstractmethod

class Players(ABC):
    
    @abstractmethod
    def MakeMove(self):
        pass