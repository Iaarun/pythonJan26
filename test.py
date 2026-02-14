def explain_range():
    for i in range(5,0,-1):
        print(i, end=" ")


#explain_range()

#Create python class and function to calculate the area of a circle,

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


circle1 = Circle(5)
#print("Area of the circle with radius 5 is: ", circle1.area())

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle1 = Rectangle(4, 6)
#print("Area of the rectangle with length 4 and width 6 is: ", rectangle1.area())
import numpy as np
my_dict= {"apple": 3, "banana": 5, "orange": 2, "grape": 4}

k = list(my_dict.keys())
v = list(my_dict.values())
sortvalue = np.argsort(v)
sorted_dict = {k[i]: v[i] for i in sortvalue}
#print(sorted_dict)




