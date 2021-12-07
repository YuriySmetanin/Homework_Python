"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


def my_func(a, b, c):
    tmp = [a, b, c]
    tmp.sort()
    return sum(tmp[-2:])


# То же для произвольного списка
def my_func2(*args):
    return sum(sorted(args)[-2:])


# И то же лямбдой
my_lambda = lambda *args: sum(sorted(args)[-2:])

# Тест. Ожидаем 19
print(my_func(10, 2, 9))
print(my_func2(1, 9, 3, 7, 10, 0, 2))
print(my_lambda(1, 9, 3, 7, 10, 0, 2))
