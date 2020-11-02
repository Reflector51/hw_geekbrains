"""
Задание 4

Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return print(f"{self.name} начал(a) движение!")

    def stop(self):
        return print(f"{self.name} остановилась")

    def turn(self, direction: str):
        return print(f"{self.name} сменила движение: {direction}")

    def show_speed(self):
        return print(f"Текущая скорость {self.name}: {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name} вы привысили максимальный порог скорости!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed >= 40:
            print(f"Внимание водитель {self.name} {self.color} цвета вы привысили максимальный порог скорости!")


class PoliceCar(Car):
    is_police: bool = True


cars = [
    SportCar(180, 'Красного', 'Bmw M6'),
    TownCar(60, 'Черного', 'Lexus GS350'),
    WorkCar(55, 'Жёлтого', 'Mitsubishi Pajero'),
    PoliceCar(120, 'Металического',  'Ford Mustang')
]

cars[0].go()
cars[1].turn("направо")
cars[1].show_speed()
cars[3].stop()

for car in cars:
    car.show_speed()


