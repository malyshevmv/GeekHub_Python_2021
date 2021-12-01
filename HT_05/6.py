'''
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
'''
def i_range(stop, start=0, step=1):
    while start < stop:
        yield start
        start += step

lst = list(i_range(5))
print(lst)
