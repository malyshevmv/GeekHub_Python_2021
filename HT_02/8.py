'''
8. Написати скрипт, який отримує від користувача позитивне ціле число і створює словник,
з ключами від 0 до введеного числа, а значення для цих ключів - це квадрат ключа.
        Приклад виводу при введеному значенні 5:
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
n = int(input('enter a positive whole number: '))
lst_key = list(range(n + 1))
dict_of_squaresfor ={}
for i in lst_key:
    dict_of_squaresfor[i] = i ** 2
print(dict_of_squaresfor)


'''
dct = {a: a**2 for a in range(n + 1)}
print(dct)
'''