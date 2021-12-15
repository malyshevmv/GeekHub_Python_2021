import json
import sqlite3 as sq


def whether_the_user_is_a_bank_customer():
    #перевіряю чи е користувач клієнтом банку
    global user_id
    number_of_attempts = 3
    while number_of_attempts:
        print(f'You have {number_of_attempts} attempts to enter the login and password')
        user = input('Enter your login: ')
        password = input('Enter your password: ')
        with sq.connect('sqlite.db') as con:
            cur = con.cursor()
            cur.execute('''SELECT * FROM users''')
            for result in cur:
                if result[1] == user and result[2] == password:
                    user_id = result[0]
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
    with sq.connect('sqlite.db') as con:
        cur = con.cursor()
        cur.execute('''SELECT * FROM balanse''')
        for result in cur:
            if user_id == result[0]:
                print(f'Your balance {result[1]}')

def i_replenish_my_balance():
    #поповнюю баланс
    number_of_tryings = 3
    while number_of_tryings:
        the_amount_of_replenishment_of_the_balance = input('Enter the top-up amount: ')
        if the_amount_of_replenishment_of_the_balance.isdigit() and int(the_amount_of_replenishment_of_the_balance) >= 0:
            with sq.connect('sqlite.db') as con:
                cur = con.cursor()
                cur.execute('''SELECT * FROM balanse''')
                for result in cur:
                    if result[0] == user_id:
                        the_amount_on_the_account = result[1]
            result = int(the_amount_of_replenishment_of_the_balance) + the_amount_on_the_account
            with sq.connect('sqlite.db') as con:
                cur = con.cursor()
                cur.execute(f'''UPDATE balanse SET amount = {result} WHERE user_id = {user_id}''')
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
                        the_amount_you_want_to_withdraw -= int(key)
                        dct_znachen[key] = value - 1
                        if key in dct_seized_banknotes:
                            dct_seized_banknotes[key] += 1
                            break
                        else:
                            dct_seized_banknotes[key] = 1
                            break
            if the_amount_you_want_to_withdraw == has_the_amount_decreased:
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
            with sq.connect('sqlite.db') as con:
                cur = con.cursor()
                cur.execute('''SELECT * FROM balanse''')
                for result in cur:
                    if result[0] == user_id:
                        balance = result[1]
            result = balance - int(the_amount_to_be_withdrawn)
            if result >= 0:
                if change_the_number_of_banknotes_in_the_ATM_after_the_user(the_amount_to_be_withdrawn, 'number_of_banknotes.data'):
                    with sq.connect('sqlite.db') as con:
                        cur = con.cursor()
                        cur.execute(f'''UPDATE balanse SET amount = {result} WHERE user_id = {user_id}''')
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
    if flag and user_id != 3:
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
    elif flag and user_id == 3:
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