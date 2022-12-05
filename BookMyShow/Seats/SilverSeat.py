from interfaces import Seat 
from Enums import  SeatPrice


class SilverSeat(Seat.Seat):
    def __init__(self):
        self.price = SeatPrice.SeatPrice.SilverSeatprice
    def setPrice(self,price=0):
        self.price = price+ self.price