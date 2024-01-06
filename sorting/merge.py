def merge_sort(target: list) -> list:
    """Merge sort.
    At each iteration, we split the array into two equal ones, recursively
    apply merge sort and join them so that the elements are in ascending order.
    Base case is one element array.

    Worktime: O(n * log(n))

    Example:
        5 3 2 5 7 8 4 0  (start array);
        split into 5 3 2 5 and 7 8 4 0;
        split into 5 3, 2 5, 7 8 and 4 0;
        split into one element arrays;
        join each stage in ascending order: 3 5, 2 5, 7 8 and 0 4;
        2 3 5 5 and 0 4 7 8;
        0 2 3 4 5 5 7 8 (sorted).
    """
    if len(target) == 1:
        return target
    middle = len(target) // 2
    left = merge_sort(target[:middle])
    right = merge_sort(target[middle:])

    # merge
    i, j = 0, 0
    for k in range(len(target)):
        if j == len(right) or i < len(left) and left[i] < right[j]:
            target[k] = left[i]
            i += 1
        else:
            target[k] = right[j]
            j += 1

    return target
