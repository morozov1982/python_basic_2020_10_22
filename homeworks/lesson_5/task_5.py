"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

numbers = '5 18 64 23 6 1 8 75 35 26 49'

try:
    with open('text_file_5.txt', 'w+', encoding='utf-8') as file:
        file.write(numbers)
        file.tell()  # проверил, где указатель, оказалось в конце
        file.seek(0)  # возвращаем в начало
        numbers_str = file.read()  # файл нормально читается
except IOError:
    print('Ошибка записи/чтения файла!')

numbers_sum = sum([int(n) for n in numbers_str.split()])

print(f'Сумма чисел: {numbers_str}\nРавна: {numbers_sum}\n')

print('Если хочется красиво, как в математике:')
print(f'{" + ".join(numbers_str.split())} = {numbers_sum}')
