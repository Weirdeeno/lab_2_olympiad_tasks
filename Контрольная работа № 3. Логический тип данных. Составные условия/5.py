"""
5.Разработать алгоритм и реализовать программу, дающую ответ на вопрос: находится ли пешка под боем коня.
Белый конь расположен на поле (х, n). Черная пешка расположена на поле (y, m). 
"""

x, n = map(int, input('Введите две координаты расположения коня через пробел: ').split())
y, m = map(int, input('Введите две координаты расположения пешки через пробел: ').split())

k = abs(x - y)
p = abs(n - m)

if k == 1 and p == 2 or k == 2 and p == 1 :
    print('Да')
else:
    print('Нет')
