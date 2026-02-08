# functions are the block of code which perform the specific task and return the result. It is reusable and modular. It helps to break the code into smaller and manageable parts.
# It also helps to avoid code duplication and improve code readability.
# it enhance the code reusability and maintainability. It also helps to improve the performance of the code by reducing the code size and improving the readability.

#non parameterised function
def say_Hello():
    print("Hello, World!")

#say_Hello()

#parameterised function
def greet(name):
    print("Hello ", name)

# say_Hello()
# greet("John")
# greet("Arun")


def add(a,b):
    sum = a+b
    print(sum)

#add(10,20)
#write a code to print the table of nmber provided by user
# *args and **kwargs
# *args is used to pass a variable number of non keyword arguments to a function.
# It is used when we are not sure about the number of arguments that will be passed to the function.

def sum_of_numbers(*args):
     sum = 0
     for num in args:
         sum += num
     print(sum)

# sum_of_numbers(1,2)
# sum_of_numbers(1,2,3,4,5)
# sum_of_numbers(1,2,3,4,5,6,7,8,9,10)

def function_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

#function_with_kwargs(name="John", age=30, city="New York")

#default parameter
def greet_guests(name="Arun"):
    print("Hello", name, " Welcome to the party!")

#greet_guests()
#greet_guests("John")

#return statement
def add_numbers(a,b):
    sum = a+b
    return sum

def multiply_numbers(num1,num2):
    multiply =num1*num2
    print(multiply)

c = add_numbers(10,30)
multiply_numbers(c,5)