"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return


# Тест
try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    res = divide(a, b)
    if res:
        print(f'{a} / {b} = {res}')
    else:
        print('Деление на ноль')
except ValueError:
    print('Введены некорректные данные')

