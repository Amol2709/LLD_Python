from DiceService import  DiceService


class Dice:
    def __init__(self):
        self.diceService = DiceService()
    def setColor(self, color):
        self.color = color 
    
    def roll(self):
        self.diceService()
