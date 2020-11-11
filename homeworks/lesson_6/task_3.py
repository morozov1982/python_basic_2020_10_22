"""
3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


# 1-й вариант
class Worker1:
    name = "Уасся"
    surname = "Пупкин"
    position = "Менеджер по уборке прилежащих территорий"
    _income = {"wage": 5000, "bonus": 250}


class Position1(Worker1):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


# Другой вариант
class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        _income = {"wage": 5000, "bonus": 250}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    # 1-й вариант
    pos_1 = Position1()
    name_1 = pos_1.get_full_name()
    income_1 = pos_1.get_total_income()
    print(f'{name_1}: доход - {income_1} копеек.')
    print(f'Должность: {pos_1.position}')

    print('\n' + '=' * 30 + '\n')

    # другой вариант
    pos = Position('James', 'Bond', 'Agent-007', 1285, 351)
    full_name = pos.get_full_name()
    total_income = pos.get_total_income()
    print(f'{full_name}: доход - {total_income} фунтов.')
    print(f'Должность: {pos.position}')
