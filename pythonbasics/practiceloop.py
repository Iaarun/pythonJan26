def tableofTwo():
    for i in range(1,11):
        print("2 x", i, "=", 2*i)

#tableofTwo()

#factorial of a number
def factorial():
    num = int(input("Enter a number to find factorial: "))
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print("Factorial of", num, "is", fact)

factorial()
