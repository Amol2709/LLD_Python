from abc import ABC, abstractmethod

class Seat(ABC):

    @abstractmethod
    def setPrice(self, price):
        pass