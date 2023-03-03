"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# Write a program that converts given string to datetime object
import datetime

sample1 = 'Jan 1 2014 2:43PM'
dt1 = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p')
print(dt1)
sample2 = '14:20 10/12/22'  # YY/MM/DD
dt2 = datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d')
print(dt2)
sample3 = 'Tuesday, September 24, 2019'
dt3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
print(dt3)
sample4 = '01.01.1970 - 00:00:01'
dt4 = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print(dt4)

