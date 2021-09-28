# tuples.py

# tuples are like lists, but immutable ( cant be changed later)
# becuz they cant be mutated, they arre slightly more space/time efficient

import sys, time

a_list = [1, 2, 3, 4, 5]
a_tuple = (1, 2, 3, 4, 5)

print("a_list size: ", sys.getsizeof(a_list))
print("a_tuple size: ", sys.getsizeof(a_tuple))

mytuple = (5,) * 10
print(mytuple)

mytuple = mytuple + (1, 2, 3)
print(mytuple)
