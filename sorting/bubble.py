def bubble_sort(target: list) -> list:
    """Bubble sort.
    Items are 'bubbled' one by one, starting with the largest items.

    Worktime: O(n^2)

    Example:
        5 2 1 9 6  (start array);
        2 5 1 9 6  (5 > 2 -> swap 5 and 2);
        2 1 5 9 6  (5 > 1 -> swap 5 and 1);
        2 1 5 9 6  (5 < 9 -> no changes);
        2 1 5 6 9  (9 > 6 -> swap 9 and 6);
        1 2 5 6 9  (2 > 1 -> swap 2 and 1);
        1 2 5 6 9  (no changes -> sorting finished).
    """
    for i in range(len(target)):
        is_sorted = True
        for j in range(len(target) - i - 1):
            if target[j] > target[j + 1]:
                target[j], target[j + 1] = target[j + 1], target[j]
                is_sorted = False
        if is_sorted:
            break
    return target
