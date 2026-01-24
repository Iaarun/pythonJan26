# Opeartos in python
# arithmetic operators + - * / % // **


def arithmetic_operations():
    print("========================Arithmetic Operators========================")
    x=4
    y=3
    print("Value of x:",x)
    #print(x)
    print("x+y =", x + y) #Addition
    print("x-y =", x - y) #Subtraction
    print("x*y =", x * y) #Multiplication
    print("x/y =", x / y) #Division
    print("x%y =", x % y) #Modulus
    print("x//y =", x // y) #Floor division
    print("x**y =", x ** y) #Exponentiation

def comparison_operators():
    print("========================Comparison Operators========================")
    a=10
    b=20
    print("Value of a:",a)
    print("Value of b:",b)
    print("a == b:", a == b) #false
    print("a != b:", a != b) #true
    print("a > b:", a > b)  #false
    print("a < b:", a < b)  #true
    print("a >= b:", a >= b) #false
    print("a <= b:", a <= b) #true

def logical_operators():
    print("========================Logical Operators========================")
    p = True
    q = False
    print("p and q:", p and q) #false
    print("p or q:", p or q)   #true
    print("not p:", not p)     #false
    print("not q:", not q)     #true


def assignment_operators():
    print("========================Assignment Operators========================")

    num=10
    num = num+5
    print("num =", num)
    num += 5
    print("num =", num) #20

    num -=5
    print("num =", num)#15

    num *=2
    print("num =", num) #30

    num /=3
    print("num =", num) #10.0


def membership_operators():
    print("========================Membership Operators========================")
    list1 = [1, 2, 3, 4, 5]
    print("List:", list1)
    print("3 in list1:", 3 in list1)       #true
    print("6 in list1:", 6 in list1)       #false
    print("3 not in list1:", 3 not in list1) #false
    print("6 not in list1:", 6 not in list1) #true

def ternary_operator():
    # conditional if
    print("========================Ternary Operator========================")
    a = 10
    b = 20
    max_value = a if a > b else b
    print("Max value between", a, "and", b, "is:", max_value)


#arithmetic_operations()
#comparison_operators()
#logical_operators()
