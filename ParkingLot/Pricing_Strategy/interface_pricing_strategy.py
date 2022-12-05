from abc import ABC , abstractmethod

class PricingStartegy(ABC):
    
    @abstractmethod
    def price(self):
        pass