'''
mode read, write, append
'''
import shutil
#read ocmplete text file
def file_read():
    file= open("data1.txt","r")
    content = file.read()
    print(content)
    file.close()

#file_read()
def read_lines_from_file(line_number):
    with open("data1.txt","r") as file:
        for line_no, line in enumerate(file):
            if line_no == line_number:
                print(line)
                break

#read_lines_from_file(10)

def write_to_file(data):
   file = open("data2.txt","a")
   file.write(data)
   print("Data written to file successfully")
   file.close()

#write_to_file("\nthis is first file i am writting")
#write_to_file("\nthis is second line i am writting")


def copydata():
    with open("data2.txt",'r') as f1 , open("data3.txt",'w') as f2:
        shutil.copyfileobj(f1,f2)
    print("Data copied successfully")

copydata()