"""
6.Разработать алгоритм и реализовать программу, дающую ответ на вопрос: находится ли пешка под боем слона.
Белый слон расположен на поле (х, n). Черная пешка расположена на поле (y, m).
Других фигур на поле нет.
"""

x, n = map(int, input('Введите две координаты расположения слонa через пробел: ').split())
y, m = map(int, input('Введите две координаты расположения пешки через пробел: ').split())

if abs(x - y) == abs(n - m):
    print('Да')
else:
    print('Нет')
