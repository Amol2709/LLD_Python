from Players import  Players
from Board import  Board

class Game:

    def setBoard(self, board:Board):
        self.board = board
    
    def setNumberOfDice(self, N):
        self.numberofdice = N
        
    def setNumberofPlayers(self,N):
        self.number_of_player = N
        self.players = []
    

    
    def setPlayers(self, player:Players):
        if len(self.players)>=self.number_of_player:
            raise Exception('Initialize again with more Players')
        self.players.append(player)