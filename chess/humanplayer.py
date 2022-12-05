
from interface_player import  Player


class HumanPlayer(Player):
    def __init__(self,peicetype) -> None:
        super().__init__(peicetype)