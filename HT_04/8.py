'''
8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
Тобто, функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок,
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
'''
def cyclic_shift_of_elements(lst, shift):
    if shift > 0:
        for _ in range(shift):
            last_elem = lst.pop()
            lst.insert(0, last_elem)
    elif shift < 0:
        for _ in range(shift * (-1)):
            first_elem = lst.pop(0)
            lst.append(first_elem)
    return lst

lst_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(cyclic_shift_of_elements(lst_num, -3))