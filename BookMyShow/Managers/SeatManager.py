from abc import ABC, abstractmethod

class SeatManager(ABC):
    # def __init__(self, capacity):
    #     self.capacity = capacity
    #     self.seat = []

    def setCapacity(self, seatobj, capacity):
        self.capacity = capacity
        self.seat = [seatobj for i in range(self.capacity)]