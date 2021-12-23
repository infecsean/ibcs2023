# sorting.py
from typing import List

from searching import create_random_list


def bubble_sort(array: List[int]) -> None:
    swapped = True
    end = len(array) - 1

    while swapped:
        swapped = False
        for i in range(end):
            j = i + 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swapped = True
        end -= 1


def selection_sort(array: List[int]) -> None:
    for i in range(len(array) - 1):
        m = i
        for j in range(i, len(array)):
            if array[j] < array[m]:
                m = j

        if m != i:
            array[m], array[i] = array[i], array[m]


def insertion_sort(array: List[int]) -> None:
    pass


def merge_sort(array: List[int]) -> None:
    pass


def main() -> None:
    data = create_random_list()
    selection_sort(data)
    print(data)


if __name__ == "__main__":
    main()
