"""
3.	Разработать программу, которая по данному натуральному числу N и вещественному числу x  вычисляет сумму S(N, x) = 1/0! + x/1! + ... + xN/N!.
Требуется, чтобы количество операций (выполненных команд присваивания) было бы не более C*n для  некоторой константы С.
"""


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


n = int(input('Введите натуральное число: '))
x = int(input("Введите х: "))
C = int(input("Введите константу С: "))
s = 1

for n in range(1, n * C):
    j = factorial(n)
    s = x * n / j
print('Cумма ряда =', s)
