# data_structures/queue.py


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None


class Queue:
    def __init__(self, data: int):
        self._head: Node = None
        self._tail: Node = None
        self._length: int = 0
        self._iter: Node = None

    def enqueue(self, data: int) -> None:
        n = Node(data)
        if self._tail is None:
            self._head = n
            self._tail = n
        else:
            self._tail.next = n
            self._tail = n
        self._length += 1

    def dequeue(self) -> int:
        if self._head is None:
            return None

        data = self._head.data
        self._head = self._head.next
        self._length -= 1

        if self._head is None:
            self._tail = None
        return data

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
