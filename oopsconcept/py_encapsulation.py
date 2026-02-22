# encapsulation: hiding the internal details of an object and only exposing a
# public interface to interact with it.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance



# class Student:
#     name=""
#     age=""
#
# student1 = Student()
# student1.name = "Alice"
# student1.age = "12345"
# print("Student Name: ", student1.name)
# print("Student Age: ", student1.age)

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if name == "":
            print("Invalid name. Name cannot be empty.")
        else:
            self.__name = name

    def set_age(self, age):
         if age > 0 and age < 100:
             self.__age = age
         else:
             print("Invalid age. Age must be between 1 and 99.")


student1 = Student("Alice", 20)
student1.set_age(12345)
student1.set_name("")
print("Student Name: ", student1.get_name())
print("Student Age: ", student1.get_age())


