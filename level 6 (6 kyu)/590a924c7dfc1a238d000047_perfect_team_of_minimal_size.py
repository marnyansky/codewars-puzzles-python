"""
# https://www.codewars.com/kata/590a924c7dfc1a238d000047/train/python
# Should be fixed some day! Tests: Passed: 326 Failed: 182

Description:
You are looking for teammates for an oncoming intellectual game in which you will have to answer some questions.
It is known that each question belongs to one of the n categories. A team is called perfect if for each category
there is at least one team member who knows it perfectly. You don't know any category well enough, but you are
going to build a perfect team. You consider several candidates, and you are aware of the categories each of them
knows perfectly. There is no restriction on the team size, but smaller teams gain additional bonus points. Thus,
you want to build a perfect team of minimal possible size. Find this size (and don't forget to count yourself!)
or determine that it is impossible to form a perfect team from the candidates you have.

Input/Output
[input] integer n representing the number of categories
1 ≤ n ≤ 10.
[input] 2D integer array candidates

For each valid i, candidates[i] is an array of different integers representing
indices of the categories which the i-th candidate knows perfectly.

0 ≤ candidates.length ≤ 10,
0 ≤ candidates[i].length < n,
0 ≤ candidates[i][j] < n.

[output] an integer
The minimal possible size of the perfect team or -1 if you can't build it.

Example
For n = 3 and candidates = [[0, 2], [1, 2], [0, 1], [0]]
the output should be  3.

You can build a perfect team of size 3 in any of the following ways:
yourself, candidate number 1 (1-based) and candidate number 2
[] + [0, 2] + [1, 2] = [0, 1, 2]
yourself, candidate number 1 and candidate number 3
[] + [0, 2] + [0, 1] = [0, 1, 2]
yourself, candidate number 2 and candidate number 3
[] + [1, 2] + [0, 1] = [0, 1, 2]
yourself, candidate number 2 and candidate number 4
[] + [1, 2] + [0] = [0, 1, 2]
"""


# bug is here probably
def is_not_duplicate(cdt, cdts):
    for c in cdts:
        if len(c) == 0:
            cdts.remove(c)
    if len(cdts) == 1:
        return True

    dupl = []
    for i in range(len(cdt)):
        for j in range(len(cdts)):
            if cdt[i] == any(v for v in cdts[j]):
                dupl.append(cdt[i])
                continue
    return len(dupl) != len(cdt)


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
            if is_not_duplicate(cdt, cdts):
                count_cdts += 1
        for category in cdt:
            if category not in confirmed_categories:
                confirmed_categories.append(category)

    len_cc = len(confirmed_categories)
    if len_cc < n or len_cc < len(all_categories):
        return -1
    return count_cdts
