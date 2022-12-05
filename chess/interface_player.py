from abc import ABC , abstractmethod 

class Player(ABC):

    def __init__(self,peicetype) -> None:
        self.peicetype = peicetype
    