import requests
import csv


def scraper(category='newstories'):
    """ Функція-генератор приймає категорію статей
    робе реквест по категорії, зберігаючи список id статей
    потім через цикл for робим реквест до конкретної статті
    і через yield повертаємо цю статтю
    """
    lst_category = ['askstories', 'showstories', 'newstories', 'jobstories']
    if category not in lst_category:
        yield 'The selected category does not exist'
    url = f'https://hacker-news.firebaseio.com/v0/{category}.json?print=pretty'
    id_stories = requests.get(url)
    lst_id_stories = id_stories.json()

    for id_stories in lst_id_stories:
        url_stories = f'https://hacker-news.firebaseio.com/v0/item/{id_stories}.json?print=pretty'
        r = requests.get(url_stories)
        res = r.json()
        yield res


input_category = input('Enter category: ')
for stories in scraper(input_category):
    with open(f'{input_category}.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=':')
        if type(stories) == dict():
            for key, value in stories.items():
                writer.writerow([key, value])
        else:
            print('The selected category does not exist')
            break
