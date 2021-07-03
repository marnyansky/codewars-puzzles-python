# TODO: merge_sort
# TODO: selection_sort (classic)
# TODO: further sorting algorithms from "Grokking algorithms" by A.Bhargava

"""
Multiple sorting algorithms compete with each other:
A. mergesortish_quicksort: StackOverflow v01: https://stackoverflow.com/posts/18262384/revisions
B. quicksort_book: book "Grokking algorithms" by A.Bhargava - chapter 4, page 92
C. My Selection Sort (function written from scratch)
D. My Selection Sort + Python's min() function
E. Classic implementation of bubble sort
F. Python's TimSort
"""

from random import choice, randint
from string import ascii_lowercase as al
from time import sleep
from timeit import default_timer as timer

from exec_time import display_function_execution_time as elapsed


# generates random list of emails
def _generate_list_emails(num_emails):
    lst_emails = []
    for _ in range(num_emails):
        new_random_email = f"{choice(al)}.test{randint(0, 10)}@{choice(al)}.com"  # example: j.test1@p.com, allow duplicates
        lst_emails.append(new_random_email)
    return lst_emails


# selection sort helper
def _find_min_value(raw_lst):
    min_value = raw_lst[0]
    for next_value in raw_lst:
        if next_value < min_value:
            min_value = next_value
    return min_value


# A
def mergesortish_quicksort(lst):
    less = []
    equal = []
    greater = []

    if len(lst) > 1:
        pivot = lst[0]
        for x in lst:
            if x == pivot:
                equal.append(x)
            elif x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
        return mergesortish_quicksort(less) + equal + mergesortish_quicksort(greater)
    else:
        return lst


# B
def quicksort_book(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [i for i in lst[1:] if i <= pivot]
    greater = [i for i in lst[1:] if i > pivot]
    return quicksort_book(less) + [pivot] + quicksort_book(greater)


# C
def my_selection_sort(raw_lst):  # pop()?
    sorted_lst = []
    for _ in range(len(raw_lst)):
        next_item = _find_min_value(raw_lst)
        sorted_lst.append(next_item)
        raw_lst.remove(next_item)
    return sorted_lst


# D
def my_selection_sort_using_min_function(raw_lst):  # pop()?
    sorted_lst = []
    for _ in range(len(raw_lst)):
        next_item = min(raw_lst)
        sorted_lst.append(next_item)
        raw_lst.remove(next_item)
    return sorted_lst


# E
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# F
def timsort(lst):
    return sorted(lst)


# list of random emails:
unsorted_lst = _generate_list_emails(10_000)

"""Tests:"""
print(f"Sorting a list of {len(unsorted_lst)} random emails...")

print("A. Quicksort in merge sort style \t", end=" ")
sleep(1)
time_s = timer()
sorted_lst_a = mergesortish_quicksort(unsorted_lst.copy())
# print(*sorted_lst_a, sep=" ")
time_f = timer()
elapsed(time_s, time_f)


print("B. Quicksort/Grokking algs \t", end=" ")
sleep(1)
time_s = timer()
sorted_lst_b = quicksort_book(unsorted_lst.copy())
# print(*sorted_lst_b, sep=" ")
time_f = timer()
elapsed(time_s, time_f)


print("C. My Selection Sort \t", end=" ")
sleep(1)
time_s = timer()
sorted_lst_c = my_selection_sort_using_min_function(unsorted_lst.copy())
# print(*sorted_lst_c, sep=" ")
time_f = timer()
elapsed(time_s, time_f)


print("D. My Selection Sort + Python's min() function \t", end=" ")
sleep(1)
time_s = timer()
sorted_lst_d = my_selection_sort(unsorted_lst.copy())
# print(*sorted_lst_d, sep=" ")
time_f = timer()
elapsed(time_s, time_f)


print("E. Bubble sort \t", end=" ")
sleep(1)
time_s = timer()
sorted_lst_e = bubble_sort(unsorted_lst.copy())
# print(*sorted_lst_e, sep=" ")
time_f = timer()
elapsed(time_s, time_f)


print("F. Python's TimSort \t", end=" ")
sleep(1)
time_s = timer()
sorted_lst_f = timsort(unsorted_lst.copy())
# print(*sorted_lst_f, sep=" ")
time_f = timer()
elapsed(time_s, time_f)
