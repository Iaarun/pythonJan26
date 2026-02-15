#Abstraction in Python is the process of hiding the implementation details and showing
# only the functionality to the user.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

circle1 = Circle(5)
print("Area of the circle with radius 5 is: ", circle1.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def test(self):
        pass




rectangle1 = Rectangle(4, 6)
print("Area of the rectangle with length 4 and width 6 is: ", rectangle1.area())