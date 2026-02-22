import array as arr
import numpy as np

#check for string array creation
def array_basic():
    #creating an array
    a = arr.array('i', [1, 2, 3, 4, 5])
    print(a)
    #accessing data
    print(a[0])
    print(a[1:4])
    #iterating array
    for i in a:
        print(i, end=" ")


def numpy_basics():
    #creating a numpy array
    a = np.array([1, 2, 3, 4, 5])
    print(a)
    #accessing data
    print(a[0])
    print(a[1:4])
    #iterating array
    for i in a:
        print(i, end=" ")
    print()
    arr1= np.zeros(5)
    print(arr1)

    arr2 = np.arange(5)
    print(arr2)

    arr4= np.arange(1,10)
    print(arr4)

    arr5 = np.random.rand(5)
    print(arr5)





numpy_basics()
