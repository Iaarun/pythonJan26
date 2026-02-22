'''
ordered datastructure of data
mutable
Allow duplicates
'''
def list_basic():
    age=12
    age=[12,54,67,34,34]
    print(age)
    age[2]=95
    print(age)
    #indexing
    print(age[3])
    print(age[-3])


def list_slicing():
    age = [12, 54, 67, 34, 34]
    # get the list from index 2-4
    print(age[2:5])
    #get the data from 3 to last
    print(age[3:])
    #reverse the list
    print(age[::-1])
    print(age[1:-1])

def list_functions():
    fruits = ["apples","banana","oranges","cherry"]
    print(fruits)
    #replace data inlist at specific index
    fruits[0]="mango"
    print(fruits)
    #add data at specific index
    fruits.insert(0,"kiwi")
    print(fruits)
    #appending data
    fruits.append("pineapple")
    print(fruits)
    veggies=["peas","tomatoes"]
    fruits.extend(veggies)
    print(fruits)
    #remove single data
    fruits.remove("pineapple")
    print(fruits)
    #remove multiple data
    del fruits[0:2]
    print(fruits)
    #to reverse the list
    fruits.reverse()
    print(fruits)
    #to sort the list
    fruits.sort()
    print(fruits)
    #to sort the list in descendingorder
    fruits.sort(reverse=True)
    print(fruits)
    fruits.clear()
    print(fruits)

def iterating_list():
    fruits = ["apples", "banana", "oranges", "cherry"]
    for fruit in fruits:
        print(fruit, end=" ")
    print()
    for i in range(len(fruits)):
        print(fruits[i], end=" ")


fruit = ["app", "banana", "cat", "dog", "man"]
fruit.sort(reverse=True)
print(fruit)

#iterating_list()