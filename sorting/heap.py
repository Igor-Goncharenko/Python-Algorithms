def heapify(target: list, n: int, i: int) -> None:
    """Heapify.
    Finds subtree elements: node and his 2 children.
    Algorithm places largest element on the i-th position
    (swap the 'largest', 'right' and 'left' so that the 'largest' is the largest).
    """
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
    """Heap sort.
    Firstly, the algorithm turns the array into a max-heap data structure.
    Max-Heap description: 1st lvl - 1 element, 2nd - 2 elements, 3rd - 4, 4th - 8 etc.
    In the array, the elements go in the same order.
    We can describe the relationship between a node and its children by indices:
        node = i;
        left = 2 * i + 1;
        right = 2 * i + 2;
    Moreover, node > left child and node > right child.
    Heapify algorithm places nodes in subtree in the right order.

    Then, each iteration we exclude the largest element (put it at the end of the array)
    and transform the heap to normal form (heapify).

    Worktime: O(n * log(n))
    (usually works 2-3 times slower than quick sort).
    """
    # create max heap data structure
    n = len(target)

    for i in range(n // 2, -1, -1):
        heapify(target, n, i)

    for i in range(n - 1, 0, -1):
        target[0], target[i] = target[i], target[0]
        heapify(target, i, 0)

    return target
