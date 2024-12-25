from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class CoffeeDecorator(Coffee):
    def __init__(self,coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class SimpleCoffee(Coffee):
    def cost(self):
        return 5
    
    def description(self):
        return "Simple Coffee"
    
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2
    
    def description(self):
        return self._coffee.description() + ",Milk"
    
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3
    
    def description(self):
        return self._coffee.description() + ",Sugar"
    
class WippedCream(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 5
    
    def description(self):
        return self._coffee.description() + ",Wipped Cream"
    
if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"Description:{coffee.description()}, Cost:${coffee.cost()}")

    coffee = MilkDecorator(coffee)
    print(f"Description:{coffee.description()}, Cost:${coffee.cost()}")

    coffee = SugarDecorator(coffee)
    print(f"Description:{coffee.description()}, Cost:${coffee.cost()}")

    coffee = WippedCream(coffee)
    print(f"Description:{coffee.description()}, Cost:${coffee.cost()}")

    
    