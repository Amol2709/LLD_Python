from abc import ABC 

class Pipe(ABC):
    def __init__(self, start, end):
        if start == end:
            raise Exception("Start and End Position should be different")
        self.start = start 
        self.end = end 