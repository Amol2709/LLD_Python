from Managers import SeatManager
from Seats import  PlatinumSeat
class PlatinumSeatManger(SeatManager.SeatManager):
    def __init__(self,capacity):
        super().setCapacity(PlatinumSeat.PlatinumSeat(), capacity)