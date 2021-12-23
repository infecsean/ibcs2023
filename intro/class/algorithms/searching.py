from typing import List
import random


def sequential_search(value: int, array: List[int]) -> int:
    for idx, val in enumerate(array):
        if val == value:
            return idx
    return None


def binary_search(value: int, array: List[int], start: int = 0, end: int = None) -> int:
    if end is None:
        end = len(array) - 1
    mid = start + (end - start) // 2

    if end >= start:
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            # search thru right subarray
            return binary_search(value, array, start=mid + 1, end=end)
        else:
            # search thru left subarray
            return binary_search(value, array, start=start, end=mid - 1)
    return None


def create_random_list(min: int = 0, max: int = 100, size: int = 50) -> List[int]:
    data = []
    for i in range(size):
        data.append(random.randint(min, max))
    return data


def test_sequential_search(value: int, array: List[int]):
    array.sort()
    idx = sequential_search(value, array)

    if idx is None:
        print(f"didnt find {value}")
    else:
        print(f"found {value} at {idx}")


def main():
    data = create_random_list(55, 110, 50)
    value = 73
    print(data)
    test_sequential_search(value, data)


if __name__ == "__main__":
    main()
