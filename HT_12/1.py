"""
1. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
   цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл та в базу.
   Результати зберегти в репозиторії.
   Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну сторінку і берете з неї URL).
   Хто захардкодить пагінацію зміною номеру сторінки в УРЛі - буде наказаний ;)
"""

import requests
from bs4 import BeautifulSoup
import csv
import sqlite3 as sq
import pprint

url = 'http://quotes.toscrape.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

def search_for_quotes(u):
    r = requests.get(u)
    soup = BeautifulSoup(r.text, 'lxml')
    lst_quotes = soup.select('span.text')
    return lst_quotes

def search_for_authors(u):
    r = requests.get(u)
    soup = BeautifulSoup(r.text, 'lxml')
    lst_author = soup.select('small.author')
    return lst_author

def search_for_tags(u):
    r = requests.get(u)
    soup = BeautifulSoup(r.text, 'lxml')
    lst = soup.find_all('div', class_='tags')
    lst_tags = []
    for i in lst:
        lst_tags.append(i.text[32:])
    return lst_tags
data = {}
for quote, author, tag in zip(search_for_quotes(url), search_for_authors(url), search_for_tags(url)):
    data[quote.text] = {author.text: tag}

div = soup.find_all('div', class_='col-md-8')[1]
lst_author = div.select('a[href*="/author/"]')
lst_link_aut = []
for i in lst_author:
    if i.attrs['href'] not in lst_link_aut:
        lst_link_aut.append(i.attrs['href'])

lst_next_page = soup.select('a[href*="/page/"]')
for i in lst_next_page:
    if 'Next' in i.text:
        next_page = i.attrs['href']
url_ = url + next_page
last_url = ''

while url_ != last_url:
    r = requests.get(url_)
    soup = BeautifulSoup(r.text, 'lxml')
    # на всих сторінках сайту тре найти посилання на авторів
    div = soup.find_all('div', class_='col-md-8')[1]
    lst_author = div.select('a[href*="/author/"]')
    for i in lst_author:
        if i.attrs['href'] not in lst_link_aut:
            lst_link_aut.append(i.attrs['href'])
    for quote, author, tag in zip(search_for_quotes(url_), search_for_authors(url_), search_for_tags(url_)):
        data[quote.text] = {author.text: tag}
    lst_next_page = soup.select('a[href*="/page/"]')
    for i in lst_next_page:
        if 'Next' in i.text:
            next_page = i.attrs['href']
    last_url, url_ = url_, url + next_page

author_information = {}
for link in lst_link_aut:
    url = 'http://quotes.toscrape.com'
    r = requests.get(url + link)
    soup = BeautifulSoup(r.text, 'lxml')
    h3 = soup.find('h3', class_='author-title')
    name = h3.text.strip()
    div = soup.find('div', class_='author-description')
    des = div.text.strip()
    if name not in author_information:
        author_information[name] = des


with open('author_and_quote.csv', 'w', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(('quote', 'author', 'tags'))
    for k, v, in data.items():
        for k_v, v_v in v.items():
            w.writerow((k, k_v, v_v))

with open('description_of_the_author.csv', 'w', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(('author', 'description'))
    for k, v in author_information.items():
        w.writerow((k, v))

with sq.connect('quotes_to_scrape.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS quotes (
        name TEXT NOT NULL,
        quote TEXT NOT NULL
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS author_information (
        name TEXT NOT NULL,
        description TEXT NOT NULL
        )''')
    for k, v in data.items():
        for k_v, v_v in v.items():
            cur.execute('''INSERT INTO quotes (name, quote)
            VALUES (?, ?)
            ''', (k_v, k))
    for k, v in author_information.items():
        cur.execute('''INSERT INTO author_information (name, description)
            VALUES (?, ?)
            ''', (k, v))