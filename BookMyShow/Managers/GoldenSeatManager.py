from Managers import  SeatManager

from Seats import  GoldenSeat
class GoldenSeatManger(SeatManager.SeatManager):
    def __init__(self,capacity):
        super().setCapacity(GoldenSeat.GoldenSeat(), capacity)