def bubble_sort(target: list) -> list:
    for i in range(len(target)):
        is_sorted = True
        for j in range(len(target) - i - 1):
            if target[j] > target[j + 1]:
                target[j], target[j + 1] = target[j + 1], target[j]
                is_sorted = False
        if is_sorted:
            break
    return target


def selection_sort(target: list) -> list:
    for i in range(len(target) - 1):
        min_i = len(target) - 1
        for j in range(i, len(target) - 1):
            if target[j] < target[min_i]:
                min_i = j
        target[i], target[min_i] = target[min_i], target[i]
    return target


def insertion_sort(target: list) -> list:
    for i in range(1, len(target)):
        moving = target[i]
        j = i - 1
        while j >= 0 and moving < target[j]:
            target[j + 1] = target[j]
            j -= 1
        target[j + 1] = moving
    return target


def heapify(target: list, n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and target[left] > target[largest]:
        largest = left
    if right < n and target[right] > target[largest]:
        largest = right

    if largest != i:
        target[i], target[largest] = target[largest], target[i]
        heapify(target, n, largest)


def heap_sort(target: list) -> list:
    n = len(target)

    for i in range(n // 2, -1, -1):
        heapify(target, n, i)

    for i in range(n - 1, 0, -1):
        target[0], target[i] = target[i], target[0]
        heapify(target, i, 0)

    return target


def quick_sort(target: list) -> None:
    pass


# test sorting algorithms speed
if __name__ == '__main__':
    from random import randint
    from time import perf_counter
    test_array_1000 = [randint(1, 10000) for _ in range(1_000)]
    test_array_10000 = [randint(1, 10000) for _ in range(10_000)]
    test_array_100000 = [randint(1, 10000) for _ in range(100_000)]
    test_array_1000000 = [randint(1, 10000) for _ in range(1_000_000)]

    # bubble sort
    start1 = perf_counter()
    bubble_sort(test_array_1000.copy())
    start2 = perf_counter()
    bubble_sort(test_array_10000.copy())
    end = perf_counter()
    print(f"Test BUBBLE sort. For 1,000 el.: {start2 - start1:.5f}s; for 10,000 el.: {end - start2:.5f}s.")

    # selection sort
    start1 = perf_counter()
    selection_sort(test_array_1000.copy())
    start2 = perf_counter()
    selection_sort(test_array_10000.copy())
    end = perf_counter()
    print(f"Test SELECTION sort. For 1,000 el.: {start2 - start1:.5f}s; for 10,000 el.: {end - start2:.5f}s.")

    # insertion sort
    start1 = perf_counter()
    insertion_sort(test_array_1000.copy())
    start2 = perf_counter()
    insertion_sort(test_array_10000.copy())
    end = perf_counter()
    print(f"Test INSERTION sort. For 1,000 el.: {start2 - start1:.5f}s; for 10,000 el.: {end - start2:.5f}s.")

    # heap sort
    start1 = perf_counter()
    heap_sort(test_array_10000.copy())
    start2 = perf_counter()
    heap_sort(test_array_100000.copy())
    end = perf_counter()
    print(f"Test HEAP sort. For 10,000 el.: {start2 - start1:.5f}s; for 100,000 el.: {end - start2:.5f}s.")

