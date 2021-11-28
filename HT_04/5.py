'''
5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
'''
def fibonacci(num):
    lst =[0]
    a, b = 0, 1
    while a < num:
        a, b = b, a+b
        if a <= num:
            lst.append(a)
    return lst

print(*fibonacci(89))