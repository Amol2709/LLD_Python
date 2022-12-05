from Players import  Players
from BotPlayingStrategy_interface import BotPlayingStrategy

class BotPlayer(Players):

    def setPlayingStratgey(self, strategy: BotPlayingStrategy):
        self.strategy = strategy

    def MakeMove(self):
        self.strategy.play()
        pass