from Pipe import Pipe  


class Ladder(Pipe):
    def __init__(self, start, end):
        if start>end:
            raise Exception('For Ladder Start should be less than End')
        super().__init__(start, end)