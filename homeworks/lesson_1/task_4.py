"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

# какой-то колхоз получился с while-ом
user_number = int(input('Введите положительное число из нескольких цифр\n>>> '))
current_digit = user_number % 10
max_digit = current_digit
current_number = user_number // 10

while current_number // 10 > 0:
    current_digit = current_number % 10
    if current_digit > max_digit:
        max_digit = current_digit
    current_number //= 10
else:
    if current_number > max_digit:
        max_digit = current_number

print(f'Самая большая цифра во введённом вами числе {user_number} - {max_digit}')

# я бы сделал так, ну так, чисто повыделываться, или опозориться ;-)
# user_number = str(user_number)  # чтобы ещё раз не вводить
# max_digit = max([int(i) for i in user_number])
# print(f'Самая большая цифра во введённом вами числе {user_number} - {max_digit}')
#
# # или даже
# print(f'Самая большая цифра во введённом вами числе {user_number} - {max([int(i) for i in user_number])}')
