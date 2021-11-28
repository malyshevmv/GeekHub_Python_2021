'''
1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата,
і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
'''
from random import randint


side_square = randint(1, 20)
def square(a, number_of_decimal_places = 2):
    diagonal_of_the_square = 2**0.5 * a
    return (4*a, a*a, float(f'{diagonal_of_the_square:.{number_of_decimal_places}f}'))

print(f'{side_square = }', square(side_square), sep='\n')