def basic_dict():
    #creating a dictionary
    emp = dict()
    emp = {"name": "John", "age": 30, "city": "New York"}
    print(emp)
    #accessing data
    print(emp["name"])
    print(emp.get("name"))
    #iterate using keys
    for k in emp:
        print(k)
    #iterate using values
    for v in emp.values():
        print(v)
    #iterate using items
    for k,v in emp.items():
        print(k,v)


def nested_dict():
    emp = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "skills": ["Python", "Java", "C++"],
        "education": {
            "degree": "Bachelor's",
            "major": "Computer Science",
            "university": "XYZ University"
        }
    }
    print(emp)
    print(emp["education"]["major"])
    for key in emp:
        print(key,": ", emp[key])


def dict_functions():
    emp = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "skills": ["Python", "Java", "C++"],
        "education": {
            "degree": "Bachelor's",
            "major": "Computer Science",
            "university": "XYZ University"
        }
    }

    #get function accepts  key as parameterand return value if key is present else return default value
    print(emp.get("name"))
    print(emp.get("salary", "Not Available"))

    print(emp.keys())
    print(emp.values())

#update dictionary
    print(emp.get("age"))
    emp["age"] = 31
    print(emp.get("age"))
    print(emp.get("name"),"   ", emp.get("salary", "Not Available"))
    d1= {"name": "Jane", "salary": 300000}
    emp.update(d1)
    print(emp.get("name"),"   ", emp.get("salary", "Not Available"))

    #pop method removes the specified key and return the corresponding value
    emp.pop("age")
    print(emp)
    emp.popitem()
    print(emp)




dict_functions()