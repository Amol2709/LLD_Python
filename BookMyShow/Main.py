from Movie import Movie
from Managers import  ScreenManager

movie = Movie()
movie.setName('Avengers')

obj = ScreenManager.ScreenManager()
obj.setScreen(3)
for screen in obj.getallScreens():
    obj.setScreenCapacity(screen)
    obj.setMovie(screen,movie)


info = obj.getallScreens()
print(info[1].getMovie())


# obj = GoldenSeat()


