"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

try:
    with open('text_file_3.txt', 'r', encoding='utf-8') as file:
        employees = dict(map(lambda l: l.split(), [line for line in file]))

        low_salary = ', '.join([em[0] for em in employees.items() if int(em[1]) < 20000])
        print(f'Фамилии сотрудников с зарплатой менее 20 тыс.: {low_salary}')

        salaries_list = [int(em[1]) for em in employees.items()]
        average_salary = sum(salaries_list) // len(salaries_list)
        print(f'Средняя заработная плата: {average_salary}')

except IOError:
    print('Не могу прочитать файл!')
