from ParkingSpotManager import ParkingSpotManager
from FourWheelerSpot import FourWheelerSpot



class FourWheelerSpotManager(ParkingSpotManager):
    def __init__(self):
        super().__init__(FourWheelerSpot)
    
    def addParkingSpot(self):
        return super().addParkingSpot()
    
    def RemovingParkingSpot(self):
        return super().RemovingParkingSpot()