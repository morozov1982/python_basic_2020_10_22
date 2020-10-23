"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

digit = input('Введи цифру, мне очень надо\n>>> ')

# вычисляю одним условием
result = int(digit) + int(digit + digit) + int(digit + digit + digit)
print(f'{digit} + {digit + digit} + {digit + digit + digit} = {result}\n')

# создаю несколько переменных и работаю с ними
int_digit = int(digit)
double_digit = int(digit + digit)
triple_digit = int(digit + digit + digit)
second_result = int_digit + double_digit + triple_digit
print(f'Как бы я не вычислял, а:\n{int_digit} + {double_digit} + {triple_digit} = {second_result}')
