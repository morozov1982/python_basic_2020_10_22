"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

    Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

    Пример списка: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

companies = []
total_companies = 0
profit_companies = 0
total_profit = 0
summary_profit = 0
average_profit = 0
total_average_profit = 0
final_json_list = []

try:
    with open('text_file_7.txt', 'r', encoding='utf-8') as file:
        for line in file:
            company = [int(el) if el.isdigit() else el for el in line.split()]
            company_profit = company[-2] - company[-1]
            company.append(company_profit)

            print(f'Прибыль {company[1]} "{company[0]}" составляет {company_profit} денег')

            companies.append(company)

            if company_profit > 0:
                profit_companies += 1
                summary_profit += company_profit
            total_profit += company_profit
except IOError:
    print('Имеет место быть ошибка ввода!')

total_companies = len(companies)
average_profit = summary_profit // profit_companies

print(f'Средняя прибыль успешных компаний: {average_profit}')

# JSON
final_json_list.append({comp[0]: comp[-1] for comp in companies})
total_average_profit = total_profit // total_companies
final_json_list.append({"average_profit": total_average_profit})

try:
    with open('profit_of_companies.json', 'w') as file:
        json.dump(final_json_list, file, ensure_ascii=False)
except IOError:
    print('Ну удаётся произвести запись в JSON-файл!')
