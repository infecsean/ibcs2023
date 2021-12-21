import json

a = open(
    "/Users/seanho/Desktop/Develop/Python/ibcs2023/intro/class/OOP/student_grader/JSONs/data.json"
)

data = json.load(a)

for i in data["person"]:
    print("Name: " + i["name"])
    print("Gender: " + i["gender"])
    print("Age: " + i["age"])

a.close
