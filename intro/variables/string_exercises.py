# 1
# Write a python program to count and return a dictionary of character
# frequencies in a given string

# Sample String: 'google.com'
# Expected Result: {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

text = "google.com"
newText = list(text)
freq = {}
for i in newText:
    freq[i] = newText.count(i)
print(freq)


# 2
# Write a Python function to insert a string in the middle of a string

# Sample function and result :
# insert_string_middle('[[]]', 'Python') -> [[Python]]
# insert_string_middle('{{}}', 'PHP') -> {{PHP}}
# insert_string_middle('|||', 'Unbalanced') -> |Unbalanced||

wrapper = "(())"
package = "Python"
wrapped = list(wrapper)
wrapIndex = round(len(wrapper) / 2)
wrapped.insert(wrapIndex, package)
wrapped = "".join(wrapped)
# print(wrapped)

# 3
# Write a Python program to display a number with a comma separator.
# Sample function and result:
# comma_sep("1102") => 1,102
# comma_sep("2340340958") => 2,340,340,958
# Advanced: comma_sep("2340340958", 4) => 23,4034,0958

number = "1102"
numList = list(str(number))
for i in reversed(numList):
    numList.insert(numList.index(i) + 2, ",")

    # print(numList)
comma_sep = "".join(numList)
# print(numList)


# 4
# Write a Python program to move spaces to the front of a given string.
# Sample function and result:
# front_pack("This is a sentence with several spaces") =>
#       #      Thisisasentencewithseveralspaces"

text = "This is a sentence with several spaces"
cnt = text.count(" ")
arr = [" "] * cnt
arr = arr + text.split(" ")
result = "".join(arr)
print(result)


# 5
# Write a Python program to compute sum of digits of a given number string
number = "394857"
s = 0
for c in number:
    if c.isdigit():
        s += int(c)
print(s)

# 6
# Write a Python program to determine if a set of parenthesis are balanced
# (()((()(())())())))()))))(())())()
text = "(()((()(())())())))()))))(())())()"
cnt = 0
balanced = True
if len(text) % 2 == 1:
    balanced = False
for c in text:
    if c == "(":
        cnt += 1
    elif c == ")":
        cnt -= 1
    if cnt < 0:
        break
if cnt != 0:
    balanced = False
