'''
Задание 3

Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

month = int(input("Укажите номер месяца >>> "))

year_dict = {
    "Зима": (1, 2, 12),
    "Весна": (3, 4, 5),
    "Лето": (6, 7, 8),
    "Осень": (9, 10, 11)
}
for season, months in year_dict.items():
    if month in months:
        print(f"Время года = {season}")
        break

# while True:
#     month = int(input("Введите номер месяца: "))
#     if 0 < month <= 12:
#         break
#     print('Пожалуйста введите верный номер месяца!')
#
# season_list = ['Зима', 'Весна', 'Лето', 'Осень']
# months_list = {
#     1: "Январь",
#     2: "Февраль",
#     3: "Март",
#     4: "Апрель",
#     5: "Май",
#     6: "Июнь",
#     7: "Июль",
#     8: "Август",
#     9: "Сентябрь",
#     10: "Октябрь",
#     11: "Ноябрь",
#     12: "Декабрь"
# }
#
# if month in range(3, 6):
#     season = season_list[1]
# elif month in range(6, 9):
#     season = season_list[2]
# elif month in range(9, 12):
#     season = season_list[3]
# else:
#     season = season_list[0]
#
# for i, el in enumerate(months_list):
#     if i + 1 == month:
#         print(f'Вы ввели {months_list.get(month)} что соответсвует сезону: {season}')