"""
Задание 2

Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_info(name: str = None,
              lastname: str = None,
              year: int = None,
              city: str = None,
              email: str = None,
              phone: str = None):
    """
    Функция карточки пользователя.
    :param name: Имя
    :param lastname: Фамилия
    :param year: Год Рождения
    :param city: Город проживания
    :param email: Активный email
    :param phone: Контактный телефон
    :return: print
    """
    return f"Name= {name}, Lastname= {lastname}, year= {year}, city= {city}, email= {email}, phone= {phone}"

print(user_info(name="Ivan", lastname="K", year=1989, city="Berlin", email="this@email.com", phone="+777777"))
