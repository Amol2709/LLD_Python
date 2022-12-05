from ParkingSpot import  ParkingSpot


class TwoWheelerSpot(ParkingSpot):
    def __init__(self, id, status):
        super().__init__(id, status)