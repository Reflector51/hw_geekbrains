"""
Задание 3

Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return print(f"{self.name} {self.surname} ({self.position})")

    def get_total_income(self):
        return print(f"Общий оклад составяет: {sum(self._income.values())}")


ivan = Position("Иван", "Иванов", "Директор", 150000, 20000)
ivan.get_full_name()
ivan.get_total_income()

artur = Position("Артур", "Иванов", "Зам Директор", 100000, 15000)
artur.get_full_name()
artur.get_total_income()
