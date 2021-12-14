'''
##########_HT_07_##########
1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>)
      та історію транзакцій (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх.
      Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль.
      Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
      (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)
^^^^^^^^^^_HT_07_^^^^^^^^^^

1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна
   "загрузити" деяку кількість банкнот (вибирається номінал і кількість).
   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом
   - видається мінімальна кількість банкнот наявного номіналу.
   P.S. Будьте обережні з використанням "жадібного" алгоритму
   (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює
   неправильно або не працює взагалі.
   Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,
   банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
   Особливості реалізації:
   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
     - переглянути наявні купюри;
     - змінити кількість купюр;
   - видача грошей для користувачів відбувається в межах наявних купюр;
   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя,
   та й, наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
'''
import csv
import json


def whether_the_user_is_a_bank_customer():
    #перевіряю чи е користувач клієнтом банку
    global user
    number_of_attempts = 3
    while number_of_attempts:
        print(f'You have {number_of_attempts} attempts to enter the login and password')
        user = input('Enter your login: ')
        password = input('Enter your password: ')
        with open('users.data') as f:
            data = csv.reader(f)
            headers = next(data)
            for user_, password_ in data:
                if user_ == user and password_ == password:
                    return True
            else:
                number_of_attempts -= 1

def menu_collector():
    print(
        '''
        Enter the number 1 and press enter to view the available banknotes
        Enter the number 2 and press enter to change the number of banknotes
        Enter the number 3 and press enter to exit
        '''
        )
    num = int(input('Your chosen number: '))
    return num

def i_check_the_available_banknotes():
    #перевіряю доступні банкноти
    with open('number_of_banknotes.data') as bank:
        result = bank.read()
    dct_res = json.loads(result)
    for key, value in dct_res.items():
        print(key, '\t', value)

def change_the_number_of_banknotes():
    #змінюю кількість банкнот
    with open('number_of_banknotes.data') as bank:
        result = bank.read()
    dct_res = json.loads(result)
    print('Enter the quantity of each banknote')
    for key in dct_res:
        dct_res[key] = int(input(f'{key} = '))

    with open('number_of_banknotes.data', 'w') as bank:
        bank.write(json.dumps(dct_res, indent=4))


def menu():
    #пропоную користувачеві послуги банкомату
    print(
        '''
    Enter the number 1 and press enter to check the balance
    Enter the number 2 and press enter to replenish the balance
    Enter the number 3 and press enter to remove from balance
    Enter the number 4 and press enter to exit
        '''
        )
    num = int(input('Your chosen number: '))
    return num

def i_check_the_balance():
    #перевіряю баланс
    with open(f'{user}_balance.data') as b:
        result = b.read()
    print(f'Your balance {result}')

def i_replenish_my_balance():
    #поповнюю баланс
    number_of_tryings = 3
    while number_of_tryings:
        the_amount_of_replenishment_of_the_balance = input('Enter the top-up amount: ')
        if the_amount_of_replenishment_of_the_balance.isdigit() and int(the_amount_of_replenishment_of_the_balance) >= 0:
            with open(f'{user}_balance.data') as b:
                the_amount_on_the_account = b.read()
            result = int(the_amount_of_replenishment_of_the_balance) + int(the_amount_on_the_account)
            with open(f'{user}_balance.data', 'w') as f, open(f'{user}_transactions.data', 'a') as tr:
                f.write(str(result))
                tr.write(json.dumps(str(result)))
                tr.write('\n')
            return
        else:
            print('Did you really enter the amount you want to top up your balance?')
            number_of_tryings -= 1
            print(f'You have {number_of_tryings} more attempts to enter the top-up amount')

