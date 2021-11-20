'''
2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення.
   Список із кортежів можна захардкодити. Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
   Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком). Кількість елементів в кортежу повинна бути різна.
             Приклад списка котежів: [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
             Очікуваний результат, якщо введено "100":
        Expected Output: [(10, 20, "100"), (40, 50, 60, "100"), (80, "100"), ("100",)]
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
number_from_1_to_5 = random.randrange(1, 5)
print('кількість кортежів у списку', number_from_1_to_5)
list_of_tuples = []
for _ in range(number_from_1_to_5):
    list_of_tuples.append(tuple(random.choices(first_words_the_zen_of_python, k = random.randrange(1, 5))))
print('список кортежів', (list_of_tuples))
value = input('Enter the value that will replace the last element of the tuple: ')
last_list = [] # кінцевий список в якому будуть змінені кортежі
for i in list_of_tuples:
    lst = list(i)
    del lst[-1]
    lst.append(value)
    last_list.append(tuple(lst))
print(last_list)