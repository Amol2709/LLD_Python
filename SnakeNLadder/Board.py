import random
from Snake import Snake
from Ladder import  Ladder
class Board:
    def __init__(self, boardSize):
        self.boardMap = {}
        self.boardSize = boardSize
        self.board = [ [None for i in range(boardSize)] for j in range(boardSize)]
    
    def setNumberofSnake(self, N):
        self.numberofsnake = N
    
    def setNumberofLadder(self, N):
        self.numberofladder = N
    

    def setSnake(self):
        n = 0
        while(n<=self.numberofsnake):
            start = random.randint(0, self.boardSize-1)
            end = random.randint(0, self.boardSize-1)

            if (start!=end) and start>end and (start, end) not in self.boardMap:
                snake = Snake(start, end)
                self.boardMap[(start, end)] = snake
                self.board[start][end] = snake
                n = n+1
        
    def setLadder(self):
        n = 0
        while(n<=self.numberofladder):
            start = random.randint(0, self.boardSize-1)
            end = random.randint(0, self.boardSize-1)

            if (start!=end) and end>start and (start, end) not in self.boardMap:
                ladder = Ladder(start, end)
                self.boardMap[(start, end)] = ladder
                self.board[start][end] = ladder
                n = n+1


                
                





    def get_board(self):
        return self.board
    