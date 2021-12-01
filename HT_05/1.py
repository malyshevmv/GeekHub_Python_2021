'''
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
   і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
       інакше (<silent> == <False>) - породжується виключення LoginException
'''
class LoginException(Exception):
    pass

def login_and_password_verification(username, password, silent = False):
    dct ={'user1': 'qwerty', 'user2': '1111', 'user3': '0000', 'user4': '1234', 'user5': '4321'}
    if username in dct:
        if dct[username] == password:
            return True
        elif dct[username] != password and silent == True:
            return False
        elif dct[username] != password and silent == False:
            raise LoginException('incorrect data entered')
    elif username not in dct and silent == True:
        return False
    elif username not in dct and silent == False:
        raise LoginException('incorrect data entered')
    else:
        return 'something went wrong'

print(login_and_password_verification('user0', 'qwerty', silent = True))