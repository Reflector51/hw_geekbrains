"""
Задание 1

1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    value: list = []

    def __init__(self, value: list):
        self.value = value

    def __add__(self, other: 'Matrix'):
        try:
            rows_count = len(self.value)
            item_count = len(self.value[0])

            new_value = [
                [
                    self.value[row][idx] + other.value[row][idx]
                    for idx in range(item_count)
                ]
                for row in range(rows_count)
            ]

            return Matrix(new_value)
        except IndexError:
            print("Ошибка - Матрицы разного размера")
            exit(1)

    def __str__(self):
        return "\n".join(
            str(row).strip('[]').replace(",", '')
            for row in self.value
        )


neo = Matrix(
    [
        [3, 5, 32],
        [2, 4, 6],
        [-1, 64, -8]
    ]
)
trinity = Matrix(
    [
        [7, 15, 18],
        [8, 16, 44],
        [11, -44, 58]
    ]
)

print(neo + trinity)
