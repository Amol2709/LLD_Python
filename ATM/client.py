import ATM
from State import idle_state

atm = ATM.ATM(idle_state.IdleState())

current_state = atm.getCurrentState()

