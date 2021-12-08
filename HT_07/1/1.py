'''
1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)
'''

import csv
import json



USER_ONLINE = ''

def ask_login_and_password():
    global USER_ONLINE
    number_of_attempts = 3
    while number_of_attempts:
        print(f'You have {number_of_attempts} attempts')
        login, password = map(str, input('Please enter the login and password through the space: ').split())
        with open('users.data') as f:
            reader = csv.reader(f)
            headers = next(reader)
            for row in reader:
                if login == row[0] and password == row[1]:
                    USER_ONLINE = login
                    return True
        print('Incorrect login or password entered')
        number_of_attempts -= 1
        return 'You used all your attempts, goodbye'


def menu():
    print('Your personal bank greets you')
    print('To view the balance, press 1 and press enter')
    print('To top up the balance, press 2 and press enter')
    print('To remove from balance, press 3 and press enter')
    print('To exit, press 4 and enter')
    user_choice = int(input())
    print('Thanks for the choice')
    return user_choice

def i_deduce_the_balance():
    #print(f'я вивожу баланс користувача {USER_ONLINE}')
    with open(f'{USER_ONLINE}_balance.data') as balance:
        print(f'Your balance is {balance.read()}')
    print('----------')

def i_replenish_the_balance():
    #print(f'я поповнюю баланс коистувача {USER_ONLINE}')
    plus_to_balance = int(input('How much do you want to top up your balance? '))
    with open(f'{USER_ONLINE}_balance.data') as balance:
        b = balance.read()
    with open(f'{USER_ONLINE}_balance.data', 'w') as balance:
        balance.write(str(plus_to_balance + int(b)))
    with open(f'{USER_ONLINE}_balance.data') as balance, open(f'{USER_ONLINE}_transactions.data', 'a') as transactions:
        b = balance.read()
        transactions.write(json.dumps(b))
    print('----------')

def i_take_off_the_balance():
    #print(f'я знімаю з балансу користувача {USER_ONLINE}')
    minus_to_balance = int(input('How much do you want to top up your balance? '))
    with open(f'{USER_ONLINE}_balance.data') as balance:
        b = balance.read()
    if int(b) >= minus_to_balance:
        with open(f'{USER_ONLINE}_balance.data', 'w') as balance:
            balance.write(str(int(b) - minus_to_balance))
        with open(f'{USER_ONLINE}_balance.data') as balance, open(f'{USER_ONLINE}_transactions.data', 'a') as transactions:
            b = balance.read()
            transactions.write(json.dumps(b))
        print('The operation was successful')
    else:
        print('Not enough funds on the balance')
    print('----------')

def start():
    if ask_login_and_password():
        while True:
            result = menu()
            if result == 1:
                i_deduce_the_balance()
            if result == 2:
                i_replenish_the_balance()
            if result == 3:
                i_take_off_the_balance()
            if result == 4:
                return 'Thank you for visiting, goodbye'
    return 'Thank you for visiting, goodbye'


start()


