"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

from re import findall

try:
    with open('text_file_2.txt', 'r', encoding='utf-8') as file:
        count_lines = 0
        count_words = []
        count_matches = []

        for line in file:
            count_lines += 1
            count_words.append(len(line.split()))

            # Добавил регулярку, чтобы более точно подсчитать кол-во слов
            # match = findall(r'\b[-A-Za-zА-Яа-яЁё]+\b', line)  # можно так
            match = findall(r'\b[-\w]+\b', line)  # или так
            count_matches.append(len(match))

        print(f'Количество строк в файле: {count_lines}')

        for idx, num in enumerate(count_words, 1):
            print(f'Количество слов в {idx}-й строке: {num} (регулярка: {count_matches[idx-1]})')
except IOError:
    print('Что-то не так с выводом данных!')
