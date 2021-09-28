# dicts.py

mydict = {"given_name": "sean", "family_name": "ho", "age": 93}

print(mydict)

# Accessing data in a dictionary
givenName = mydict["given_name"]
print(givenName)

# dictionaries do NOT store keys in any particular order
dictItems = mydict.items()
print(dictItems)

# Iterating over a dict
for k, v in mydict.items():
    print(f"Key: {k}\tValue: {v}")

for k in mydict.keys():
    print(f"Key: {k}")

for v in mydict.values():
    print(f"Value: {v}")

hasKey = "given_name" in mydict
print(hasKey)

hasKey = "DNE" in mydict
print(hasKey)

# Accessing data in a dictionary
givenName = mydict.get("given_name")
print(givenName)
middleName = mydict.get("middle_name")
print(middleName)

familyName = mydict.pop("family_name")
print(familyName)
print(mydict)

something = mydict.popitem()
print(something)
print(mydict)

mydict.clear()
print(mydict)

mydict["one"] = 1
mydict["two"] = 2
print(mydict)

del mydict["one"]
print(mydict)
