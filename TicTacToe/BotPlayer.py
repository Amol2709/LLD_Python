from Players import  Players
from BotPlayingStrategy_interface import  BotPlayingStrategy

class BotPlayer(Players):
    def set_symbol(self, symbol):
        return super().set_symbol(symbol)

    def set_playingStrategy(self, playingStrategy: BotPlayingStrategy):
        self.playingstrategy = BotPlayingStrategy

    def makeMove(self):
        self.playingstrategy.play()
