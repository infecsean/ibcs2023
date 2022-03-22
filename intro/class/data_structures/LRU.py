# LRU.py


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            stuff = self.cache.pop(key)
            self.cache[key] = stuff
            return stuff
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if len(self.cache) >= self.cap:
            self.cache.pop(self.cap)

        self.cache.pop[key] = value

    capacity = 3
