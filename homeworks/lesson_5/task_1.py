"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

try:
    with open('text_file_1.txt', 'w', encoding='utf-8') as file:
        text = ''
        print('Что запишем в файл? (пустая строка - конец текста)')
        while True:
            user_input = input('>>> ')
            if user_input:
                text += f'{user_input}\n'
            else:
                break
        print(text, file=file)
except IOError:
    print('Произошла неприятнось, имеет место быть ошибка ввода!')
