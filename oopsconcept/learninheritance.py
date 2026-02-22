class Animal:
    def __init__(self, species):
        self.species = species
    def makeSound(self):
        return "some generic animal sound"

class Mammal(Animal):
    def __init__(self, species, fur_color):
        super().__init__(species)
        self.fur_color = fur_color
    def giveBirth(self):
        return "Giving birth to live young"

# dog = Mammal("Canine", "Brown")
# print(f"Species: {dog.species}")
# print(f"Fur Color: {dog.fur_color}")
# print(dog.makeSound())# Inherited from Animal class


class Animal1:
    species = ""
    def makeSound(self):
        return "some generic animal sound"

class Mammal1(Animal):
    fur_color = ""
    def giveBirth(self):
        return "Giving birth to live young"

dog = Mammal1()
dog.species = "Canine"
dog.fur_color = "Brown"
print(f"Species: {dog.species}")
print(f"Fur Color: {dog.fur_color}")
print(dog.makeSound())# Inherited from Animal class