from collections import namedtuple
from typing import List

from numpy import divide


Coord = namedtuple("Coord", ["x", "y"])


class Quad:
    def __init__(self, top: int, right: int, bottom: int, left: int):
        self.ne = None
        self.se = None
        self.nw = None
        self.sw = None
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.children: List[Coord] = []

    def divide(self):
        """
        Divides this quad into four equal quads
        """
        """
        
        """

        cx = (self.left + self.right) // 2
        cy = (self.top + self.bottom) // 2
        self.nw = Quad(top=self.top, right=cx, bottom=cy, left=self.left)
        self.ne = Quad(top=self.top, right=self.right, bottom=cy, left=cx)
        self.sw = Quad(top=cy, right=cx, bottom=self.bottom, left=self.left)
        self.se = Quad(top=cy, right=self.right, bottom=self.bottom, left=cx)

    def contains(self, c: Coord) -> bool:
        return (
            c.x >= self.left
            and c.x < self.right + 1
            and c.y >= self.top
            and c.y < self.bottom
        )

    def __len__(self):
        return len(self.children)

    def __str__(self):
        cd = [f"({c.x}, {c.y})" for c in self.children]

        return f"""Quad ({self.right}, {self.bottom}): {len(self.children)}
    {', '.join(cd)}
NW:{self.nw}
NE:{self.ne}
SW:{self.sw}
SE:{self.se}
"""


class QuadTree:
    def __init__(self, top: int, right: int, bottom: int, left: int, max_cap: int = 5):
        self._max_cap = max_cap
        self._root = Quad(top=top, right=right, bottom=bottom, left=left)

    def add(self, child: Coord):
        # find smallest quad that should contain
        # child
        quad = self._find_quad(self._root, child)

        # if it has room for another child
        # put that chold in quad
        if len(quad) < self._max_cap:
            quad.children.append(child)
            return

        # if there is no room, divide the quad
        while len(quad) >= self._max_cap:
            quad.divide()

            # reassign children to new smaller quads
            for c in quad.children:
                next = self._next_quad(quad, c)
                next.children.append(c)
            # remove children from this quad
            quad.children.clear()
            # check smaller quads to see if THEY
            # should also be divided
            quad = self._next_quad(quad, child)

        quad.children.append(child)

    def _next_quad(self, root: Quad, child: Coord) -> Quad:
        """
        Find the appropriate child quad that goes into
        """
        if root.ne is None:
            return None
        if root.ne.contains(child):
            return root.ne
        if root.nw.contains(child):
            return root.nw
        if root.se.contains(child):
            return root.se
        if root.sw.contains(child):
            return root.sw

    def _find_quad(self, root: Quad, child: Coord) -> Quad:
        """
        Recursively dive into quads until it gets to the smallest
        appropriate quad
        Find the lowest-level quad that has not been divided
        """
        quad = root
        parent = quad
        while quad is not None:
            parent = quad
            quad = self._next_quad(quad, child)
        return parent

    def __str__(self):
        return str(self._root)


if __name__ == "__main__":
    qt = QuadTree(top=0, right=1024, bottom=1024, left=0)

    qt.add(Coord(256, 256))
    qt.add(Coord(768, 256))
    qt.add(Coord(256, 768))
    qt.add(Coord(768, 768))
    qt.add(Coord(256, 100))
    qt.add(Coord(256, 200))
    qt.add(Coord(256, 300))
    qt.add(Coord(256, 400))
    qt.add(Coord(100, 400))
    qt.add(Coord(200, 400))
    qt.add(Coord(300, 400))
    qt.add(Coord(400, 400))
    print(qt)
    print("─" * 50)
