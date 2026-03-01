import json

def read_json_file():
    with open("testdata.json","r") as json_file:
        data = json.load(json_file)
        #dumps() method to convert python object to a json object
        print(json.dumps(data, indent=4))
        #print("id",data.menu.id)

read_json_file()


