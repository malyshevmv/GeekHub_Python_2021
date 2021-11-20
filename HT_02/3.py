'''
3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
        Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
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
number_from_1_to_3 = random.randrange(1, 3)
list_of_tuples_of_dictionaries_and_lists = []
last_list = []

for _ in range(number_from_1_to_3):
    list_of_tuples_of_dictionaries_and_lists.append(tuple(random.choices(first_words_the_zen_of_python, k = random.randrange(0, 3))))
    list_of_tuples_of_dictionaries_and_lists.append(dict.fromkeys(random.choices(first_words_the_zen_of_python, k = random.randrange(0, 3))))
    list_of_tuples_of_dictionaries_and_lists.append(list(random.choices(first_words_the_zen_of_python, k = random.randrange(0, 3))))
print((list_of_tuples_of_dictionaries_and_lists), '-->', end=' ')

for i in list_of_tuples_of_dictionaries_and_lists:
    if len(i) != 0:
        last_list.append(i)
print(last_list)