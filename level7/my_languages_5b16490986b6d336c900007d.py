"""
Task:
You are given a dictionary/hash/object containing some languages and your test results in the given languages.
Return the list of languages where your test score is at least 60, in descending order of the results.
Note: the scores will always be unique (so no duplicate values)
Examples
{"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}     -->  []

Hint: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
"""

from timeit import default_timer as timer

from exec_time import display_function_execution_time as elapsed


def my_languages(results):
    tmp_dict = sorted(results.items(), key=lambda item: item[1])
    tmp_dict.reverse()
    return [k for k, v in tmp_dict if v >= 60]


def my_languages_alt(results):
    return sorted((l for l, r in results.items() if r >= 60), reverse=True, key=results.get)


# tests of task (kata) id = 5b16490986b6d336c900007d
print("--My Solution--")
time_s = timer()
my_languages({"Java": 10, "Ruby": 80, "Python": 65})  # test, expected: ["Ruby", "Python"]
my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71})  # test, expected: ["Dutch", "Greek", "Hindi"]
my_languages({"C++": 50, "ASM": 10, "Haskell": 20})  # test, expected: []
time_f = timer()
elapsed(time_s, time_f)

print("--Alternative Solution--")
time_s = timer()
my_languages_alt({"Java": 10, "Ruby": 80, "Python": 65})  # test, expected: ["Ruby", "Python"]
my_languages_alt({"Hindi": 60, "Dutch": 93, "Greek": 71})  # test, expected: ["Dutch", "Greek", "Hindi"]
my_languages_alt({"C++": 50, "ASM": 10, "Haskell": 20})  # test, expected: []
time_f = timer()
elapsed(time_s, time_f)
