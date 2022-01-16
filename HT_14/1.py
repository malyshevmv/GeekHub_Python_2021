
import sqlite3 as sq

import requests


class User(object):
    def __init__(self, login, password):
        self.login = login
        self.password = password


class Authorization(object):
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.user_id = None
        self.collector = False

    def is_a_bank_user(self):
        with sq.connect('sqlite.db') as con:
            cur = con.cursor()
            cur.execute('''SELECT * FROM users''')
            for result in cur:
                if result[1] == self.login and result[2] == self.password:
                    self.user_id = result[0]
                    if self.user_id == 3:
                        self.collector = True
                    return True
            return False


class ATM(object):

    def i_check_the_balance(self, user_id):
        with sq.connect('sqlite.db') as con:
            cur = con.cursor()
            cur.execute('''SELECT * FROM balanse''')
            for result in cur:
                if user_id == result[0]:
                    print(f'Your balance {result[1]}')
                    break

    def i_replenish_my_balance(self, user_id, amount_of_replenishment):
        self.number_of_tryings = 3
        while self.number_of_tryings:
            the_amount_of_replenishment_of_the_balance = amount_of_replenishment
            if the_amount_of_replenishment_of_the_balance.isdigit() and int(
                    the_amount_of_replenishment_of_the_balance) >= 0:
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
                with sq.connect('sqlite.db') as con:
                    cur = con.cursor()
                    cur.execute('''SELECT * FROM transactions''')
                    dct = {i[0]: i[1] for i in list(cur)}
                transact = ''
                for key in dct:
                    if key == user_id:
                        transact += str(dct[key])
                result_str = str(result)
                transact += result_str
                with sq.connect('sqlite.db') as con:
                    cur = con.cursor()
                    cur.execute(f'''UPDATE transactions SET user_transactions = ? WHERE user_id = ?''',
                                (transact + ' ', user_id))
                return 'The replenishment operation was successful'
            else:
                print('Did you really enter the amount you want to top up your balance?')
                self.number_of_tryings -= 1
                print(f'You have {self.number_of_tryings} more attempts to enter the top-up amount')

    def _change_the_number_of_banknotes_in_the_ATM_after_the_user(self, summa):
        # зменшую кількість банкнот в банкоматі коли користувач ЗНІМАЄ з балансу
        the_amount_you_want_to_withdraw = int(summa)
        with sq.connect('sqlite.db') as con:
            cur = con.cursor()
            cur.execute('''SELECT * FROM number_of_banknotes''')
            dct_znachen = {i[0]: i[1] for i in list(cur)}
        sum_bankomat = 0
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
                with sq.connect('sqlite.db') as con:
                    cur = con.cursor()
                    for key, value in dct_znachen.items():
                        cur.execute(f'''UPDATE number_of_banknotes SET number = {value} WHERE banknote = {key}''')
        else:
            return False
        return True

    def i_take_off_the_bank_balance(self, user_id, the_amount_to_be_withdrawn):
        self.the_amount_to_be_withdrawn = the_amount_to_be_withdrawn
        self.number_of_tryings = 3
        while self.number_of_tryings:
            print('Such banknotes are now available')
            with sq.connect('sqlite.db') as con:
                cur = con.cursor()
                cur.execute('''SELECT * FROM number_of_banknotes''')
                dct_res = {i[0]: i[1] for i in list(cur)}
            for key in dct_res:
                if dct_res[key] != 0:
                    print(key)
            if self.the_amount_to_be_withdrawn.isdigit() and int(self.the_amount_to_be_withdrawn) > 0:
                with sq.connect('sqlite.db') as con:
                    cur = con.cursor()
                    cur.execute('''SELECT * FROM balanse''')
                    for result in cur:
                        if result[0] == user_id:
                            balance = result[1]
                result = balance - int(self.the_amount_to_be_withdrawn)
                if result >= 0:
                    if ATM._change_the_number_of_banknotes_in_the_ATM_after_the_user(self, self.the_amount_to_be_withdrawn):
                        with sq.connect('sqlite.db') as con:
                            cur = con.cursor()
                            cur.execute(f'''UPDATE balanse SET amount = {result} WHERE user_id = {user_id}''')
                        with sq.connect('sqlite.db') as con:
                            cur = con.cursor()
                            cur.execute('''SELECT * FROM transactions''')
                            dct = {i[0]: i[1] for i in list(cur)}
                        transact = ''
                        for key in dct:
                            if key == user_id:
                                transact += str(dct[key])
                        result_str = str(result)
                        transact += result_str
                        with sq.connect('sqlite.db') as con:
                            cur = con.cursor()
                            cur.execute(f'''UPDATE transactions SET user_transactions = ? WHERE user_id = ?''',
                                        (transact + ' ', user_id))
                        return 'The removal from the balance was successful'
                    else:
                        print('Enter a smaller value')
                        self.number_of_tryings -= 1
                        print(f'{self.number_of_tryings} more attempts left')
                else:
                    print('Enter a smaller value')
                    self.number_of_tryings -= 1
                    print(f'{self.number_of_tryings} more attempts left')
            else:
                print('Enter a smaller value')
                self.number_of_tryings -= 1
                print(f'{self.number_of_tryings} more attempts left')

    def current_exchange_rate(self):
        pb = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        r = requests.get(pb)
        lst = r.json()
        for dct in lst:
            print('1', dct['ccy'], 'buy', dct['buy'], dct['base_ccy'], '& sale', dct['sale'], dct['base_ccy'])

    def i_check_the_available_banknotes(self, collector):
        if collector:
            with sq.connect('sqlite.db') as con:
                cur = con.cursor()
                cur.execute('''SELECT * FROM number_of_banknotes''')
            dct_res = {i[0]: i[1] for i in list(cur)}
            for key, value in dct_res.items():
                print(key, '\t', value)
        else:
            print('You do not have access')

    def change_the_number_of_banknotes(self, collector):
        if collector:
            with sq.connect('sqlite.db') as con:
                cur = con.cursor()
                cur.execute('''SELECT * FROM number_of_banknotes''')
            dct_res = {i[0]: i[1] for i in list(cur)}
            print('Enter the quantity of each banknote')
            for key in dct_res:
                dct_res[key] = int(input(f'{key} = '))
            with sq.connect('sqlite.db') as con:
                cur = con.cursor()
                for key, value in dct_res.items():
                    cur.execute(f'''UPDATE number_of_banknotes SET number = {value} WHERE banknote = {key}''')
        else:
            print('You do not have access')


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


