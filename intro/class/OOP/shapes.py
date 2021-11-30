# OOP/shapes.py
from math import pi


class Circle:
    def __init(self, r: float):
        """
        Constructor for a circle

        Args:
            r: the radius of the circle
        """
        self.r = r
        # the _ before r indicates that this is private
        print(f"this is the constructor: r:{r}")

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r: float):
        if r <= 0:
            raise ValueError("radius must be > 0")
        self._r = r

    @property
    def circumference(self):
        return self._r * pi * 2

    @property
    def area(self):
        return self._r ** 2 * pi

    # python equivilant of ToString
    def __str__(self):
        return f"r: {self._r}\tcircumference: {self.circumference}\tarea: {self.area}"

    def __gt__(self, other):
        return self._r > other._r

    def __lt__(self, other):
        return self._r < other._r

    def __eq__(self, other):
        if type(other) == Circle:
            return self._r == other._r
        if type(other) == float or type(other) == int:
            return self.area == other

        # if the other object has an area member
        area = getattr(other, "area", None)
        if area is not None:
            return self.area == other.area
        return False


class Rectalngle:
    def __init__(self, height: float, width: float):
        """
        Args: H is the height
        w is the width
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height: float):
        if height <= 0:
            raise ValueError("no negs")
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width: float):
        if width <= 0:
            raise ValueError("No negs")
        self._width = width

    @property
    def perimeter(self):
        return 2 * (self.height + self.width)

    @property
    def area(self):
        return self.height * self.width


def main():
    r = Rectalngle(5, 4)
    print(f"height: {r.height}\tperimeter: {r.perimeter}\tarea: {r.area}")

    """
    c = Circle(5)
    print(f"r: {c.r}\tcircumference: {c.circumference}\tarea: {c.area}")
    """


if __name__ == "__main__":
    main()
