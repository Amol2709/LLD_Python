from abc import  ABC, abstractmethod
from GameSymbol import  Symbol

class Players(ABC):
    def __init__(self):
        self.symbol = None

    @abstractmethod
    def set_symbol(self, symbol: Symbol):
        self.symbol = symbol

    @abstractmethod
    def makeMove(self):
        pass
    