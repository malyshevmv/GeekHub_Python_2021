'''
Сайт для виконання завдання: https://jsonplaceholder.typicode.com
Написати програму, яка буде робити наступне:
1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів (ID, ім'я, нікнейм)
2. Запропонувати обрати користувача (ввести ID)
3. Розробити наступну менюшку (із вкладеними пунктами):
   1. Повна інформація про користувача
   2. Пости:
      - перелік постів користувача (ID та заголовок)
      - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
   3. ТУДУшка:
      - список невиконаних задач
      - список виконаних задач
   4. Вивести URL рандомної картинки
'''
import requests
import time
import pprint
# users = 'https://jsonplaceholder.typicode.com/users'
# r = requests.get(users)
# data_users = r.json()
#
# posts = 'https://jsonplaceholder.typicode.com/posts'
# r = requests.get(users)
# data_posts = r.json()
#
# comments = 'https://jsonplaceholder.typicode.com/comments'
# r = requests.get(users)
# data_comments = r.json()
#
# todos = 'https://jsonplaceholder.typicode.com/todos'
# r = requests.get(users)
# data_todos = r.json()
#
# photos = 'https://jsonplaceholder.typicode.com/photos'
# r = requests.get(users)
# data_photos = r.json()


def i_return_brief_information_about_users():
    global data_users
    users = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(users)
    data_users = r.json()
    print('User information')
    for user in data_users:
        print('id:', user['id'])
        print('name:', user['name'])
        print('username:', user['username'])
        print('-' * 20)
        #time.sleep(0.75)

def i_choose_the_user():
    print('Select user')
    id_user = int(input('Enter id: '))
    return id_user

def complete_user_information(id: int):
    ''' Повна інформація про користувача '''
    for user in data_users:
        if user['id'] == id:
            for key, value in user.items():
                if type(value) == dict:
                    print(key)
                    for key, value_ in value.items():
                        print('\t', key + ':', value_)
                else:
                    print(key + ':', value)
            return user

def menu(id: int):
    '''
    print('ведіть що тре по юзеру зробить
    1  -повна інфа по користувачю
    2 пости
        введіть 1 щоб - перелік постів користувача (ID та заголовок)
        введіть 2 щоб - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
        тут, або між ними тре вернутись в головне меню типу: "що робити далі з юзером"
    3 туду це список завдань по юзеру
        введіть 1 щоб список невиконаних задач
        введіть 2 щоб побачити список виконаних задач
        тут теж тре вертатись в головне меню
    4 принтуєм рандомну картинку
    '''
    complete_user_information(id)

def start():
    i_return_brief_information_about_users()
    id_user = i_choose_the_user()
    menu(id_user) # МЕНЮ ТРЕБА ЗАЦИКЛИТЬ АБО КОЖНОГО РАЗУ ВЕРТАТИСЬ ДО АЙДІ ЮЗЕРА ЩО НЕ ОК

start()