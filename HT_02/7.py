'''
7. Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.
                Приклад словника (можете використовувати свій):
                dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
                Вихідний результат:
                MIN: 10
                MAX: 60
'''
import random


first_words_the_zen_of_python = [
        1, 'Beautiful',
        2, 'Explicit',
        3, 'Simple',
        4, 'Complex',
        5, 'Flat',
        6, 'Sparse',
        7, 'Readability',
        8, 'Special',
        9, 'Although',
        10, 'Errors',
        11, 'Unless',
        12, 'In',
        13, 'There',
        14, 'Although',
        15, 'Now',
        16, 'Although',
        17, 'If',
        18, 'If',
        19, 'Namespaces'
]
dict_data = {}
for i in first_words_the_zen_of_python:
    dict_data[i] = random.randrange(0, 100)
lst_values = list(dict_data.values())
print(f'MIN: {min(lst_values)} \nMAX: {max(lst_values)}')
'''
for key, value in dict_data.items():
    print(key, ':', value)
'''