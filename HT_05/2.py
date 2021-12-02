'''
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :) пароль повинен мати хоча б одни із символів [!, @, $, %, ^, &, *, (, ), _, -, +]
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
'''
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

    if  50 >= len(username) <= 3:
        raise LoginException('the name must be at least 3 characters and at most 50')
    elif len(password) < 8:
        raise LoginException('password must be at least 8 characters long')
    elif not has_numbers(password):
        raise LoginException('the password must have at least one digit')
    elif not symbol_from_the_list(symbols, password):
        raise LoginException('the password must have at least one of the characters [!, @, $, %, ^, &, *, (, ), _, -, +]')
    else:
        return True

print(login_and_password_validation('qwerty', '1qazttt!'))