def change_the_number_of_banknotes_in_the_ATM_after_the_user(summa, json_znachen):
    #зменшую кількість банкнот в банкоматі коли користувач ЗНІМАЄ з балансу
    the_amount_you_want_to_withdraw = int(summa)
    with open(json_znachen) as bank:
        res = bank.read()
        dct_znachen = json.loads(res)
    sum_bankomat = 0
    sorted_tuple_znachen = sorted(dct_znachen.items(), key=lambda x: int(x[0]), reverse=True)
    dct_znachen = dict(sorted_tuple_znachen)
    for key, value in dct_znachen.items():
        if value != 0:
            sum_bankomat += int(key) * value
    if sum_bankomat >= the_amount_you_want_to_withdraw:
        dct_seized_banknotes = {}
        while the_amount_you_want_to_withdraw != 0:
            has_the_amount_decreased = the_amount_you_want_to_withdraw
            for key, value in dct_znachen.items():
                if value >= 1:
                    if the_amount_you_want_to_withdraw % int(key) == 0:
                        print(key, 'pislja if')
                        the_amount_you_want_to_withdraw -= int(key)
                        dct_znachen[key] = value - 1
                        if key in dct_seized_banknotes:
                            dct_seized_banknotes[key] += 1
                            break
                        else:
                            dct_seized_banknotes[key] = 1
                            break
            if the_amount_you_want_to_withdraw == has_the_amount_decreased:
                print(the_amount_you_want_to_withdraw)
                return False
        print('Was withdrawn from the ATM')
        for key, value in dct_seized_banknotes.items():
            print(key, '\t', value)
        if the_amount_you_want_to_withdraw == 0:
            with open(json_znachen, 'w') as bank:
                bank.write(json.dumps(dct_znachen, indent=4))
    else:
        return False
    return True

def i_take_off_the_bank_balance():
    #знімаю з балансу
    number_of_tryings = 3
    while number_of_tryings:
        print('Such banknotes are now available')
        with open('number_of_banknotes.data') as bank:
            result = bank.read()
        dct_res = json.loads(result)
        for key in dct_res:
            if dct_res[key] != 0:
                print(key)
        the_amount_to_be_withdrawn = input('What amount do you want to deduct from the balance? ')
        if the_amount_to_be_withdrawn.isdigit() and int(the_amount_to_be_withdrawn) > 0:
            with open(f'{user}_balance.data') as b:
                balance = b.read()
            result = int(balance) - int(the_amount_to_be_withdrawn)
            if result >= 0:
                if change_the_number_of_banknotes_in_the_ATM_after_the_user(the_amount_to_be_withdrawn, 'number_of_banknotes.data'):
                    with open(f'{user}_balance.data', 'w') as b, open(f'{user}_transactions.data', 'a') as tr:
                        b.write(str(result))
                        tr.write(json.dumps(str(result)))
                        tr.write('\n')
                        return 'The removal from the balance was successful'
                else:
                    print('Enter a smaller value')
                    number_of_tryings -= 1
                    print(f'{number_of_tryings} more attempts left')
            else:
                print('Enter a smaller value')
                number_of_tryings -= 1
                print(f'{number_of_tryings} more attempts left')
        else:
            print('Enter a smaller value')
            number_of_tryings -= 1
            print(f'{number_of_tryings} more attempts left')

def start():
    flag = whether_the_user_is_a_bank_customer()
    if flag and user != 'admin':
        while True:
            the_user_has_selected = menu()
            if the_user_has_selected == 1:
                i_check_the_balance()
            elif the_user_has_selected == 2:
                i_replenish_my_balance()
            elif the_user_has_selected == 3:
                i_take_off_the_bank_balance()
            elif the_user_has_selected == 4:
                break
            else:
                break
        return 'Thank you for using the services of our bank'
    elif flag and user == 'admin':
        while True:
            the_choice_of_the_collector = menu_collector()
            if the_choice_of_the_collector == 1:
                i_check_the_available_banknotes()
            elif the_choice_of_the_collector == 2:
                change_the_number_of_banknotes()
            elif the_choice_of_the_collector == 3:
                break
            else:
                break
        return 'Thank you for visiting'
    return 'Sorry, you are not a member of our bank'

print(start())