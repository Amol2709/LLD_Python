from abc import  ABC, abstractmethod 
from interfaces import  Rooms
from Enums import  RoomStatus

class Manager(ABC):
    def __init__(self):
        self.rooms=[]
        self.availableRooms={}
        self.bookedRooms={}

  
    def setNumberofRooms(self,number_of_room, room_obj: Rooms.Rooms):
        #self.rooms = [room_obj() for i in range(number_of_room)]
        for i in range(number_of_room):
            obj = room_obj()
            self.availableRooms[obj]=[1]
            self.rooms.append(obj)
    
    def getRooms(self):
        return self.rooms
    
    def getAvailableRooms(self):
        return self.availableRooms
    
    def bookRoom(self, meeting_obj, room_obj):
        #print(self.availableRooms,room_obj)
        if room_obj not in self.availableRooms:
            raise Exception('Room not available')
        else:


            self.bookedRooms[room_obj] = meeting_obj
            room_obj.setStatus(RoomStatus.RoomStatus.BOOKED)
            del self.availableRooms[room_obj]

        
    
    # @abstractmethod
    # def createMeeting(self):
    #     pass 
