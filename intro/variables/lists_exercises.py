# lists_exercise.py

# 01. sum all of the elements in the list
mylist = [1, 2, 3, 4, 5]
sum = sum(mylist)
# print(sum)

# 02. write a program that removes all duplicates from a list
mylist = [1, 1, 1, 2, 2, 3, 4, 4]
unduped = []

x = 0
while mylist[x] == mylist[x + 1]:
    mylist.remove(x)
    x = x + 1
# unduped = [mylist.remove(x) for x in mylist if x == x + 1]
print(mylist)

# 03. Write a program that finds the intersection of two lists
# 04. Write a program that finds the union of two lists, omitting duplicates
# 05. Write a program that finds the differences of two lists
# 06. Write a program that creates a list containing the freqiencies of elements in a list
