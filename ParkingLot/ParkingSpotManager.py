from abc import ABC ,abstractmethod
from ParkingSpotStatus import ParkingSpotStatus
from ParkingSpot import  ParkingSpot

class ParkingSpotManager(ABC):
    def __init__(self, parkingspotType: ParkingSpot):
        self.parkingspot_list = []
        self.parkingspotType = parkingspotType

   
    def setNumberofParkingSpot(self,N:int):
        for i in range(N):
             self.parkingspot_list.append(self.parkingspotType(i,ParkingSpotStatus.Available))
    
    @abstractmethod
    def addParkingSpot(self):
        pass

    @abstractmethod
    def RemovingParkingSpot(self):
        pass