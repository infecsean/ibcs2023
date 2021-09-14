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
# unduped = [unduped.append(x) for x in mylist if x not in unduped]
print(unduped)

# 03. Write a program that finds the intersection of two lists
# 04. Write a program that finds the union of two lists, omitting duplicates
# 05. Write a program that finds the differences of two lists
# 06. Write a program that creates a list containing the freqiencies of elements in a list
