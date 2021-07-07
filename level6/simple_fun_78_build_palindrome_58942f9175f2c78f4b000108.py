"""
https://www.codewars.com/kata/58942f9175f2c78f4b000108/train/python
Description:
"Given a string str, find the shortest possible string which can be achieved
by adding characters to the end of initial string to make it a palindrome.
Example:
For str = "abcdc", the output should be "abcdcba"

A string consisting of lowercase latin letters.
Constraints: 3 ≤ str.length ≤ 10"
"""


from timeit import default_timer as timer
import pytest

# before launching pytest tests comment exec_time import below:
# from exec_time import display_function_execution_time as elapsed


def _is_palindrome(palindrome_candidate):
    return palindrome_candidate == palindrome_candidate[::-1]


def my_build_palindrome(s):
    if not isinstance(s, str):
        raise ValueError('Function accepts only strings')
    if len(s) <= 1 or _is_palindrome(s):
        return s
    # now s >= 2, for example: "ab"

    """
    for "cdaf":
        loop 1: s + "c"     (indices: 0 -> reverse)
        loop 2: s + "dc"    (indices: 0, 1 -> reverse)
        loop 3: s + "adc"   (indices: 0, 1, 2 -> reverse)
    """
    substr = ''
    for ch in s:
        substr += ch
        shortest_palindrome = s + substr[::-1]
        if _is_palindrome(shortest_palindrome[:]):
            return shortest_palindrome
    return Exception('Unable to return result. Please, check the string or environment')


def alt_build_palindrome(s):
    suffix = ""
    for ch in s:
        pal = s + suffix
        if pal == pal[::-1]:
            return pal
        suffix = ch + suffix


@pytest.mark.tryfirst
def test_task():
    assert my_build_palindrome("cdaf") == "cdafadc"
    assert my_build_palindrome("abcdc") == "abcdcba"
    assert my_build_palindrome("ababab") == "abababa"
    assert my_build_palindrome("abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba"


def test_alt_solutions():
    assert alt_build_palindrome("cdaf") == "cdafadc"
    assert alt_build_palindrome("abcdc") == "abcdcba"
    assert alt_build_palindrome("ababab") == "abababa"
    assert alt_build_palindrome("abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba"


# time measurements
# if __name__ == '__main__':
#     time_s = timer()
#     my_build_palindrome("cdaf")
#     my_build_palindrome("abcdc")
#     my_build_palindrome("ababab")
#     my_build_palindrome("abcdefghijklmnopqrstuvwxyz")
#     time_f = timer()
#     elapsed(time_s, time_f, function_name="my_build_palindrome()")
#
#     time_s = timer()
#     alt_build_palindrome("cdaf")
#     alt_build_palindrome("abcdc")
#     alt_build_palindrome("ababab")
#     alt_build_palindrome("abcdefghijklmnopqrstuvwxyz")
#     time_f = timer()
#     elapsed(time_s, time_f, function_name="alt_build_palindrome()")
