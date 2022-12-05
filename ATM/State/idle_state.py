from . import interface_atm_state 
from . import hascard_state

class IdleState(interface_atm_state.ATMState):

    def acceptCard(self,machine):
        machine.changeState(hascard_state.HasCardState())
    

    
    def selectOperation(self,machine):
        pass

    
    def checkBalance(self,machine):
        pass
    
    
    def withDrawnCash(self,machine):
        pass
    