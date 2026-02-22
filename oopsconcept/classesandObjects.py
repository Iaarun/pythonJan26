class Bike:
    name=""
    gear=""
    def stop(self):
        print("Bike is stopping")
    def display_info(self):
        print("Bike Name: ", self.name)
        print("Bike Gear: ", self.gear)
    def start(self):
        print(self.name+ "Bike is starting")

# bike1 = Bike()
# bike1.name = "Yamaha"
# bike1.gear = "5"
# bike1.start()
#
# bike2 = Bike()
# bike2.name = "Honda"
# bike2.gear = "6"
# bike2.start()
#
# bike2.display_info()
# bike1.display_info()

class Car:
   #constructor is a special method that is called when an object is created.
   # It is used to initialize the attributes of the object.
    def __init__(self,name, model, year=2004):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        print("Car Name: ", self.name)
        print("Car Model: ", self.model)
        print("Car Year: ", self.year)

car1 = Car("Toyota", "Camry")
#car1.display_info()


car2 = Car("Honda", "Civic", 2021)
#car2.display_info()

#Inheritance is a fundamental concept in object-oriented programming that allows
# a new class (called a child or subclass) to inherit attributes and methods from
# an existing class (called a parent or superclass).
# The child class can also have its own unique attributes and methods, in addition to those inherited from the parent class.
#multiple inheritance is a feature of some object-oriented programming languages in which a class can inherit attributes and methods from more than one parent class. This allows for greater flexibility and code reuse, as a child class can combine the functionality of multiple parent classes. However, it can also lead to ambiguity and complexity if not used carefully, especially when there are conflicting attributes or methods in the parent classes.
#multilevel inheritance is a feature of object-oriented programming languages in which a class can inherit attributes and methods from a parent class, which in turn can inherit from another parent class. This creates a hierarchy of classes, where each class can have its own unique attributes and methods, as well as those inherited from its parent classes. Multilevel inheritance allows for greater code reuse and organization, as it enables the creation of more specific classes that build upon the functionality of more general classes. However, it can also lead to complexity and potential issues with method resolution if not used carefully.
class Animal:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("Animal Name: ", self.name)
class Dog(Animal):
    #subclass Dog inherits from superclass Animal
    def sound(self):
        print(self.name, " Woof! Woof!")

# german_shepherd = Dog("Rex")
# german_shepherd.info()  # Inherited method from Animal class
# german_shepherd.sound()  # Method defined in Dog class
#
# labrador = Dog("Buddy")
# labrador.info()  # Inherited method from Animal class
# labrador.sound()  # Method defined in Dog class


class Animal:
    def __init__(self, breed):
        self.breed = breed
    def info(self):
        print("Animal Breed: ", self.breed)

class Cat(Animal):
     def __init__(self,breed, name):
         super().__init__(breed)
         self.name = name

     def display_details(self):
         print("Cat Name: ", self.name)

cat1 = Cat("Siamese","Whisker" )
cat1.display_details()
cat1.info()

#multiple inheritance
class Person:
    def __init__(self, name):
        self.name = name
class Job:
    def __init__(self, title):
        self.title = title
class Employee(Person, Job):
    def __init__(self, name, title):
        Person.__init__(self, name)
        Job.__init__(self, title)
    def display_info(self):
        print("Employee Name: ", self.name)
        print("Job Title: ", self.title)

employee1 = Employee("Alice", "Software Engineer")
employee1.display_info()

#multilevel inheritance
class Vehicle:
    def __init__(self, make):
        self.make = make
class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model
    def display_info(self):
            print("Car Make: ", self.make)
            print("Car Model: ", self.model)
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    def display_info(self):
        super().display_info()
        print("Battery Capacity: ", self.battery_capacity)



