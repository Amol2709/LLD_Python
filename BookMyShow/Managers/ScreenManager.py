import Screen

class ScreenManager:
    def __init__(self):
        # self.screen_info = {}
        self.screen = [None]
    
    def setScreen(self,number_of_screen):
        self.screen = [Screen.Screen() for i in range(number_of_screen)]
    
    def getallScreens(self):
        return self.screen
    
    def setScreenCapacity(self,screen_obj, silver=50, gold = 50, platinum = 50):
        screen_obj.setCapacity(silver+gold+platinum)
        screen_obj.setGoldenSeat(gold)
        screen_obj.setPlatinumSeat(platinum)
        screen_obj.setSilverSeat(silver)    


    def setMovie(self, screen_obj, movie_obj):
        screen_obj.setMovie(movie_obj)

     
