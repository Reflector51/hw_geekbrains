"""
Задание 3, часть вторая)

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_data = []
translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': "Три",
    'Four': "Четыре"
}
with open("data3_2.txt", 'r', encoding='utf-8') as my_stream:
    for line in my_stream:
        my_val = line.split(" - ")
        if my_val[0] in translate:
            word = translate[my_val[0]]
            my_data.append(word + ' - ' + my_val[1])

my_data = [line.rstrip() for line in my_data]

with open("data3_2_result.txt", 'w', encoding='utf-8') as new_stream:
    for line in my_data:
        print(line, file=new_stream)
