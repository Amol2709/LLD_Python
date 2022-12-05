from . import interface_computaional_strategy  

class TwoWheeler_CS(interface_computaional_strategy.Computataional_Strategy):
    def __init__(self) :
        self.twowheeler_default_price = 10
        
    def computePrice(self):
        return  self.twowheeler_default_price