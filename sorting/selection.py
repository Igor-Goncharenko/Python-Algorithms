def selection_sort(target: list) -> list:
    """Selection sort.
    Looks for the smallest element and places it at the beginning of the remaining array.

    Worktime: O(n^2)

    Example:
        8 2 1 9 6  (start array);
        1 2 8 9 6  (1 is smallest element at indices 0 to 4 -> swap 8 and 1);
        1 2 8 9 6  (2 is smallest element at indices 1 to 4 -> no changes);
        1 2 6 9 8  (6 is smallest element at indices 2 to 4 -> swap 8 and 6);
        1 2 6 8 9  (8 is smallest element at indices 3 to 4 -> swap 9 and 8);
        1 2 6 8 9  (array sorted).
    """
    for i in range(len(target) - 1):
        min_i = len(target) - 1
        for j in range(i, len(target) - 1):
            if target[j] < target[min_i]:
                min_i = j
        target[i], target[min_i] = target[min_i], target[i]
    return target
