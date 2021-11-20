'''
6. Написати скрипт, який об'єднає три словника в самий перший. Оновлюється тільки перший словник. Дані можна "захардкодити".
        Sample Dictionary :
        dict_1 = {1:10, 2:20}
        dict_2 = {3:30, 4:40}
        dict_3 = {5:50, 6:60}
        Expected Result : dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
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
print(dict_1, dict_2, dict_3, sep='\n')
print()
dict_1.update(dict_2)
dict_1.update(dict_3)
print(dict_1)