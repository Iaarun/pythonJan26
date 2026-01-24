#input() always  return String

def user_input_example():
    name = input("Enter your name:")
    print(name)
    #type casting
    age = int(input("Enter your age:"))
    print(age +5 )
    print(type(age))

#user_input_example()

#conditional statements
# if statement, Match-case
# if, if-else, if-elif-else, nested if-else
def conditional_if_statements_example():
    age = int(input("Enter your age:"))
    if age >= 18:
        print("You are eligible to vote.")

    print("End of if statement")
#conditional_if_statements_example()
def conditional_if_else_statements_example():
    age = int(input("Enter your age:"))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
    print("End of if-else statement")

#conditional_if_else_statements_example()

def conditional_if_elif_else_statements_example():
    marks = int(input("Enter your marks:"))
    if marks > 100:
        print("Marks should not be greater than 100")
    else:
        if marks >= 90 and marks <= 100:
            print("Grade A")
        elif marks >= 75 and marks < 90:
            print("Grade B")
        elif marks >= 60 and marks < 75:
            print("Grade C")
        elif marks >= 50 and marks < 60:
            print("Grade D")
        else:
            print("Grade F")
        print("End of if-elif-else statement")


#conditional_if_elif_else_statements_example()

#Match-case statement example
def match_case_example():
    day = input("Enter day of the week:").lower()
    match day:
        case "monday":
            print("It's Monday")
        case "tuesday":
            print("It's Tuesday")
        case "wednesday":
            print("It's Wednesday")
        case "thursday":
            print("It's Thursday")
        case "friday":
            print("It's Friday")
        case "saturday":
            print("It's Saturday")
        case "sunday":
            print("It's Sunday")
        case _:
            print("Invalid day")

#match_case_example()

#example take one integer number input form user and find out even odd
# take two number input from the user and perform the arithmetic operations as per user choice

def arithmetic_operations():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    operation= input("Enter operation (+, -, *, /):")
    match operation:
        case "+":
            print("Sum:", a + b)
        case "-":
            print("Difference:", a - b)
        case "*":
            print("Product:", a * b)
        case "/":
            print("Quotient:", a / b)
        case _:
            print("Invalid operation")

#arithmetic_operations()



#compare two numbers and print the largest numbe

def operations():
    number1 = int(input("enter first number"))
    number2 = int(input("enter second number"))
    operation = input("enter the operation")
    match operation:
        case "Add":
            print(number1 + number2)
        case "Sub":
            print(number1 - number2)
        case "Mult":
            print(number1 * number2)
        case "Div":
            print(number1 % number2)
        case _:
            print("invalid operation")

operations()





