from abc import  ABC, abstractmethod
#from .. Pricing_Strategy import interface_pricing_strategy,HourlyBasis_Startegy
from Pricing_Strategy import  interface_pricing_strategy,HourlyBasis_Startegy

class Computataional_Strategy:
    def __init__(self) :
        self.pricing_strategy  = HourlyBasis_Startegy.HourlyBasis()
    
    def computePrice(self):
        print('AAAAAaaa')
        return self.pricing_strategy.price()
