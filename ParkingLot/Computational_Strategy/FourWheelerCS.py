#from interface_computaional_strategy import Computataional_Strategy 
from . import interface_computaional_strategy  
class FourWheeler_CS(interface_computaional_strategy.Computataional_Strategy):
    def __init__(self):
        self.Fourwheeler_default_price = 20
        super().__init__()
    
    def computePrice(self):
        #print(super().computePrice())
        
        return  self.Fourwheeler_default_price*super().computePrice()