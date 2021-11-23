'''
4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат.
Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
'''
def func_random_num_range():
    import random

    n = random.randrange(20)
    return n

def func_random_num_randint():
    import random

    n = random.randint(0, 20)
    return n
def func_random_num_choice():
    import random

    lst = list(range(21))
    n = random.choice(lst)
    return n

def main_function():
    a = func_random_num_randint()
    b = func_random_num_range()
    c = func_random_num_choice()

    if a == b == c:
        return 'Oho!'
    elif a == b != c or a != b == c or a == c != b:
        return 'Indeed!'
    else:
        return 'well as always'


print(main_function())