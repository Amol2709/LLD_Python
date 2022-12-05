
from interface_player import  Player


class BotPlayer(Player):
    def __init__(self,peicetype,playingstrategy) -> None:
        self.playingstrategy = playingstrategy
        super().__init__(peicetype)
    
    