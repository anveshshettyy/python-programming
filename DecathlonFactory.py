from abc import ABC, abstractmethod

class SportsEquipment(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class Apparel(ABC):
    @abstractmethod
    def get_name(self):
        pass

    def get_price(self):
        pass

class RunningShoes(SportsEquipment):
    def get_name(self):
        return "Decathlon Running Shoes"
    
    def get_price(self):
        return 50.0
    
class RunningTShirt(Apparel):
    def get_name(self):
        return "Decathlon Running T-Shirt"
    
    def get_price(self):
        return 100.0
    
class CyclingHelmet(SportsEquipment):
    def get_name(self):
        return "Decathlon Cycling Helmet"
    
    def get_price(self):
        return 150.0
    
class CyclingGloves(Apparel):
    def get_name(self):
        return "Decathlon Cycling Gloves"
    
    def get_price(self):
        return 200.0
    
class DecathlonFactory(ABC):
    @abstractmethod
    def create_sports_equipment(self):
        pass

    def create_apparel(self):
        pass

class RunningFactory(DecathlonFactory):
    def create_sports_equipment(self):
        return RunningShoes()
    
    def create_apparel(self):
        return RunningTShirt()
    
class CyclingFactory(DecathlonFactory):
    def create_sports_equipment(self):
        return CyclingHelmet()
    
    def create_apparel(self):
        return CyclingGloves()
        
def create_decathlon_factory(factory: DecathlonFactory):
    equipment = factory.create_sports_equipment()
    apparel = factory.create_apparel()

    print(f"Name: {equipment.get_name()}, Price:{equipment.get_price()}")
    print(f"Name: {apparel.get_name()}, Price:{apparel.get_price()}")

runningFactory = RunningFactory()
cyclingFactory = CyclingFactory()

print("Running Products:")
create_decathlon_factory(runningFactory)

print("Cycling Factory:")
create_decathlon_factory(cyclingFactory)