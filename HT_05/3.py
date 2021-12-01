'''
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
   перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
'''
#---2.py---
class LoginException(Exception):
    pass


def login_and_password_validation(username, password):
    symbols = ['!', '@', '$',' %', '^', '&', '*', '(', ')', '_', '-', '+']
    def has_numbers(string):
        for i in string:
            if i.isdigit():
                return True
        return False

    def symbol_from_the_list(lst, string):
        for i in string:
            if i in lst:
                return True
        return False

    if 3 <= len(username) <= 50:
        if len(password) >= 8:
            if has_numbers(password):
                if symbol_from_the_list(symbols, password):
                    return 'OK'
                else:
                    raise LoginException('the password must have at least one of the characters [!, @, $, %, ^, &, *, (, ), _, -, +]')
            else:
                raise LoginException('the password must have at least one digit')
        else:
            raise LoginException('password must be at least 8 characters long')
    else:
        raise LoginException('the name must be at least 3 characters and at most 50')
#^^^2.py^^^

list_of_pairs_name_password = [('user0', 'qwerty1!'), ('user1', 'qwerty!'), ('user2', 'qwerty11'), ('user3', 'qwertyu!'), ('us', 'qwerty1!'), (('user5', 'qwerty2@'))]
for i in list_of_pairs_name_password:
    try:
        print('Name:', i[0])
        print('Password:', i[1])
        print('Status:', login_and_password_validation(i[0], i[1]))
    except LoginException as error:
        print(f'Status: {error}')
    print('-----')