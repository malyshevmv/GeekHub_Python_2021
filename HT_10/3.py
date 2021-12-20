'''
3. Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
   Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
   конвертацію введеної суми з однієї валюти в іншу.
'''
import requests
import datetime


currency1 = input('Enter the currency you want to exchange(example: USD, EUR, GBP, PLN, UAH): ')
currency2 = input('Enter the currency you want to receive(example: USD, EUR, GBP, PLN, UAH): ')
summa = int(input('Enter the amount you want to exchange: '))

lst_of_currencies = ['USD', 'EUR', 'GBP', 'PLN', 'UAH']
if currency1 not in lst_of_currencies:
    print('Entered an incorrect value')
if currency2 not in lst_of_currencies:
    print('Entered an incorrect value')

now = datetime.datetime.today()
pb= f'https://api.privatbank.ua/p24api/exchange_rates?json&date={now.strftime("%d.%m.%Y")}'
r = requests.get(pb)
data = r.json()

if len(data['exchangeRate']) == 0:
    one_day = datetime.timedelta(days=1)
    now -= one_day
    pb = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={now.strftime("%d.%m.%Y")}'
    r = requests.get(pb)
    data = r.json()

number_UAH = 0
if currency1 == 'USD':
    number_UAH = data['exchangeRate'][-2]['purchaseRate'] * summa
if currency1 == 'EUR':
    number_UAH = data['exchangeRate'][8]['purchaseRate'] * summa
if currency1 == 'GBP':
    number_UAH = data['exchangeRate'][9]['purchaseRate'] * summa
if currency1 == 'PLN':
    number_UAH = data['exchangeRate'][17]['purchaseRate'] * summa
if currency1 == 'UAH':
    number_UAH = data['exchangeRate'][-3]['purchaseRateNB'] * summa
if currency2 == 'USD':
    number_USD = number_UAH / data['exchangeRate'][-2]['saleRate']
    print(f'{number_USD:.2f}')
if currency2 == 'EUR':
    number_EUR = number_UAH / data['exchangeRate'][8]['saleRate']
    print(f'{number_EUR:.2f}')
if currency2 == 'GBP':
    number_GBP = number_UAH / data['exchangeRate'][9]['saleRate']
    print(f'{number_GBP:.2f}')
if currency2 == 'PLN':
    number_PLN = number_UAH / data['exchangeRate'][17]['saleRate']
    print(f'{number_PLN:.2f}')
if currency2 == 'UAH':
    number_UAH_ = number_UAH / data['exchangeRate'][-3]['saleRateNB']
    print(f'{number_UAH_:.2f}')
