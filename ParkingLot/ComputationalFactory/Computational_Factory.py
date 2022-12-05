
from Computational_Strategy import  TwoWheelerCS
from Computational_Strategy import  FourWheelerCS

import VechileType

class CompFactory:
    def getComputational_starategy(self,vechile_type:VechileType.Vechile):
        #print(vechile_type)
        if vechile_type ==VechileType.Vechile.FourWheeler:
            print(0000000000)
            return FourWheelerCS.FourWheeler_CS()
        if vechile_type == VechileType.Vechile.TwoWheeler:
            return TwoWheelerCS.TwoWheeler_CS()