def menu():
    print(
        '''
    Enter the number 1 and press enter to check the balance
    Enter the number 2 and press enter to replenish the balance
    Enter the number 3 and press enter to remove from balance
    Enter the number 4 and press enter to view the current exchange rate
    Enter the number 5 and press enter to exit
        '''
        )
    num = int(input('Your chosen number: '))
    return num


def start():
    user = User(input('Enter login: '), input('Enter password: '))
    bank_user = Authorization(user.login, user.password)
    bank_user.is_a_bank_user()
    bankomat = ATM()
    if bank_user.collector:
        while True:
            num = menu_collector()
            if num == 1:
                bankomat.i_check_the_available_banknotes(bank_user.collector)
            elif num == 2:
                bankomat.change_the_number_of_banknotes(bank_user.collector)
            elif num == 3:
                break
            else:
                break
    else:
        while True:
            num = menu()
            if num == 1:
                bankomat.i_check_the_balance(bank_user.user_id)
            elif num == 2:
                bankomat.i_replenish_my_balance(bank_user.user_id, input('Enter the top-up amount: '))
            elif num == 3:
                bankomat.i_take_off_the_bank_balance(bank_user.user_id, input('What amount do you want to deduct from the balance? '))
            elif num == 4:
                bankomat.current_exchange_rate()
            elif num == 5:
                break
            else:
                break


start()
