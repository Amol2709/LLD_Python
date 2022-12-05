from abc import ABC , abstractmethod

import ATM
class ATMState(ABC):
    
    @abstractmethod
    def acceptCard(self,machine:ATM.ATM):
        pass

    @abstractmethod
    def selectOperation(self,machine:ATM.ATM):
        pass

    @abstractmethod
    def checkBalance(self,machine:ATM.ATM):
        pass
    
    @abstractmethod
    def withDrawnCash(self,machine:ATM.ATM):
        pass
    