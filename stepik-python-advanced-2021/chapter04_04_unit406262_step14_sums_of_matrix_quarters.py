"""
https://stepik.org/lesson/416754/step/14?unit=406262
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями:
верхнюю, нижнюю, левую и правую. Напишите программу, которая вычисляет сумму элементов:
верхней четверти; правой четверти; нижней четверти; левой четверти.
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы (целые числа) построчно через пробел.
Программа должна вывести текст в соответствии с условием задачи. Элементы диагоналей не учитываются.
"""


class Solution:

    @property
    def quarters(self):
        return ['Верхняя четверть: ',
                'Правая четверть: ',
                'Нижняя четверть: ',
                'Левая четверть: ']


    def _prepare_result(self, *args):
        res = ''
        if not args or len(args) < 4:
            for q in self.quarters:
                res += q + '0\n'
            return res.strip()

        for i in range(len(self.quarters)):
            res += self.quarters[i] + f'{args[i+1]}\n'
        return res.strip()


    def calc_per_quarter(self):
        n = int(input())
        if n < 3:
            return self._prepare_result(self)

        sum_upr, sum_rgt, sum_lwr, sum_lft = 0, 0, 0, 0
        matrix = [list(map(int, input().split())) for i in range(n)]

        for i in range(n):
            for j in range(n):
                if i < j and i < n-1-j:
                    sum_upr += matrix[i][j]
                elif i > j and i < n-1-j:
                    sum_lft += matrix[i][j]
                elif i < j and i > n-1-j:
                    sum_rgt += matrix[i][j]
                elif i > j and i > n-1-j:
                    sum_lwr += matrix[i][j]

        return self._prepare_result(self, sum_upr, sum_rgt, sum_lwr, sum_lft)
# the end of my solution


def calc_per_quarter_alt1():
    n = int(input())
    matrix = [[int(i) for i in input().split()] for _ in range(n)]
    sums = [0] * 4
    quarters = ('Верхняя', 'Правая', 'Нижняя', 'Левая')
    for i in range(n // 2):
        for j in range(i + 1, n - i - 1):
            for k, e in enumerate((matrix[i][j], matrix[j][~i], matrix[~i][j], matrix[j][i])):
                sums[k] += e

    print(*(f'{q} четверть: {sums[i]}' for i, q in enumerate(quarters)), sep='\n')


def calc_per_quarter_alt2():
    n = int(input())
    matrix = [[*map(int, input().split())] for _ in range(n)]
    quarters = {
        'Верхняя четверть': lambda i, j: j > i < n - 1 - j,
        'Правая четверть': lambda i, j: j > i > n - 1 - j,
        'Нижняя четверть': lambda i, j: j < i > n - 1 - j,
        'Левая четверть': lambda i, j: j < i < n - 1 - j,
    }

    for qr, f in quarters.items():
        print(f'{qr}: {sum(matrix[i][j] for i in range(n) for j in range(n) if f(i, j))}')
