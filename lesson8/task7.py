"""
Задание 7

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class NumberComplex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 'x + y * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.x * other.x - (self.x * other.y)} + {self.y * other.x} * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.x + other.x} + {self.y + other.y} * i'

    def __str__(self):
        return f'z = {self.x} + {self.y} * i'


z_1 = NumberComplex(1, -2)
z_2 = NumberComplex(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)