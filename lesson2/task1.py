'''
Задание 1

Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
'''


my_list = [1, complex(5, 6), "string", None, 0.14, [], {}, (), set(), frozenset(), 1 == 1, bytes(1), bytearray(1)]


for i in my_list:
    print(type(i))
