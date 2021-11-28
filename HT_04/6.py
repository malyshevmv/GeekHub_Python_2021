'''
6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
'''
def i_accept_the_number(n):
    if n > 0:
        return n**2
    elif n < 0:
        return n + 100
    return n

print(i_accept_the_number(25))