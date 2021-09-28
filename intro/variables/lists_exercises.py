# lists_exercise.py

# 01. sum all of the elements in the list
mylist = [1, 2, 3, 4, 5]
sum = sum(mylist)
print(sum)

# 02. write a program that removes all duplicates from a list
mylist = [1, 1, 1, 2, 2, 3, 4, 4]
unduped = []

for i in mylist:
    if i not in unduped:
        unduped.append(i)
    i = i + 1
print(unduped)

mylist = [x for x in range(1, 10)] * 2
newlist = [x for i, x in enumerate(mylist) if mylist.index(x) == i]
print("Solution 3", newlist)

newlist = [x for i, x in enumerate(mylist) if x not in mylist[i + 1 :]]
print("Solution 4", newlist)
# 03. Write a program that finds the intersection of two lists
lista = [2, 4, 23, 32, 1, 39, 21]
listb = [4, 52, 23, 98, 72, 89, 1]
intersection = []

# thid works
for i in lista:
    if i in listb:
        intersection.append(i)
    i = i + 1

# this doesnt work
# intersection = [intersection.append(i) for i in lista if i in listb]

print(intersection)


lista = [x for x in range(1, 10)] * 2
listb = [x for x in range(5, 15)]

result = [x for x in lista if x in listb]
result = list(set(result))
print("solution 1: ", result)

result2 = [x for i, x in enumerate(lista) if x in listb and lista.index(x) == i]
print("Solution 2: ", result2)
# 04. Write a program that finds the union of two lists, omitting duplicates
alist = [4, 2, 3, 1, 9]
blist = [2, 5, 8, 7, 6]
templist = []
unionlist = []
templist = alist + blist

for i in templist:
    if i not in unionlist:
        unionlist.append(i)
    i = i + 1

unionlist.sort()
print(unionlist)

result = list(set(lista + listb))
print("solution 1: ", result)
# 05. Write a program that finds the differences of two lists
listc = [1, 3, 4, 5, 6, 7, 9]
listd = [1, 2, 3, 4, 5, 6, 7, 8]
liste = []

for i in listc:
    if i not in listd:
        liste.append(i)


for o in listd:
    if o not in listc:
        liste.append(o)


print(liste)


result = [x for x in (lista + listb) if ((x not in lista) != (x not in listb))]
result = list(set(result))
print("Solution 2: ", result)


# 06. Write a program that creates a list containing the freqiencies of elements in a list
lisa = [1, 1, 1, 2, 3, 3, 4, 5, 2, 3, 4, 2, 4, 5]
lisb = []

####
"""
unduped = []

for i in lisa:
    if i not in unduped:
        unduped.append(i)
print(unduped)
result = []
for i in unduped:
    result.append([i, lisa.count(i)])
print(result)
"""
####


for i in lisa:
    if i not in lisb:
        lisb.append(i)

for o in lisb:
    cnt = lisa.count(o)
    print(f"there are {cnt} {o}s in the list")

list1 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5]
list2 = list(set(list1))
newlist = []
for val in list2:
    newlist += [(val, list1.count(val))]

print("Solution 1: ", newlist)

freq = [(x, list1.count(x)) for i, x in enumerate(list1) if i == list1.index(x)]

print("Solution 2: ", freq)
