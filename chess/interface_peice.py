from abc import ABC , abstractmethod 

from peicetype import  PeiceType 
from differentPeices import  DifferentPeices

class Piece(ABC):

    

    @abstractmethod
    def move(self,inital_x,initial_y,board):
        pass

    @abstractmethod
    def getType(self):
        pass 
