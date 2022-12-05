from Pipe import Pipe  


class Snake(Pipe):
    def __init__(self, start, end):
        if end>start:
            raise Exception('For Ladder Start should be greater than End')
        super().__init__(start, end) 