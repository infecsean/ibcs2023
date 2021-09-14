# python is dynamically typed

# integer
myvar = 7
print(myvar)

# float
myvar = 7.3
print(myvar)

# string
myvar = "now im a string lol"
print(myvar)

myvar = "I'm a string"
print(myvar)

myvar = """
This a very long strring
multiple lines
preserved 
"""
print(myvar)

a, b = 5, 10
print(f"a: {a}\t b: {b}")

myvar = 3.5
mytype = type(myvar)
print(mytype)

myvar = "I'm a string"
mytype = type(myvar)
print(mytype)

# Some Operators are overloaded
a, b = 4, 6
result = a + b
print(result)

a, b = 4, 6.8
result = a + b
print(result)

a, b = "Number ", 5
result = a + str(b)
print(result)
result = f"{a}{b}"
print(result)

result = float(a)
print(result)

result = int(a)
print(result)
