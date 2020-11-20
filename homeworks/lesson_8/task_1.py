"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f'{self.date}'

    @classmethod
    def extract_date(cls, date: str):
        try:
            return tuple(map(int, date.split('-')))
        except ValueError:
            return 'Некорректные данные!'

    @staticmethod
    def is_correct_date(data):
        if not type(data) == str:
            data = str(data)
        day, month, year = [i for i in Date.extract_date(data)]
        m30 = (4, 6, 9, 11)  # месяцы с 30 днями
        m31 = (1, 3, 5, 7, 8, 10, 12)  # месяцы с 31 днём

        if 0 <= year <= 2020 and 0 < month <= 12:
            if (month in m31 and day <= 31) or (month in m30 and day <= 30):
                return True
            elif month == 2:
                """
                кратен 400, — високосный
                остальные, кратные 100, — невисокосные
                остальные годы, номер которых кратен 4, — високосные
                """
                if year % 4 or (not year % 100 and year % 400):
                    return day <= 28
                else:
                    return day <= 29
        return False


if __name__ == '__main__':
    print(Date.extract_date('20-08-1052'))
    print(Date.extract_date('20-08-jazz'))

    # Куча проверок, в основном из-за високосного года
    date_1 = Date('20-08-1052')
    print(date_1, '->', Date.is_correct_date(str(date_1)))  # Отправляем строку на проверку

    date_2 = Date('20-08-2050')
    print(date_2, '->', Date.is_correct_date(date_2))  # Отправляем объект Date, проверяем преобразование внутри функции

    date_3 = Date('20-00-2010')
    print(date_3, '->', Date.is_correct_date(str(date_3)))

    date_4 = Date('20-13-2010')
    print(date_4, '->', Date.is_correct_date(str(date_4)))

    date_5 = Date('30-11-2010')
    print(date_5, '->', Date.is_correct_date(str(date_5)))

    date_6 = Date('31-11-2010')
    print(date_6, '->', Date.is_correct_date(str(date_6)))

    date_7 = Date('28-02-2010')
    print(date_7, '->', Date.is_correct_date(str(date_7)))

    date_8 = Date('29-02-2010')
    print(date_8, '->', Date.is_correct_date(str(date_8)))

    date_9 = Date('29-02-2011')
    print(date_9, '->', Date.is_correct_date(str(date_9)))

    date_10 = Date('29-02-1900')
    print(date_10, '->', Date.is_correct_date(str(date_10)))

    date_11 = Date('29-02-1600')
    print(date_11, '->', Date.is_correct_date(str(date_11)))

    date_12 = Date('29-02-2020')
    print(date_12, '->', Date.is_correct_date(str(date_12)))

    # assert я тоже знаю просто хочется видеть результаты наглядно :-)
    assert Date.is_correct_date(str(date_12)), f'{date_12} очень неправильная дата'
    assert Date.is_correct_date(str(date_2)), f'{date_2}: год за пределами допустимого диапазона'
