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
    lst_user = [['user1', 'qwerty'], ['user2', '1111'], ['user3', '0000'], ['user4', '1234'], ['user5', '4321']]
    for user in lst_user:
        if user[0] == username and user[1] == password:
            return True
        elif silent == True:
            return False
        else:
            raise LoginException('incorrect data entered')

print(login_and_password_verification('user1', 'qwerty'))