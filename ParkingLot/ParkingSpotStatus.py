from enum import Enum

class ParkingSpotStatus(Enum):
    Available, Filled, Maintainance = 1,2,3


# x=ParkingSpotStatus.Available

# if x==ParkingSpotStatus.Available:
#     print('do')