"""
Задание 7

Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
for el in fact(n). Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from itertools import count
from math import factorial

def fact(number: int):
    temp_result = 1

    if number <= 0:
        yield temp_result

    for x in range(1, number + 1):
        temp_result *= x
        yield temp_result

N = 4

for el in fact(N):
    print(el)
#
# def fibo_gen():
#     for el in count(1):
#         yield factorial(el)
#
#
# x = 0
# for el in fibo_gen():
#     if x > 15:
#         break
#     else:
#         print(el)
#         x += 1



