"""
Задание 2

Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    __mass: float = 25.0
    _lenght: float
    _width: float

    def __init__(self, lenght: float, width: float):
        self._lenght = lenght
        self._width = width

    def calculate(self, depth: float = 1):
        return (self._lenght * self._width * self.__mass * depth) / 1000


road = Road(20, 5000)
calculation = road.calculate(5)

print(f"{calculation}")


# class Road:
#     def __init__(self, _lenght, _width):
#         self._lenght = _lenght
#         self._width = _width
#
#     def find_mass(self):
#         self.weight = 25
#         self.thickness = 0.005
#         return self._width * self._lenght * self.weight * self.thickness
#
#
# road = Road(int(input("Введите ширину дороги >>> ")), int(input("Введите длину дороги >>> ")))
# print(f'Для покрытия дороги придется использовать {int(road.find_mass())}т. асфальта!')

