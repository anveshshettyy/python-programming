from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    def description(self):
        pass

class CoffeeDecorator(Coffee):
    def __init__(self,coffee):
        self._coffee = coffee

    def cost(self):
        pass

    def description(self):
        pass

class SimpleCoffee(Coffee):
    def cost(self):
        return 5
    
    def description(self):
        return "Simple Coffee"
    
class MilkDecorator(Coffee):
    def cost(self):
        return self.cost() + 2
    
    def description(self):
        return self.description() + ",Milk"
    
if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"Description:{coffee.description()}, Cost:${coffee.cost()}")
    