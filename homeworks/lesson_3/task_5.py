"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def sum_of_number_string(num_string: str, prev_sum: int) -> tuple:
    """Возвращает сумму введённых через пробел чисел + предыдущий результат"""
    num_list = num_string.split()
    result = prev_sum
    cont_sum = True
    for i in num_list:
        try:
            result += int(i)
        except ValueError:
            cont_sum = False

    return result, cont_sum


continue_summation = True
summation = 0
while continue_summation:
    print('*' * 30)
    user_input = input('Введи числа, разделяя пробелами, для выхода - другой символ\n>>> ')
    summation, continue_summation = sum_of_number_string(user_input, summation)
    print(f'Сумма: {summation}\n')

print('Всё, кина не будет, плёнка закончилась!')
