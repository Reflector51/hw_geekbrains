"""
Задание 3

Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """ Функция возвращает сумму двух наибольший аргументов  """
    my_list = [a, b, c]
    my_list.remove(min(a, b, c))
    return sum(my_list)


a, b, c = int(input("Число a >>> ")), int(input("Число b >>> ")), int(input("Число c >>> "))

print(my_func(a, b, c))

