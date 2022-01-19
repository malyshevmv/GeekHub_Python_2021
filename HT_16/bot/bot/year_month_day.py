"""
Перевіряємо на правильність введеної дати
"""
import datetime


user_year = input('Enter year: ')
user_month = input('Enter month: ')
user_day = input('Enter day: ')

user_date = f'{user_year}.{user_month}.{user_day}'
now = datetime.datetime.today().date()
try:
    if now >= datetime.datetime.strptime(user_date, "%Y.%m.%d").date():
        print('Date verified')
        year = user_year
        month = user_month
        day = user_day
        date = f'{year}_{int(month):02}_{int(day):02}'
    else:
        print('Invalid date entered')
except ValueError as err:
    print(err)
