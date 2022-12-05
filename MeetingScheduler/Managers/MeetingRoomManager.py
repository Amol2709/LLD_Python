from interfaces import  Manager
from Rooms import  MeetingRooms

class MeetingRoomManager(Manager.Manager):


    def setNumberofRooms(self, number_of_room):
        super().setNumberofRooms(number_of_room, MeetingRooms.MeetingRooms)
    
    def getRooms(self):
        return super().getRooms()
    
    def getAvailableMeetingRooms(self):
        return list(super().getAvailableRooms().keys())
    
    def bookMeetingRoom(self, meeting, room_obj):
        super().bookRoom(meeting, room_obj)
    
 