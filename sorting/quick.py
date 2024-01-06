def quick_sort(target: list) -> list:
    """Quick sort.
    First, choose pivot (some element from the array). Then let's write
    to the left of pivot the elements that are smaller than it, and to
    the right the elements that are larger than it. We get that Pivot
    is at the correct position.
    Then we recursively repeat the operation until we reach the base
    case - an array of one element.
    This algorithm utilizes the principle of 'Divide and Conquer'.

    Worktime: O(n * log(n))
    (In the worst case worktime will be O(n^2).

    Example:
        15 9 7 33 10 25  (start array);
        9 7 10 15 33 25  (first element - 15 - is 'pivot', 9 7 10 less than 15,
            33 25 greater than 15, now 15 in the right position);
        9 7 10  (left array, 9 - 'pivot');
        7 9 10  (7 < 9, 9 < 10, 7 and 10 is one element array - base case);
        7 9 10  (sorted);
        33 25  (right array, 33 - 'pivot');
        25 33  (25 < 33, 25 is one element array - base case);
        25 33  (sorted);
        7 9 10 15 25 33  (merge all arrays and get sorted result).
    """
    if len(target) <= 1:
        return target
    else:
        pivot = target[0]
        left = [x for x in target[1:] if x < pivot]
        right = [x for x in target[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
