from Board import Board
from Players import  Players
from WinningStrategy_interface import  WinningStrategy

class Game:

    def __init__(self):
        self.players=[]


    
    def set_board(self, board:Board ):
        self.board = board
    
    def set_player(self, player:Players):
        if len(self.players)>=2:
            return "Only Two Player can Playe Game"
        self.players.append(player)
    
    def set_winning_strategy(self, strategy:WinningStrategy):
        self.strategy = strategy

    
    
