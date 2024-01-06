from random import randint as _randint
from time import perf_counter as _perf_counter
from typing import Callable as _Callable

from sorting.bubble import bubble_sort
from sorting.selection import selection_sort
from sorting.insertion import insertion_sort
from sorting.heap import heap_sort
from sorting.quick import quick_sort
from sorting.merge import merge_sort


def is_sorted(array: list[int]) -> bool:
    """Returns 'True' if array elements in non-decreasing order."""
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


def gen_test_int_array(size: int, a: int = None, b: int = None) -> list[int]:
    a, b = a or 1, b or size
    return [_randint(a, b) for _ in range(size)]


def test_sort_alg_worktime(algorithm: _Callable, *, test_size: int = 1000, to_sort: list[int] = None) -> float:
    """"""
    target = to_sort.copy() if to_sort is not None else gen_test_int_array(test_size)
    start_time = _perf_counter()
    sorted_arr = algorithm(target)
    end_time = _perf_counter()
    if sorted_arr is None or not is_sorted(sorted_arr):
        raise RuntimeError(f"Sorting algorithm '{algorithm.__name__}' does not work!")
    return end_time - start_time


if __name__ == '__main__':
    test_1000 = gen_test_int_array(1_000)
    test_10000 = gen_test_int_array(10_000)
    test_100000 = gen_test_int_array(100_000)
    test_1000000 = gen_test_int_array(1_000_000)

    t1 = test_sort_alg_worktime(bubble_sort, to_sort=test_1000)
    t2 = test_sort_alg_worktime(bubble_sort, to_sort=test_10000)
    print(f"'{bubble_sort.__name__}' worktime: \n1000 elements {t1:.3f}s;\n10000 elements {t2:.3f}.\n")

    t1 = test_sort_alg_worktime(selection_sort, to_sort=test_1000)
    t2 = test_sort_alg_worktime(selection_sort, to_sort=test_10000)
    print(f"'{selection_sort.__name__}' worktime: \n1000 elements {t1:.3f}s;\n10000 elements {t2:.3f}.\n")

    t1 = test_sort_alg_worktime(insertion_sort, to_sort=test_1000)
    t2 = test_sort_alg_worktime(insertion_sort, to_sort=test_10000)
    print(f"'{insertion_sort.__name__}' worktime: \n1000 elements {t1:.3f}s;\n10000 elements {t2:.3f}.\n")

    t1 = test_sort_alg_worktime(heap_sort, to_sort=test_100000)
    t2 = test_sort_alg_worktime(heap_sort, to_sort=test_1000000)
    print(f"'{heap_sort.__name__}' worktime: \n100000 elements {t1:.3f}s;\n1000000 elements {t2:.3f}.\n")

    t1 = test_sort_alg_worktime(quick_sort, to_sort=test_100000)
    t2 = test_sort_alg_worktime(quick_sort, to_sort=test_1000000)
    print(f"'{quick_sort.__name__}' worktime: \n100000 elements {t1:.3f}s;\n1000000 elements {t2:.3f}.\n")

    t1 = test_sort_alg_worktime(merge_sort, to_sort=test_100000)
    t2 = test_sort_alg_worktime(merge_sort, to_sort=test_1000000)
    print(f"'{merge_sort.__name__}' worktime: \n100000 elements {t1:.3f}s;\n1000000 elements {t2:.3f}.\n")



