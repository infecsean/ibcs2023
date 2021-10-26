# functions.py


def myFunc():
    print("I'm a function")


myFunc()
# prints out "Im a function"


def area(w: float, h: float) -> float:
    """area function returns the area of a quadrilateral
    Attributes
        w: width of the quadrilateral
        h: height of the quadrilateral
    Returns:
        width * height
    """
    return w * h


a = area(4, 5)
print(a)


def increment(x: int) -> None:
    x = x + 1


x = 5
print(x)
increment(x)
print(x)


def incrementList(x: list) -> None:
    x[0] = x[0] + 1


x = [5]
print(x)
incrementList(x)
print(x)


def nth_root(num: float, root: int, prec: float = 1e-20) -> float:
    if num < 0 and root % 2 == 0:
        raise ValueError(f"No even roots of negative numbers: num = {num}")
    if root < 0:
        raise ValueError(f"No negative roots: root={root}")
    if num == 0:
        return 0
    if root == 0:
        return 1

    # This is our initial guess at an answer
    # There are more advanced ways to choose this
    guess = 1
    prev = 0
    while abs(guess - prev) > prec:
        prev = guess
        #                                 this right here is a demon derivative
        guess -= (guess ** root - num) / (root * guess ** (root - 1))
    return guess


def nth_root2(num: float, root: int, prec: float = 1e-20) -> float:
    r = nth_root(4, 2)
    print(r)

    def f(x: float, r: float, g: float) -> float:
        return g ** r - x

    def df(r: float, g: float) -> float:
        return r * g ** (r - 1)

    guess = 1
    prev = 0
    while abs(guess - prev) > prec:
        prev = guess
    guess -= f(x=num, r=root, g=guess) / df(r=root, g=guess)
    return guess


r = nth_root2(2, 2)
print(r)

r = nth_root(root=4, num=81)
print(r)

# In Python, functions are first-class members
myvar = nth_root

r = myvar(num=625, root=4)
print(r)


def even_handler(val: int) -> None:
    print(f"{val} is divisible by 2")


def odd_handler(val: int) -> None:
    print("ew i dont like odd numbers")


def odd_handler_2(val: int) -> None:
    val = val + 1
    print(f"value is now {val}. Much better...")


def do_a_thing(even_callback, odd_callback) -> None:
    for i in range(20):
        if i % 2 == 0:
            even_callback(i)
        else:
            odd_callback(i)


do_a_thing(even_handler, odd_handler)
do_a_thing(even_handler, odd_handler_2)

# Generators
