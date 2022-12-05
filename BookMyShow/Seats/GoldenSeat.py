from interfaces import Seat 
from Enums import  SeatPrice


class GoldenSeat(Seat.Seat):
    def __init__(self):
        self.price = SeatPrice.SeatPrice.GoldenSeatPrice
    def setPrice(self,price=0):
        self.price = price+ self.price