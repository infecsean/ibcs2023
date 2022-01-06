# data_structures/dequeue.py

from typing import Iterator


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None
        self.prev: Node = None


class Queue:
    def __init__(self, data: int):
        self._head: Node = None
        self._tail: Node = None
        self._length: int = 0
        self._iter: Node = None

    def append(self, data: int) -> None:
        n = Node(data)
        if self._tail is None:
            self._head = n
            self._tail = n
        else:
            self._tail.next = n
            n.prev = self._tail
            self._tail = n
        self._length += 1

    def prepend(self, data: int) -> None:
        n = Node(data)
        if self._head is None:
            self._head = n
            self._tail = n
        else:
            self._head.next = n
            n.next = self._head
            self._head = n
        self._length += 1

    def delete_first(self) -> int:
        if self._head is None:
            return None

        data = self._head.data
        self._head = self._head.next

        if self._head is not None:
            self._head.prev = None

        self._length -= 1

        if self._head is None:
            self._tail = None
        return data

    def delete_last(self) -> int:
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __contains__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        return self._length


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(f"Length: {len(q)}")

    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
