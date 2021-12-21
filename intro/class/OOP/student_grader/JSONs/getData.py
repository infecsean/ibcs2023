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


def Student(ID: str):
    for i in student["Student"]:
        if i["id"] == ID:
            print("Hello, " + i["givenName"] + " " + i["familyName"])
    while True:
        command = input("What would you like to do? ")

        if command == "get assignment":
            GetAssignments(ID)
        if command == "get grades":
            GetGrades(ID)
        else:
            return


def GetGrades(ID):
    # for i in student["Student"]:
    #     if i["id"] == ID:
    #         sub1 = i["subjects"][0]
    #         sub2 = i["subjects"][1]
    #         sub3 = i["subjects"][2]
    # chosenSub = input("Which subject? ")
    # if chosenSub == sub1:

    pass


# def SubChooser(Sub:str):
#     for i in student["Student"]:
#         if i["id"] == ID:
#             sub1 = i["subjects"][0]
#             sub2 = i["subjects"][1]
#             sub3 = i["subjects"][2]
#     switch = {
#         Sub:
#     }


def GetAssignments(ID):
    for i in student["Student"]:
        if i["id"] == ID:
            sub1 = i["subjects"][0]
            sub2 = i["subjects"][1]
            sub3 = i["subjects"][2]
    print("Your subjects are: " + sub1 + ", " + sub2 + ", " + sub3)


def Subject():
    pass


a.close
