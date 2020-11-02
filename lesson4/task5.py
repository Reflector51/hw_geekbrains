"""
Задание 5

Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce


numbers = [item for item in range(100, 1001) if item % 2 == 0]

multi = reduce(lambda x, y: x * y, numbers, 1)

print(multi)
# def my_func(prev_el, el):
#     return prev_el * el
#
#
# print(f'Перемножение четных элементов в списке: \n{reduce(my_func, [el for el in range(100, 1000 + 1) if el % 2 == 0])}')
