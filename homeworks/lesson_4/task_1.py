"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.

В расчете необходимо использовать формулу:
    (выработка в часах * ставка в час) + премия.

Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def salary_calc(hours, rate, bonus=0):
    """Возвращает расчет з/п по формуле (hours * rate) + bonus

    Параметры:
    hours - выработка в часах
    rate - ставка в час
    bonus = премия, если есть (необязательный параметр, по умолчанию - 0)
    """
    try:
        hours = int(hours)
        rate = int(rate)
        bonus = int(bonus)
    except ValueError as e:
        return 0
    result = (hours * rate) + bonus
    return result


_, *data = argv
try:
    salary = salary_calc(*data)
    if salary:
        print(f'Зарплатушка: {salary} настоящих денег.')
    else:
        print('Введите корректные данные!')
except TypeError:
    print('Данные введены не корректно!')
