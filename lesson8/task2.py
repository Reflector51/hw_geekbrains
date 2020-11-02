"""
Задание 2

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(ZeroDivisionError):
    def __str__(self):
        return "Нельзя делить на ноль!"

    @staticmethod
    def division(x, y):
        try:
            if y == 0:
                raise MyZeroDivisionError()
            return x / y
        except MyZeroDivisionError as err:
            return err


print(MyZeroDivisionError.division(33, 0))
