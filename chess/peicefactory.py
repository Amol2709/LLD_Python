from differentPeices import  DifferentPeices
from horse import  Horse
from camel import  Camel

class PeiceFactory:

    def getpeice_instance(self,peicetype):
        if peicetype == DifferentPeices.HORSE.value:
            return Horse()
        elif peicetype == DifferentPeices.CAMEL.value:
            return Camel()