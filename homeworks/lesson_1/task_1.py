"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

str_variable_double = "Работаю со строковой переменной в \"двойных кавычах\" ;-)"
str_variable_single = 'Строка в \'одинарных кавычках\''
print(str_variable_double)
print(str_variable_single)

int_variable = 951
float_variable = 123.654
print(f'Целочисленное: {int_variable}\nВещественное: {float_variable}\n')

print('***** Поработаем с вводом *****')
user_name = input('Введите имя: ')
favorite_year = input('Любимый год: ')
print(f'Я тебя вычислил, тебя зовут {user_name} и ты любишь {favorite_year} год!\n')

print('***** Хотелось бы уточнить *****')
two_is_a_few = input('Две строки - это несколько?\n(Да/нет): ')
favorite_number = input('Любимое число: ')
print(f'Спасибо за позитивный ответ "{two_is_a_few}",\nлюбимое число {favorite_number}, тоже неплохо!\n')
