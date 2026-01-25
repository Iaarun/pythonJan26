'''
unordered datastructure
unique value
'''

def set_basic():
    emp_id={12,54,67,34,34}
    print(emp_id)
    emp_id = {12, 54, 67, 34, 34,'hello', 'world'}
    print(emp_id)
    #emplty set
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

iterate_set()