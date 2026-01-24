
def string_basic():
    s1 = "Hello world"
    s4 = 'Hello world'
    s2 = '''this is a multi line
            string data'''
    s3 = """this is another multi line @#$2334
            string data"""
    print(s3)
    # iterate through string
    for char in s1:
        print(char, end=" ")
    print()
    print(s1[1])
    print(s1[-1])
    # s1[0]="10"
    # print(s1)
     #string comparison
    print(s1==s4)
    #join two strings
    s5 = s1 + " " + s2
    print(s5)
    #string length
    print("Length of s1:", len(s1))


def string_functions():
    s1 = "hello world"
    print(s1)
    print(s1.upper())
    print(s1.lower())
    print(s1.capitalize())
    print(s1.title())
    s1.count('l')
    print("Count of 'l':", s1.count('l'))
    print("Index of 'w':", s1.index('w'))
    print("Find 'o':", s1.find('o'))
    print("Replace 'world' with 'there':", s1.replace('world', 'there'))
  #  s1.split(' ')
    print("Split by space:", s1.split('r'))
    s2 = "   hello world   "

#string_basic()
string_functions()