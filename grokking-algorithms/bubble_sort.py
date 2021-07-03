"""
Classic implementation of bubble sort number sorting algorithm:
https://www.programiz.com/dsa/bubble-sort
"""

from time import sleep
import numpy as np
from timeit import default_timer as timer

from exec_time import display_function_execution_time as elapsed


def _build_large_list_of_nums(amount=10_000):
    nums = []
    for i in range(amount):
        nums.append(np.random.randint(low=0, high=amount))
    return nums


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def timsorted(lst):
    return sorted(lst)


if __name__ == '__main__':
    nums1 = _build_large_list_of_nums()
    nums2 = _build_large_list_of_nums()
    # print(nums)

    """Tests:"""
    print("\n--Bubble sort/Programiz--")
    sleep(1)
    time_s = timer()
    sorted_lst1 = bubble_sort(nums1)
    # print(*sorted_lst1, sep=" ")
    time_f = timer()
    elapsed(time_s, time_f)


    print("\n--Python 3.9.0 built-in TimSort--")
    sleep(1)
    time_s = timer()
    sorted_lst2 = timsorted(nums2)
    # print(*sorted_lst3, sep=" ")
    time_f = timer()
    elapsed(time_s, time_f)
