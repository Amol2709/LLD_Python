from Managers import GoldenSeatManager, PlatinumSeatManager, SilverSeatManager

class Screen:
    def setMovie(self, movie_obj):
        self.movieinfo = movie_obj
        self.seatinfo=[]
    def getMovie(self):
        return self.movieinfo.getName()
    def getScreenInfo(self):
        pass

    def setCapacity(self,capacity):
        self.totalCap = capacity

    def setGoldenSeat(self,goldcap):
        GoldenSeatManager.GoldenSeatManger(goldcap)
    def setPlatinumSeat(self, platinumcap):
        PlatinumSeatManager.PlatinumSeatManger(platinumcap) 
    def setSilverSeat(self, silvercap):
        SilverSeatManager.SilverSeatManger(silvercap)