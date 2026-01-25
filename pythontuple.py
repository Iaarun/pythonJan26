'''
ordered collection
Immutable
allow duplicates
'''

def tuple_basic():
    fruits = ("apple", "banana", "cherry","pineapple","cherry")
    print(fruits)
    #retrieve data using index
    print(fruits[2])
    #modification of data is not supported
    # fruits[2]='kiwi'
    # print(fruits)
    print(len(fruits))


def iterate_tuples():
    fruits = ("apple", "banana", "cherry", "pineapple", "cherry")

    for fruit in fruits:
        print(fruit, end=" ")

    print()
    for i in range(len(fruits)):
        print(fruits[i], end=" ")

#write a function to add element in the end of a tuple


iterate_tuples()