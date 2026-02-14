#Polymorphism is the ability of an object to take on many forms. In Python, polymorphism allows us to define methods in the child class with the same name as defined in their parent class. It is a powerful feature that allows us to use a unified interface for different data types.
#compile time and runtime
#compile time polymorphism is achieved through method overloading, where multiple methods have the same name but different parameters. However, Python does not support method overloading in the traditional sense, but we can achieve similar functionality using default parameters or variable-length arguments.
#runtime polymorphism is achieved through method overriding, where a child class provides a specific implementation of a method that is already defined in its parent class. This allows the child class to modify or extend
#the behavior of the parent class method.

#methodoverloading using *args
class Calculator:
    def multiply(self, a,b, *args):
        result = a*b
        for num in args:
            result *= num
        print("Multiplication: ", result)
#
# calc = Calculator()
# calc.multiply(2,3) # Output: Multiplication: 6
# calc.multiply(2,3,4) # Output: Multiplication: 24
# calc.multiply(2,3,4,5) # Output: Multiplication: 120


#method overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
#dog.sound() # Output: Dog barks
#cat.sound() # Output: Cat meows
animal = [Cat(), Dog(), Animal()]
for a in animal:
    a.sound() # Output: Cat meows, Dog barks, Animal makes a sound

