# lists.py

mylist = [5, 10, 15, 20]
print(mylist)
mytype = type(mylist)
print(mytype)

print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])

for val in mylist:
    print(val)

for idx, val in enumerate(mylist):
    print(f"{idx}: {val}")

i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

for i in range(len(mylist)):
    print(mylist[i])

# append adds to the end of the list
mylist.append(25)
print(mylist)

length = len(mylist)

mylist = [1, 2.5, "3.5", [4.5, 5.5], (6, 7)]
print(mylist)
print(len(mylist))

mylist = [0] * 15
print(mylist)
mylist = [1, 2, 3] * 5
print(mylist)

# concatenates lists
lista = [1, 2, 3]
listb = [4, 5, 6]
listc = lista + listb
print(listc)

# find out if an element is in a list
mylist = ["a", "b", "c", "d", "e", "f"]
print("c" in mylist)
print("c" not in mylist)
print("z" in mylist)
print("z" not in mylist)

# searching for location in list
idx = mylist.index("c")
print(idx)

idx = mylist.index("c", 3, 6)
print(idx)

# inserting into list
mylist.insert(3, "z")
print(mylist)

# remove a specific element from le list
mylist.remove("z")
print(mylist)

popped = mylist.pop()
print(mylist, popped)

popped = mylist.pop(2)
print(mylist, popped)

# count tings in a list
cnt = mylist.count("a")
print(cnt)

mylist.extend(["z", "e", "w", "j"])

# sorting a list
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

# list comprehensions
mylist = []
for i in range(10):
    mylist.append(i)
print(mylist)

mylist = [x for x in range(10)]
print(mylist)

mylist = [x for x in range(10) if x % 2 == 0]
print(mylist)
mylist = [x for x in range(0, 10, 2)]
print(mylist)

mylist = [(x * 3) for x in range(10)]
print(mylist)

filtered = [x for x in mylist if x % 2 == 0]
print(filtered)

maxVal = max(mylist)
filtered = [(maxVal - x) for x in mylist if x > 5 and x < 25]
print(filtered)

mylist = [x for x in range(20)]
# Slicing start:end:step
sublist = mylist[3:6]
print(sublist)

sublist = mylist[3:15:2]
print(sublist)

sublist = mylist[15:3:-2]
print(sublist)

sublist = mylist[7:]
print(sublist)

sublist = mylist[7::3]
print(sublist)

sublist = mylist[:10]
print(sublist)
