def linear_search(sequence: list, target) -> int:
    """Linear search.
    Finds element's index in sequence.
    If sequence does not contain element returns -1.
    """
    for i, item in enumerate(sequence):
        if item == target:
            return i
    return -1


def binary_search(sorted_seq: list[int], target: int) -> int:
    """Binary search.
    Finds element's index in sequence.
    If sequence does not contain element returns -1.
    """
    start, end = 0, len(sorted_seq) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if sorted_seq[mid] > target:
            # except right part
            end = mid - 1
        elif sorted_seq[mid] < target:
            # except left part
            start = mid + 1
        else:
            return mid

    return -1
