import json
from pathlib import Path

# Gets the parent directory and turns it into a string
path = str(Path(__file__).parent)

# Open and gets the data from the json file
a = open(path + "/student.json")
b = open(path + "/subject.json")
c = open(path + "/assignment.json")
student = json.load(a)
subject = json.load(b)
assignment = json.load(c)

for i in student["Student"]:
    print("Student ID: " + i["id"])
    print("Family Name: " + i["familyName"])
    print("Given Name: " + i["givenName"])


def Student(ID):
    pass
    # ndex = student["Student"].index(ID)
    # print("Hello, " + index["givenName"] + index["familyName"])


a.close
