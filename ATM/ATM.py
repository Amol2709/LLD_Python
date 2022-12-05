

class ATM:
    def __init__(self,state) -> None:
        self.machineState = state
    
    def getCurrentState(self):
        return self.machineState
    
    def changeState(self,newstate):
        self.machineState = newstate
        
