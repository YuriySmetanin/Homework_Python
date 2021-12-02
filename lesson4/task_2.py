"""Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
import math
import task_1

def my_list_gen(lst):
    prev = None
    for el in lst:
        if prev is not None and el > prev:
            yield el
        prev = el


if __name__ == '__main__':
    try:
        src_list = input('Введите список чисел через пробел: ').split(' ')
        # print(f'Исходный список: {src_list}')
        # Уберем пустые строки и сконвертим в числа
        src_list = [task_1.try_int(x) for x in src_list if x]
        print(f'Исходный список: {src_list}')

        print(f'Результат: {[el for el in my_list_gen(src_list)]}')

        exit(0)
    except Exception as e:
        print(e)
        exit(2)
