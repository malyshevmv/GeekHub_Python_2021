import requests

posts = 'https://jsonplaceholder.typicode.com/posts'
comments = 'https://jsonplaceholder.typicode.com/comments'
albums = 'https://jsonplaceholder.typicode.com/albums'
photos = 'https://jsonplaceholder.typicode.com/photos'
todos = 'https://jsonplaceholder.typicode.com/todos'
users = 'https://jsonplaceholder.typicode.com/users'

r = requests.get(users)
data = r.json()
# for i in data:
#     print(i)
# pars users
for i in data:
    for key, values in i.items():
        print(key, values)
    print('-------------------------------------------------------')