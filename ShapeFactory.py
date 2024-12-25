from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def draw(self):
        return f"Drawing a Circle with radius : {self.radius}"
    
class Square(Shape):
    def __init__(self,side):
        self.side = side

    def draw(self):
        return f"Drawing a Square with side : {self.side}"
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def draw(self):
        return f"Drawing a Rectangle with Lenght: {self.length}, Width: {self.width}"
    
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type,*args):
        shape_type = shape_type.lower()
        if shape_type == "circle":
            if len(args) != 1 :
                raise ValueError("Circle requires 1 argument")
            return Circle(*args)
        elif shape_type == "square":
            if len(args) != 1 :
                raise ValueError("Square requires 1 argument")
            return Square(*args)
        elif shape_type == "rectangle":
            if len(args) != 2 :
                raise ValueError("Rectangle requires 2 arguments")
            return Rectangle(*args)
        else:
            raise ValueError("Invalid Shape")

if __name__ == "__main__":
    factory = ShapeFactory()
    circle = factory.create_shape("circle",5)
    print(circle.draw())

    square = factory.create_shape("square",10)
    print(square.draw())

    rectangle = factory.create_shape("rectangle",20,30)
    print(rectangle.draw())
