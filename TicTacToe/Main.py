from Game import  Game 
from Board import  Board
from HumanPlayer import HumanPlayer
from User import  User
from GameSymbol import  Symbol
from DefaultWinningStrategy import  DefaultStrategy

user = User()
user.set_id(1)
user.set_name('Amol')

board = Board(3)

humanplayer1 = HumanPlayer()
humanplayer1.set_user(user)
humanplayer1.set_symbol(Symbol.symbol_x.value)

humanplayer2 = HumanPlayer()
humanplayer2.set_user(user)
humanplayer2.set_symbol(Symbol.symbol_o.value)


game = Game()
game.set_board(board)
game.set_player(humanplayer1)
game.set_player(humanplayer2)
game.set_winning_strategy(DefaultStrategy())