"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

# См. стр. 5 методички
# TODO: проверка деления на 0
# TODO: лучше переписать всё с нуля


def ask_for_num(message: str, is_second=False) -> int:
    """Возвращает введённое пользователем число

    Параметры:
    message - инструкция перед вводом пользователя
    is_second - делитель ли, при значении True включается проверка, не допускающая ввода "0"

    При вводе "q" - вернёт None

    """
    while True:
        user_input = input(message)
        try:
            user_num = int(user_input)
        except ValueError as error:
            if user_input.lower() == 'q':
                return
            print('Попробуем ещё разок! :-)')
            continue
        if is_second and user_num == 0:
            print('На ноль делить нельзя!')
            continue
        return user_num


def divide_two_nums(a: float, b: float) -> float:
    """Возвращает результат деления двух чисел"""
    result = a / b
    return result


while True:
    print('*' * 25)
    print('Щя будем поделить!')
    print('*' * 25)
    first_num = ask_for_num('Введите число или "q", для выхода\n>>> ')
    if first_num is None:
        break
    second_num = ask_for_num('Введите ещё одно число (не 0)\n>>> ', True)
    if second_num is None:
        break
    print(divide_two_nums(first_num, second_num), '\n')

print('До свидания!')
