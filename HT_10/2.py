'''
2. Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.
   - Перелік валют краще принтануть.
   - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
   - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
   - Також перевірте, чи введена правильна валюта.
   Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну
   курсу обраної валюти (Нацбанк) від введеної дати до поточної. Приблизний вивід наступний:
   Currency: USD
   Date: 12.12.2021
   NBU:  27.1013   -------
   Date: 13.12.2021
   NBU:  27.0241   -0,0772
   Date: 14.12.2021
   NBU:  26.8846   -0,1395
'''
import requests
import datetime
import time

# вводим дані валюту та дату
currency = input('Enter currency(example: USD, EUR, GBP, PLN): ')
#currency = 'USD'
lst_of_currencies = ['USD', 'EUR', 'GBP', 'PLN']
if currency not in lst_of_currencies:
    print('Entered an incorrect value')
start_date = input('Enter the start date(example: 19.12.2021): ')
#start_date = '12.12.2021'

now = datetime.datetime.today().date()
try:
    if now >= datetime.datetime.strptime(start_date, "%d.%m.%Y").date():
        print('Date verified')
    else:
        print('Something went wrong')
except ValueError as err:
    print(err)

# список дат від введеної до сьогодні
lst_date = []
one_day = datetime.timedelta(days=1)
d = datetime.datetime.strptime(start_date, "%d.%m.%Y")
while d.date() != now:
    lst_date.append(d.strftime("%d.%m.%Y"))
    d += one_day
else:
    lst_date.append(now.strftime("%d.%m.%Y"))

# парсим пб
dct_data = {}
for date_ in lst_date:
    pb = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date_}'
    r = requests.get(pb)
    time.sleep(0.5)
    dct = r.json()
    if currency == 'USD':
        dct_data[date_] = dct['exchangeRate'][-2]['saleRateNB']
    elif currency == 'EUR':
        dct_data[date_] = dct['exchangeRate'][8]['saleRateNB']
    elif currency == 'GBP':
        dct_data[date_] = dct['exchangeRate'][9]['saleRateNB']
    elif currency == 'PLN':
        dct_data[date_] = dct['exchangeRate'][17]['saleRateNB']

# список з різницямми курсу
lst_values = list(dct_data.values())
lst_of_differences = ['-------']
for i in range(1, len(lst_values)):
    lst_of_differences.append(round(lst_values[i] - lst_values[i - 1], 4))

# додаєм різницю до основного словника dct_data і отримуємо dct_diff
dct_diff = {}
for key, value in dct_data.items():
    dct_diff[key] = [value]
for key, i in zip(dct_diff, lst_of_differences):
    dct_diff[key].append(i)

# вивід на екран
print(f'Currency: {currency}')
print()
for key, value in dct_diff.items():
    print(f'Date: {key}')
    print(f'NBU: {value[0]}', '\t', value[1])
    print()