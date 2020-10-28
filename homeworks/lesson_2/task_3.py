"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# Через list, декабрь вставил в начало, чтобы сократить количество условий
months_list = ['декабрь', 'январь', 'февраль',
               'март', 'апрель', 'май',
               'июнь', 'июль', 'август',
               'сентябрь', 'октябрь', 'ноябрь']

seasons_list = ['зима', 'весна', 'лето', 'осень']
user_num = None

print('Введи чило от 1 до 12, а я назову месяц и время года к которому он относится.')
print('Чтобы выйти, просто нажми Enter')

while True:
    user_num = input('>>> ')
    if not user_num:
        break
    if not user_num.isdigit():
        print('\nПопробуем ещё разок, нужно ввести число от 1 до 12')
    else:
        # Поскольку ещё не проходили исключения, делаю вложенные условия
        user_num = int(user_num)
        if user_num < 1 or user_num > 12:
            print('\nНужно ввести число от 1 до 12')
            continue

        user_num = 0 if user_num == 12 else user_num
        month = months_list[user_num]
        season = seasons_list[user_num // 3].capitalize()
        print(f'{season}, {month} как-никак!\n')

print('Всё, наигрались!')

# Через dict, без названий месяцев
seasons_dict = {(1, 2, 12): 'Зима', (3, 4, 5): 'Весна', (6, 7, 8): 'Лето', (9, 10, 11): 'Осень'}

print('\nВведи номер месяца.')
print('Чтобы выйти, нажми Enter')

while True:
    user_num = input('>>> ')
    if not user_num:
        break
    if not user_num.isdigit():
        print('\nПопробуем ещё разок, нужно ввести число от 1 до 12')
    else:
        user_num = int(user_num)
        if user_num < 1 or user_num > 12:
            print('\nНужно ввести число от 1 до 12')
            continue

        for keys, value in seasons_dict.items():
            if user_num in keys:
                print(f'{value} однако!\n')

print('Окончательно, наигрались!')
