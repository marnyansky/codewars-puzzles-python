"""
Task:
You need to make a function multiply_all which takes a list of integers as an argument.
This function must return another function, which takes a single integer as an argument and returns a new list.
The returned list should consist of each of the elements from the first list multiplied by the integer.
Example: multiply_all([1, 2, 3])(2); // => [2, 4, 6]
You must not mutate the original list.

Hint: function currying: https://stackoverflow.com/questions/24881604/when-should-i-use-function-currying-in-python
"""

from timeit import default_timer as timer

from exec_time import display_function_execution_time as elapsed


def multiply_all(nums):
    def factor(f):
        return [n * f for n in nums]
    return factor


def multiply_all_alt(nums: list):
    return lambda factor: [n * factor for n in nums]


# test of task (kata) id = 586909e4c66d18dd1800009b
time_s = timer()
print(
    multiply_all([1, 2, 3])(5)  # test, expected: [5, 10, 15]
)
time_f = timer()
elapsed(time_s, time_f)
print('----')
time_s = timer()
print(
    multiply_all_alt([1, 2, 3])(5)  # test, expected: [5, 10, 15]
)
time_f = timer()
elapsed(time_s, time_f)
