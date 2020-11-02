"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def full_user_data(first_name, last_name, birth_year, city, email, phone_number):
    """Возвращает полные данные о пользователе одной строкой.

    !!! Полученные данные не проверяются !!!

    Именованные параметры:
    first_name - имя
    last_name - фамилия
    birth_year - год рождения
    city - город проживания
    email - тут понятно :-)
    phone_number - номер телефона

    """
    result = f'Вы (ты) - {last_name.title()} {first_name.title()} {birth_year} года рождения, '
    result += f'проживаешь(-те) в г. {city.title()}, мыло: {email}, телефонь: {phone_number}.'
    return result


# Проверка трудоспособности функции full_user_data()
print(full_user_data(first_name='Уасся', last_name='Спичкин', birth_year='1999',
                     city='Урюпинск', email='sam_ty@dot.com', phone_number='+1 (234) 567-89-01'))

