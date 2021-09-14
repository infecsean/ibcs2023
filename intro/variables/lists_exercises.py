# lists_exercise.py

# 01. sum all of the elements in the list
mylist = [1, 2, 3, 4, 5]
sum = sum(mylist)
# print(sum)

# 02. write a program that removes all duplicates from a list
mylist = [1, 1, 1, 2, 2, 3, 4, 4]
unduped = []

for i in mylist:
    if i not in unduped:
        unduped.append(i)
    i = i + 1
# print(unduped)

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

# print(intersection)

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
# print(unionlist)

# 05. Write a program that finds the differences of two lists
listc = [1, 3, 4, 5, 6, 7, 9]
listd = [1, 2, 3, 4, 5, 6, 7, 8]
liste = []

for i in listc:
    if i not in listd:
        liste.append(i)
    i = i + 1

for o in listd:
    if o not in listc:
        liste.append(o)
    o = o + 1

# print(liste)

# 06. Write a program that creates a list containing the freqiencies of elements in a list
lisa = [1, 1, 1, 2, 3, 3, 4, 5, 2, 3, 4, 2, 4, 5]
lisb = []

for i in lisa:
    if i not in lisb:
        lisb.append(i)
    i = i + 1

for o in lisb:
    cnt = lisa.count(o)
    print(f"there are {cnt} {o}s in the list")
