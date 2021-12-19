'''
3. Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
   Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
   конвертацію введеної суми з однієї валюти в іншу.
'''
import requests
import datetime


currency1 = input('Enter the currency you want to exchange(example: USD, EUR): ')
currency2 = input('Enter the currency you want to receive(example: USD, EUR): ')
summa = int(input('Enter the amount you want to exchange: '))

lst_of_currencies = ['USD', 'EUR']
if currency1 not in lst_of_currencies:
    print('Entered an incorrect value')
if currency2 not in lst_of_currencies:
    print('Entered an incorrect value')

now = datetime.datetime.today()
pb= f'https://api.privatbank.ua/p24api/exchange_rates?json&date={now.strftime("%d.%m.%Y")}'
r = requests.get(pb)
data = r.json()
data ={'exchangeRate': []}

if len(data['exchangeRate']) == 0:
    one_day = datetime.timedelta(days=1)
    now -= one_day
    pb = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={now.strftime("%d.%m.%Y")}'
    r = requests.get(pb)
    data = r.json()
print(data['exchangeRate'][-2])
print(data['exchangeRate'][8])
number_UAH = 0
if currency1 == 'USD':
    number_UAH = data['exchangeRate'][-2]['purchaseRate'] * summa
if currency1 == 'EUR':
    number_UAH = data['exchangeRate'][8]['purchaseRate'] * summa
if currency2 == 'USD':
    number_USD = number_UAH // data['exchangeRate'][-2]['saleRate']
    print(number_USD)
if currency2 == 'EUR':
    number_EUR = number_UAH // data['exchangeRate'][8]['saleRate']
    print(number_EUR)