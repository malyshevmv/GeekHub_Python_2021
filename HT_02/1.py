'''
1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран.
Список можна "захардкодити".
Елементами списку повинні бути як рядки, так і числа.
'''
import random


string = ''
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
n = int(input(f'enter the number of items in the list, but not more than {len(first_words_the_zen_of_python)}: '))
lst = random.sample(first_words_the_zen_of_python, n)
for i in lst:
    string += str(i)
print(f'{lst} --> {string}')