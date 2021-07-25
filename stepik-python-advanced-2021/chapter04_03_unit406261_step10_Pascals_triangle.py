"""
https://stepik.org/lesson/416753/step/10?thread=solutions&unit=406261
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму.
В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.
0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....
На вход программе подается число n. Напишите программу, которая возвращает указанную строку
треугольника Паскаля в виде списка (нумерация строк начинается с нуля).
"""

from timeit import default_timer as timer
from exec_time import display_function_execution_time as elapsed


def pascals_triangle(key_num=4096):
    if not key_num:  # 0
        return [1]

    prev = [1, 1]
    for i in range(key_num):
        """
        build new temporary list
        fill temporary list (thus getting a result)
        "remember" list to store data for building a new list
        """
        curr = [1] + [0] * i + [1]
        for j in range(1, i + 1):
            curr[j] = prev[j - 1] + prev[j]
        prev = curr

    return curr

def pascals_triangle_alt1(key_num=4096):
    lst = [1]
    for i in range(key_num):
        for j in range(len(lst) - 1):
            lst[j] = lst[j] + lst[j + 1]
        lst.insert(0, 1)
    return lst

def pascals_triangle_alt2(key_num=4096):
    lst = [1]
    for _ in range(key_num):
        lst = [a + b for a, b in zip([*lst, 0], [0, *lst])]
    return lst


# algorithms' efficiency measurements
if __name__ == '__main__':
    time_s = timer()
    print(pascals_triangle())
    time_f = timer()
    elapsed(time_s, time_f, function_name="pascals_triangle()")

    time_s = timer()
    print(pascals_triangle())
    time_f = timer()
    elapsed(time_s, time_f, function_name="pascals_triangle_alt1()")

    time_s = timer()
    print(pascals_triangle())
    time_f = timer()
    elapsed(time_s, time_f, function_name="pascals_triangle_alt2()")
