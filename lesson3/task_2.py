"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def user_info(firstname, lastname, birthdate, city, email, phone):
    fields = ["имя: ", 'фамилия: ', 'год рождения: ', 'город проживания: ', 'email: ', 'телефон: ']
    res_str = ''
    for t in zip(fields, [firstname, lastname, birthdate, city, email, phone]):
        res_str += t[0] + t[1] + ", "
    print(res_str[:-2])


# test
user_info(firstname="Петр", lastname="Иванов", birthdate="04.08.1977", city="Урюпинск",
          email="ivanov@kremlin.ru", phone="112")

