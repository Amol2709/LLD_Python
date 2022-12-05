from Players import  Players
from User import User

class HumanPlayer(Players):

    def set_user(self, user: User):
        self.User = user

    def set_symbol(self, symbol):
        super().set_symbol(symbol)
    
    

    def makeMove(self):
        pass