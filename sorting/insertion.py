def insertion_sort(target: list) -> list:
    """Insertion sort.
    Consider that the array from 0 to (i-1)-th index is already sorted.
    And then we insert the i-th element at the position such that the
    array from 0 to i-th index will be sorted as well.

    Worktime: O(n^2)
    (If the array is almost sorted, the execution time tends to O(n))

    Example:
        8 2 1 9 6  (start array);
        2 8 1 9 6  (8 - sorted, insert - 2 -> 2 < 8 -> 2 8 - sorted);
        1 2 8 9 6  (2 8 - sorted, insert - 1 -> 1 < 2 -> 1 2 8 - sorted);
        1 2 8 9 6  (1 2 8 - sorted, insert 9 -> 9 > 8 -> 1 2 8 9 - sorted);
        1 2 6 8 9  (1 2 8 9 - sorted, insert - 6 -> 2 < 6 < 8 -> 1 2 6 8 9 - sorted);
        1 2 6 8 9  (array sorted).
    """
    for i in range(1, len(target)):
        moving = target[i]
        j = i - 1
        while j >= 0 and moving < target[j]:
            target[j + 1] = target[j]
            j -= 1
        target[j + 1] = moving
    return target
