#data 
# Number data types
num = 10          # Integer
fnum = 10.5      # Float
#cnum = 3 + 4j    # Complex

#dict data type : where we store data in key value pair { key1: value1, key2: value2 }
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person)
print(person["name"]) # Access value by key
print(person["age"]) # Access value by key using get() method

#bool data type
is_active = True
is_admin = False

#set data type : unordered collection of unique items , does not allow duplicate values
fruits = {"apple", "banana", "cherry", "apple", "kiwi"} #duplicate apple
print(fruits) # Output: {'banana', 'kiwi', 'cherry', 'apple'}

#String data type
name = "Sachin" #double quotes
name = 'Sachin'  #single quotes

#List data type : ordered collection of items , allows duplicate values
# Items are enclosed in square brackets [] and mutable
numbers = [1, 2, 3, 4, 5, 2, 3] #duplicate 2 and 3
print(numbers) #

#Tuple data type : ordered collection of items , allows duplicate values
# Items are enclosed in parentheses () and immutable
coordinates = (10, 20, 30, 10) #duplicate 10
print(coordinates) #
