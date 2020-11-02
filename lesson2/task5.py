'''
Задание 5

Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

rating = [7, 5, 3, 3, 2]

while True:
    try:
        print(f"Рейтинг = {rating}")
        user_rate = int(input("Введите новый рейтинг >>> "))

        rating.append(user_rate)
        rating.sort(reverse=True)

        print(rating)
    except ValueError:
        print("Неверное число")
    except KeyboardInterrupt:
        exit()

# my_list = [7, 5, 3, 3, 2]
# print(f"{my_list} текущая таблица рейтинга")
# count = int(input("Кол-во элементов вы хотите добавить в рейтинг: "))
# c = 1
# while c <= count:
#     c += 1
#     number = int(input("Введите новый элемент для рейтинга: "))
#     repeat = my_list.count(number)
#     for el in my_list:
#         if repeat > 0:
#             i = my_list.index(number)
#             my_list.insert(i + repeat, number)
#             break
#         else:
#             if number > el:
#                 j = my_list.index(el)
#                 my_list.insert(j, number)
#                 break
#             elif number < my_list[len(my_list) - 1]:
#                 my_list.append(number)
#     print(f"{my_list} новая таблица рейтинга")
