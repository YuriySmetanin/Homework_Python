"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами. """
from sys import argv


def try_int(num_str, description=''):
    try:
        return int(num_str)
    except ValueError as ex:
        err_msg = f'Ошибка конвертации "{description}": ' if description else ''
        err_msg += str(ex)
        raise ValueError(err_msg)


if __name__ == '__main__':
    try:
        if len(argv) != 4:
            print("Использование: python task_1.py <выработка в часах> <ставка в час> <премия>")
            print("Пример: python task_1.py 200 1000 75000")
            exit(1)

        hours = try_int(argv[1], 'выработка в часах')
        pay_rate = try_int(argv[2], 'ставка в час')
        bonus = try_int(argv[3], 'премия')

        print(f'Зарплата: {hours * pay_rate + bonus}')
        exit(0)
    except Exception as e:
        print(e)
        exit(2)
