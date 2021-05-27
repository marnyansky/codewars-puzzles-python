"""
Multiple sorting algorithms compete with each other:
1. My Selection Sort (function written from scratch)
2. My Selection Sort + Python's min() function
3. Python's TimSort
"""

from random import choice, randint
from string import ascii_lowercase as al
from timeit import default_timer as timer

from exec_time import display_function_execution_time as elapsed


def _generate_list_emails(num_emails):
    lst_emails = []
    for _ in range(num_emails):
        new_random_email = f"{choice(al)}.test{randint(0, 1000)}@{choice(al)}.com"  # example: z.test324@e.com
        lst_emails.append(new_random_email)
    return lst_emails


def _find_min_value(raw_lst):
    min_value = raw_lst[0]
    for next_value in raw_lst:
        if next_value < min_value:
            min_value = next_value
    return min_value


def my_selection_sort(raw_lst):
    sorted_lst = []
    for _ in range(len(raw_lst)):
        next_item = _find_min_value(raw_lst)
        sorted_lst.append(next_item)
        raw_lst.remove(next_item)
    return sorted_lst


def my_selection_sort_using_min_function(raw_lst):
    sorted_lst = []
    for _ in range(len(raw_lst)):
        next_item = min(raw_lst)
        sorted_lst.append(next_item)
        raw_lst.remove(next_item)
    return sorted_lst


# list of random emails:
unsorted_lst = _generate_list_emails(1000)

"""Tests:"""
print("--My Selection Sort--")
time_s = timer()
sorted_lst1 = my_selection_sort_using_min_function(unsorted_lst.copy())
# print(*sorted_lst1, sep="\n")
time_f = timer()
elapsed(time_s, time_f)

print("\n--My Selection Sort + Python's min() function--")
time_s = timer()
sorted_lst2 = my_selection_sort(unsorted_lst.copy())
# print(*sorted_lst2, sep="\n")
time_f = timer()
elapsed(time_s, time_f)

print("\n--Python's TimSort--")
time_s = timer()
sorted_lst3 = sorted(unsorted_lst.copy())
# print(*sorted_lst3, sep="\n")
time_f = timer()
elapsed(time_s, time_f)
