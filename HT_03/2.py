'''
2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).
'''
first_year = int(input('enter year: '))
last_year = int(input('enter last year: '))
for i in range(first_year, last_year + 1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        print(i)