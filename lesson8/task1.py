"""
Задание 1

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, my_date):
        self.my_date = my_date

    @classmethod
    def day_number(cls, my_date):
        return [int(x) for x in my_date.split("-")]

    @staticmethod
    def check_data_day(day, month, year):
        result = ""
        if not (1 <= day <= 31):
            result = "Неправильный день"

        if not (1 <= month <= 12):
            result = "Неправильный месяц"

        if not (1500 <= year <= 2100):
            result = "Неправильный год"

        return result


print(Data.day_number("12-12-2020"))
print(Data.check_data_day(21, 12, 2021))



