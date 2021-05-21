'''
Story:
You and a group of friends are earning some extra money in the school holidays by re-painting the numbers on people's letterboxes for a small fee.
Since there are 10 of you in the group each person just concentrates on painting one digit! For example, somebody will paint only the 1's, somebody else will paint only the 2's and so on...
But at the end of the day you realise not everybody did the same amount of work.
To avoid any fights you need to distribute the money fairly. That's where this Kata comes in.

Task:
Given the start and end letterbox numbers, write a method to return the frequency of all 10 digits painted.
'''


def paint_letterboxes(start, finish):
    lst = [0] * 10
    for number in range(start, finish + 1):
        for digit in range(0, 10):
            lst[digit] += str(number).count(str(digit))
    return lst


def paint_letterboxes_alt(start, finish):
    lst = [0] * 10
    for number in range(start, finish + 1):
        for str_digit in str(number):
            lst[int(str_digit)] += 1
    return lst


# test of task (kata) https://www.codewars.com/kata/597d75744f4190857a00008d
print(paint_letterboxes(125, 132))  # [1,9,6,3,0,1,1,1,1,1]
print(paint_letterboxes_alt(125, 132))  # [1,9,6,3,0,1,1,1,1,1]
