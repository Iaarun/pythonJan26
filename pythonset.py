'''
unordered datastructure
unique value
'''

def set_basic():
    emp_id={12,54,67,34,34}
    print(emp_id)
    emp_id = {12, 54, 67, 34, 34,'hello', 'world'}
    print(emp_id)
    #empty set
    id = set()
    print(id)
    #add and update data
    emp_id.add(63)
    print(emp_id)

    #update set
    id={54,92,37}
    emp_id.update(id)
    print(emp_id)
    #length
    print(len(emp_id))


def iterate_set():
    emp_id = {12, 54, 67, 34, 34, 'hello', 'world'}
    for id in emp_id:
        print(id, end=" ")

def accessdatainSet():
    set1 = {"apple", "banana", "cherry", "date"}
    print("apple" in set1)

def remove_descard_clear():
    set1 = {"apple", "banana", "cherry", "date", "kiwi", "mango"}
    set1.remove("banana")
    print(set1)
    set1.discard("cherry1")
    print(set1)
    set1.pop()
    print(set1)
    set1.clear()
    print(set1)
    set1.pop()

 #tycaste data
def ex_typecasting():
    li= [1,2,3,4,5,5,3,4]
    print(li)
    li1=[]
    for data in li:
        if data not in li1:
            li1.append(data)
    print(li1)
    #typecasting
    x = set(li)
    print(x)


ex_typecasting()