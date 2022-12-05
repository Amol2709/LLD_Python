from interfaces import  Rooms 

class MeetingRooms(Rooms.Rooms):
    
    def setCapacity(self, capacity):
        super().setCapacity(capacity)
    

    def setID(self, id):
        super().setID(id)
    
    def setStatus(self, status):
        super().setStatus(status)
