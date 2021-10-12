import sys

text = "This is a string"
text = "This is a string"
text = """This is a string that preserves whitespace
I can make more than one line
and the new lines will be preserved!"""

print(text)

text = "I'm a string. \n This is a new line \n \tI'm indented"
print(text)

text = '" I\'m a quoted string"'
print(text)

text = '"'
text = "\"I'm "
text = " ' \" "
text = """ ""'''''''''' """

text = r"Special characters do nothing \n\n See, no new lines haha gotcha"
print(text)

print(sys.getdefaultencoding())


# Unicode characters
text = "The circumference of a circle is 2\u03c0r"
print(text)

text = "\u6211\u6703\u5beb\u4e2d\u6587"
print(text)

text = "I'm a long sentence with a lot of useless words"
# Strings are immutable
sub = text[10:]
print(sub)
sub = text[:10]
print(sub)
sub = text[10:20]
print(sub)

text = "42"
number = text.isdigit()
letter = text.isalpha()
starts_with_cap = text.istitle()
print(number, letter, starts_with_cap)

text = "     \n\n\t\t\r\r"
space = text.isspace()
print(space)


text = "I'm a long sentence with a lot of useless words"
length = len(text)
print(length)
countL = text.count("l")
print(countL)

print(text.title())
print(text.capitalize())
print(text.swapcase())
print(text.lower())
print(text.upper())


text = "I'm a bit shorter"
newText = text.center(30)
print(newText)
newText = text.rjust(30)
print(newText)

text = "The big blue bisexual bird bites the dust"
newText = text.replace("bi", "xx")
print(newText)
newText - text.replace("bi", "xx", 1)
print(newText)

words = text.split(" ")
print(words)

start = text.startswith("T")
print(start)
end = text.endswith("T")
print(end)
loc = text.find("bi")
print(loc)
loc = text.find("bi", loc + 1)
print(loc)
loc = text.rfind("bi")
print(loc)
loc = text.find("z")
print(loc)

loc = text.find("bi")
print(loc)
loc = text.index("bi")
print(loc)
loc = text.find("z")
print(loc)
# loc = text.index("z")
# print(loc)
# commented out cus it causes crash

words = ["One", "Two", "Three", "Four"]
text = " ".join(words)
print(text)
text = "\t".join(words)
print(text)
text = "\n".join(words)
print(text)
text = "student,".join(words)
print(text)
