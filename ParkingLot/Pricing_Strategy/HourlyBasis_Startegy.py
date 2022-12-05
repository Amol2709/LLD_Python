from . import interface_pricing_strategy 


class HourlyBasis(interface_pricing_strategy.PricingStartegy):
    def __init__(self):
        self.hourly_charge = 20
    
    def price(self):
        return self.hourly_charge