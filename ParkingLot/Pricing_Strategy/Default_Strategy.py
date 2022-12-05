import  interface_pricing_strategy 


class Default(interface_pricing_strategy.PricingStartegy):
    def __init__(self):
        self.charge = 50 
    
    def price(self):
        return self.charge