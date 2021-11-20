'''
5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити).
Словник для роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
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
dict_1 = dict.fromkeys(random.choices(first_words_the_zen_of_python, k = random.randrange(0, 3)), 'dictionary 1')
dict_2 = dict.fromkeys(random.choices(first_words_the_zen_of_python, k = random.randrange(0, 3)), 'dictionary 2')
dict_3 = dict.fromkeys(random.choices(first_words_the_zen_of_python, k = random.randrange(0, 3)), 'dictionary 3')
initial_dictionary = {}
initial_dictionary.update(dict_1)
initial_dictionary.update(dict_2)
initial_dictionary.update(dict_3)
print(initial_dictionary)

value_initial_dictionary = []
for key, value in initial_dictionary.items():
    value_initial_dictionary.append(value)
values_without_repeats = list(set(value_initial_dictionary))

last_dict = {}
for i in values_without_repeats:
    for key, value in initial_dictionary.items():
        if initial_dictionary[key] == i:
            last_dict[key] = i
            break

print(last_dict)