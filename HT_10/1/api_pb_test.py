import requests

pb = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
r = requests.get(pb)
lst = r.json()
for i in lst:
    print(i)
for dct in lst:
    print('1', dct['ccy'], 'buy', dct['buy'], dct['base_ccy'], '& sale', dct['sale'], dct['base_ccy'])