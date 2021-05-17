# https://www.codewars.com/kata/590a924c7dfc1a238d000047/train/python
def perfect_team_of_minimal_size(n, cdts):
    if 0 > n > 10 or len(cdts) == 0:
        return -1
    all_categories = []
    for cdt in cdts:
        all_categories = [category for category in cdt if category not in all_categories]

    count_cdts = 1
    confirmed_categories = []

    cdts = sorted(cdts, reverse=True)
    for cdt in cdts:
        if any(category not in confirmed_categories for category in cdt):
            count_cdts += 1
        for category in cdt:
            if category not in confirmed_categories:
                confirmed_categories.append(category)

    len_cc = len(confirmed_categories)
    if len_cc == 0 or len_cc < n or len_cc < len(all_categories):
        return -1
    return count_cdts


res1 = perfect_team_of_minimal_size(3, [[0, 2], [1, 2], [0, 1], [0]])
print(res1)
print('=====')
res2 = perfect_team_of_minimal_size(6, [[0, 1], [1, 3], [0, 2], [0, 5], [1, 4]])
print(res2)
print('=====')
res3 = perfect_team_of_minimal_size(1, [[], []])
print(res3)
print('=====')
res4 = perfect_team_of_minimal_size(1, [])
print(res4)
print('=====')
res5 = perfect_team_of_minimal_size(2, [[], [0, 1]])
print(res5)
print('=====')
res6 = perfect_team_of_minimal_size(1, [[0], [0]])
print(res6)
print('=====')
res7 = perfect_team_of_minimal_size(2, [[0], [0]])
print(res7)
