from Managers import SeatManager
from Seats import  SilverSeat
class SilverSeatManger(SeatManager.SeatManager):
    def __init__(self,capacity):
        super().setCapacity(SilverSeat.SilverSeat(), capacity)