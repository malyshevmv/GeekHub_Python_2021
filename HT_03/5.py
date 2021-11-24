'''
5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися
рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z
'''
a = int(input('enter a number: '))
b = int(input('enter a number: '))

def comparison_of_numbers(x, y):
    if x > y:
        return f'{x} бiльше нiж {y} на {x - y}'
    elif x < y:
        return f'{y} бiльше нiж {x} на {y - x}'
    else:
        return f'{x} дорiвнює {y}'


print(comparison_of_numbers(a, b))