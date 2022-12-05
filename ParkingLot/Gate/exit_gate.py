from . import interface_gate
from ComputationalFactory import  Computational_Factory

import VechileType

class ExitGate():
    def __init__(self) -> None:
        self.computational_factory_obj = Computational_Factory.CompFactory()
    
    def getPrice(self,vechile_type:VechileType.Vechile):
        print(vechile_type)
        return self.computational_factory_obj.getComputational_starategy(vechile_type).computePrice()
    

