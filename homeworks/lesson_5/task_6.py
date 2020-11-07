"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.

Важно, чтобы для каждого предмета не обязательно были все типы занятий.

Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —

Пример словаря:
    {"Информатика": 170, "Физика": 40, "Физкультура": 30}
"""

subjects = {}

try:
    with open('text_file_6.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
except IOError:
    print('Файл не читается!')

if lines:
    for line in lines:
        idx = line.index(':')
        subj_name = line[:idx]
        hours_str = ''.join([sym for sym in line[idx+1:].strip() if sym.isdigit() or sym.isspace()])
        hours_list = hours_str.split()
        hours_list = [int(num) for num in hours_list]
        subjects[subj_name] = sum(hours_list)
else:
    print('А нечего читать ;-)')

print(f'Предметы и часы:\n\t{subjects}')
