"""
Задание 1

Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

_, work_hours, hour_cost, bonus = argv

salary = (float(hour_cost) * float(work_hours) + float(bonus))

print(f"Заработная плата = {salary}")

# python task1.py 8 1200 6500