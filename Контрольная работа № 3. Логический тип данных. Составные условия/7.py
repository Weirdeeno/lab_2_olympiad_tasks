"""
7.Разработать алгоритм и реализовать программу, дающую ответ находится ли черная шашка под боем белой дамки.
Белая дамка расположена на поле (х, n). Черная шашка расположена на поле (y, m). (Других фигур на доске нет).
"""

x, n = map(int, input('Введите две координаты расположения дамки через пробел: ').split())
y, m = map(int, input('Введите две координаты расположения шашки через пробел: ').split())

if abs(x - y) == abs(n - m) or x == y or n == m:
    print('Да')
else:
    print('Нет')

