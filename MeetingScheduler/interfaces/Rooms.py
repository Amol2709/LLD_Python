from abc import ABC , abstractmethod
from Enums import  RoomStatus
class Rooms(ABC):
    def __init__(self):
        self.capacity = 0
        self.id = None 
        self.status = RoomStatus.RoomStatus.AVAILABLE
    
    @abstractmethod
    def setCapacity(self, capacity:int):
        self.capacity = capacity
    
    @abstractmethod
    def setID(self, id:str):
        self.id = id
    
    @abstractmethod
    def setStatus(self, status):
        self.status = status
    
    