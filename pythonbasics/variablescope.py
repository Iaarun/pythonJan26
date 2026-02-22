# local
# global
# nonlocal

def greet():
    message = "Hello, World!" # local variable
    print(message)

greet()
#print(message)
name = "John" # global variable
def greet_name(name):
    print("Hello", name)

greet_name(name)
print(name)
def outer_function():
    message = "Hello, World!" # local variable
    def inner_function():
        nonlocal message
        message = "Hello, Python!"
        print("Inner Function:", message)
    inner_function()
    print("Outer Function:", message)

outer_function()