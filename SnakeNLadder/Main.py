from Game import  Game
from Board import  Board
from HumanPlayers import  HumanPlayer
from User import  User




board  = Board(9)
board.setNumberofLadder(6)
board.setNumberofSnake(6)
board.setSnake()
board.setLadder()
board = board.get_board()


user1 = User()
user1.setId(1)
user1.setName('Amol')


user2 = User()
user2.setId(2)
user2.setName('User2')


human1 = HumanPlayer()
human1.setUser(user1)

human2 = HumanPlayer()
human2.setUser(user2)


game = Game()
game.setBoard(board)
game.setNumberofPlayers(2)
game.setPlayers(human1)
game.setPlayers(human2)


print(board)