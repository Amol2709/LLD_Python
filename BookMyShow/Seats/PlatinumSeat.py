from interfaces import Seat 
from Enums import  SeatPrice


class PlatinumSeat(Seat.Seat):
    def __init__(self):
        self.price = SeatPrice.SeatPrice.PlatinumSeatPrice
    def setPrice(self,price=0):
        self.price = price+ self.price