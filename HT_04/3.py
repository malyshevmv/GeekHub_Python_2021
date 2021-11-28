'''
3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте, и False - якщо ні.
'''
from random import randint


def is_prime(n):
    counter = 0
    for i in range(2, n + 1):
        if n % i == 0:
            counter += 1
    if counter == 1:
        return True
    return False

num = randint(0, 1000)
print(f'{num = }', is_prime(num), sep='\n')
