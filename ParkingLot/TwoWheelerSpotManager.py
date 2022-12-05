from ParkingSpotManager import ParkingSpotManager
from TwoWheelerSpot import TwoWheelerSpot



class TwoWheelerSpotManager(ParkingSpotManager):
    def __init__(self):
        super().__init__(TwoWheelerSpot)
    

    def addParkingSpot(self):
        return super().addParkingSpot()
    def RemovingParkingSpot(self):
        return super().RemovingParkingSpot()