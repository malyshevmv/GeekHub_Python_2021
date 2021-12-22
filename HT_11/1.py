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
import random
users = 'https://jsonplaceholder.typicode.com/users'
r = requests.get(users)
data_users = r.json()
#
posts = 'https://jsonplaceholder.typicode.com/posts'
r = requests.get(posts)
data_posts = r.json()
#
# comments = 'https://jsonplaceholder.typicode.com/comments'
# r = requests.get(users)
# data_comments = r.json()
#
todos = 'https://jsonplaceholder.typicode.com/todos'
r = requests.get(todos)
data_todos = r.json()
#
photos = 'https://jsonplaceholder.typicode.com/photos'
r = requests.get(photos)
data_photos = r.json()


def i_return_brief_information_about_users():
    '''інформація про користувачів'''
    global lst_user_id
    lst_user_id = []
    print('User information')
    for user in data_users:
        print('id:', user['id'])
        print('name:', user['name'])
        print('username:', user['username'])
        print('-' * 20)
        time.sleep(0.75)
        lst_user_id.append(user['id'])
def i_choose_the_user():
    print('Select user')
    id_user = int(input('Enter id: '))
    if id_user < 1 or id_user > 10:
        return 'Error'
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
    return menu(id)

def list_of_user_posts(id):
    '''інформація про  пости користувача'''
    global data_posts
    posts = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(posts)
    data_posts = r.json()
    print('List of user posts')
    for post in data_posts:
        if post['userId'] == id:
            print('id:', post['id'])
            print(post['title'])
            print('-' * 20)
            time.sleep(0.75)

def rec_comments(id_post):
    '''шатаєм коментарі'''
    comments = 'https://jsonplaceholder.typicode.com/comments'
    r = requests.get(comments)
    data_comments = r.json()
    counter = 0
    for comment in data_comments:
        if comment['postId'] == id_post:
            counter += 1
            print('id:',comment['id'], end='  ')
    print(f'Number of comments: {counter}')

def information_about_a_particular_post(id):
    '''інформація про конкретний пост'''
    id_post = int(input('Enter id post: '))
    for post in data_posts:
        if post['userId'] == id and post['id'] == id_post:
            print('id:', post['id'])
            print('title:', post['title'])
            print('body:', post['body'])
            rec_comments(id_post)

def menu_posts(id: int):
    '''проситиме ввести два значення для вибору переліку постів користувача або інформація про конкретний пост'''
    print('''
        Select 1 to see a list of user posts
        Select 2 to see information about a specific post
    ''')
    user_choice_posts = int(input('Your choice: '))
    if user_choice_posts == 1:
        list_of_user_posts(id)
    elif user_choice_posts == 2:
        information_about_a_particular_post(id)
    else:
        print('Invalid value entered')
    return menu(id)
def menu_todos(id):
    print('''
        Select 1 to see a list of completed tasks
        Select 2 to see a list of failed tasks
    ''')
    flaq = int(input('Your choice: '))
    if flaq == 1:
        for i in data_todos:
            if i['userId'] == id and i['completed'] == True:
                print(i['title'])
    elif flaq == 2:
        for i in data_todos:
            if i['userId'] == id and i['completed'] == False:
                print(i['title'])
    return menu(id)
def random_url_pic():
    ran_num = random.randint(1, 5000)
    for i in data_photos:
        if i['id'] == ran_num:
            print(i['url'])

def menu(id: int):
    print('''
        Select 1 to view complete user information
        Select 2 to go to the user's posts
        Select 3 to go to user tasks
        Select 4 to get the random picture URL
    ''')
    user_choice = int(input('Your choice: '))
    if user_choice == 1:
        complete_user_information(id)
    elif user_choice == 2:
        menu_posts(id)
    elif user_choice == 3:
        menu_todos(id)
    elif user_choice == 4:
        random_url_pic()
    return 'Your choice is not correct'

def start():
    i_return_brief_information_about_users()
    id_user = i_choose_the_user()
    if id_user == 'Error':
        print('Your choice is not correct!!')
        return
    menu(id_user)

start()