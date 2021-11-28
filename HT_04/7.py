'''
7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
'''
def number_of_identical_elements(lst):
    return {i: lst.count(i) for i in lst}



print(number_of_identical_elements([1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 5, 0, 0, 0]))