#loops in python
#  for loop
# while loop
print("========================For Loop========================")
# for i in range(1,5): # 0 to 4
#     print("Iteration:", i)

def loopthroughfruits():
    fruits =["apple", "banana", "cherry", "kiwi"]

    for x in fruits:
        print(x)

def iterate_using_index():
    fruits =["apple", "banana", "cherry", "kiwi"]
    print(len(fruits))
    print("Max index:", len(fruits)-1)

    for i in range(len(fruits)):
        print("Index:", i, "Value:", fruits[i])




def nested_for_loop():
    for i in range(1,4): #outer loop
        print("Outer Loop Iteration:", i)
        for j in range(1,4): #inner loop
            print("  Inner Loop Iteration:", j)


#iterate_using_index()
#nested_for_loop()


# for i in range(1,11):
#    print(i)

print("\n========================Pattern Programms========================")
'''
* * * * 
* * * * 
* * * * 
* * * *
'''
def pattern1():
    for i in range(4):
        for j in range(4):
            print("*", end=" ")
        print()

#pattern1()

'''
* 
* * 
* * * 
* * * * 
'''
def pattern2():
    for i in range(1,5):
        for j in range(i):
            print("*", end=" ")
        print()
#pattern2()

def pattern3():
    for i in range(4,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()
#pattern3()



def while_loop():
    count =1
    while count <=5:
        print("Count is:", count)
        count +=1

while_loop()
