"""
Задание 6

Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

int_func = lambda txt: txt.title()

# Не понял где в этом задании подвох?) title отлично справляется как в первом так и во втором случае

# def int_func(txt):
#    return ' '.join(s[:1].upper() + s[1:] for s in txt.split(' '))

print(int_func("text"))
print(int_func("text many worlds in str"))
