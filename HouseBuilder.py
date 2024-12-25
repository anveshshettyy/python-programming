class House:
    def __init__(self):
        self.address = None
        self.size = None
        self.material = None
        self.NumBedRooms = None
        self.NumBathrooms = None

    def __str__(self):
        return f"House at Location:{self.address}, size: {self.size}"
    
class BrickHouse(House):
    def __init__(self):
        super().__init__()
        self.material = "brick"

class CementHouse(House):
    def __init__(self):
        super().__init__()
        self.material = "cement"

class HouseBuilder:
    def __init__(self):
        self.house = None

    def create_house(self,house_type):
        if house_type == "brick":
            self.house = BrickHouse()
        
        elif house_type == "cement":
            self.house = CementHouse()
        
        else:
            raise ValueError("Invalid House Type") 
        
    def set_address(self,address):
        self.house.address = address

    def set_size(self,size):
        self.house.size = size

    def set_bedRooms(self,numBedRooms):
        self.house.numBedRooms = numBedRooms

    def set_numbathrooms(self,numBathrooms):
        self.house.numBathrooms = numBathrooms

    def get_house(self):
        return self.house
    
builder = HouseBuilder()
builder.create_house("brick")
builder.set_address("Manglore")
builder.set_size(10)
builder.set_bedRooms(2)
builder.set_numbathrooms(5)

brick_house = builder.get_house()
print(brick_house)



    
