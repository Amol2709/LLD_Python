class Board:
    def __init__(self, N):
        self.N = N 
        self.board = [[None for i in range(N)] for j in range(N)]

    def get_board(self):
        return self.board