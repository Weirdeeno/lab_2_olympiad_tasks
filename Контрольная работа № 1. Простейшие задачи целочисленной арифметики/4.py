''' 4.	Составить алгоритм и разработать программу,
которая по числу месяца Октябрь текущего года вычисляет номер дня недели,
который приходится это число.
(Счет номеров дней недели начинается с понедельника.)'''


import datetime

d = int(input('Введите день: '))
date = datetime.datetime(
    year = 2022,
    month = 2,
    day = d)
print('День недели -',date.strftime('%A'))
