from random import choice, randint
from string import ascii_lowercase as al


def _generate_list_emails(num_emails):
    lst_emails = []
    for _ in range(num_emails):
        new_random_email = f"{choice(al)}.test{randint(0, 1000)}@{choice(al)}.com"  # example: z.test324@e.com
        lst_emails.append(new_random_email)
    return lst_emails


def my_selection_sort(raw_lst):
    # to be implemented
    pass


def my_selection_sort_using_min_function(raw_lst):
    sorted_lst = []
    for _ in range(len(raw_lst)):
        next_item = min(raw_lst)
        sorted_lst.append(next_item)
        raw_lst.remove(next_item)
    return sorted_lst


# list of random emails:
unsorted_lst = _generate_list_emails(10)

# tests:
sorted_lst1 = my_selection_sort_using_min_function(unsorted_lst.copy())
print(*sorted_lst1, sep="\n")

print("-----")
# to be implemented
# sorted_lst2 =
# print(*sorted_lst2, sep="\n")

print("-----")
sorted_lst3 = sorted(unsorted_lst.copy())
print(*sorted_lst3, sep="\n")
