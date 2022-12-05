from game import Game
from board import Board
from humanplayer import  HumanPlayer
from peicetype import  PeiceType

from bot_player import BotPlayer
from HardStrategy import  HardStrat

board_obj= Board()
board = board_obj.getBoard()

player1 = HumanPlayer(PeiceType.BLACK)
player2 = HumanPlayer(PeiceType.WHITE)


player3 = BotPlayer(PeiceType.BLACK, HardStrat())

game = Game(board,player1,player2)

