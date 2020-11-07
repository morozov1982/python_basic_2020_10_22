"""
4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
new_strings = ''

try:
    with open('text_file_4.txt', 'r', encoding='utf-8') as file:
        for line in file:
            word = line.split()[0]
            new_strings += line.replace(word, num_dict[word.lower()].title())
except IOError:
    print('Не удаётся считать данные')


try:
    with open('text_file_4_new.txt', 'w', encoding='utf-8') as file:
        file.write(new_strings)
except IOError:
    print('Не удаётся считать/записать данные')
