"""
Задагие 2

Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

raw_count = 0
with open("data2.txt", 'r') as my_stream:
    for idx, line in enumerate(my_stream, 1):
        print(f"В строке {idx} - {len(line.split())} слов")

