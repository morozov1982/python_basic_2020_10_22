"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """Принимает три аргумента, возвращает сумму двух наибольших"""
    sorted_list = [a, b, c]
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] < sorted_list[i + 1]:
            sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
    result = sorted_list[0] + sorted_list[1]
    return result


print(my_func(1, 2, 3))
print(my_func(2, 3, 1))
print(my_func(3, 1, 2))
print(my_func(3, 2, 1))
print(my_func(8, 6, 6))
print(my_func(8, 8, 6))
