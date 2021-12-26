'''
1. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
   цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл та в базу. Результати зберегти в репозиторії.
   Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну сторінку і берете з неї URL). Хто захардкодить
   пагінацію зміною номеру сторінки в УРЛі - буде наказаний ;)
'''

import requests
from bs4 import BeautifulSoup
import pprint
import csv
import sqlite3 as sq
url = 'http://quotes.toscrape.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

#===========на сторінці находим цитати та їх авторів і додаємо в словник===========
lst_page_text = soup.select('span.text')
lst_page_author = soup.select('small.author')
dct_quote = {}
for txt, author in zip(lst_page_text, lst_page_author):
    if author.text not in dct_quote:
        dct_quote[author.text] = [txt.text]
    else:
        dct_quote[author.text].append(txt.text)

#шукаємо юрл на автора для інфи про нього
div = soup.find_all('div', class_='col-md-8')[1]
lst_author = div.select('a[href*="/author/"]')
lst_link_aut = []
for i in lst_author:
    lst_link_aut.append(i.attrs['href'])

#шукаємо як перейти на наступну сторінку
lst_next_page = soup.select('a[href*="/page/"]')
for i in lst_next_page:
    if 'Next' in i.text:
        next_page = i.attrs['href']
url_ = url + next_page
last_url = ''

#переходимо по всих сторінка сайту і отримаємо ВСІ цитати ВСИХ авторів
while url_ != last_url:
    r = requests.get(url_)
    soup = BeautifulSoup(r.text, 'lxml')
    #на всих сторінках сайту тре найти посилання на авторів
    div = soup.find_all('div', class_='col-md-8')[1]
    lst_author = div.select('a[href*="/author/"]')
    for i in lst_author:
        lst_link_aut.append(i.attrs['href'])
    #===========на сторінці находим цитати та їх авторів і додаємо в словник===========
    lst_page_text = soup.select('span.text')
    lst_page_author = soup.select('small.author')
    for txt, author in zip(lst_page_text, lst_page_author):
        if author.text not in dct_quote:
            dct_quote[author.text] = [txt.text]
        else:
            dct_quote[author.text].append(txt.text)
    #=================================
    # шкукаємо як перейти на наступну сторінку
    #print(soup.select('a[href*="/page/"]'))
    lst_next_page = soup.select('a[href*="/page/"]')
    for i in lst_next_page:
        if 'Next' in i.text:
            next_page = i.attrs['href']
    last_url, url_ = url_, url + next_page

#шукаємо інфу по автору
lst_link_aut = set(lst_link_aut)
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

with open('author_and_quote.csv', 'w', encoding='utf-8') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    w.writerow(('author', 'quote'))
    for k, v in dct_quote.items():
        w.writerow((k, v))

with open('description_of_the_author.csv', 'w', encoding='utf-8') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    w.writerow(('author', 'description'))
    for k, v in author_information.items():
        w.writerow((k, v))

with sq.connect('quotes_to_scrape.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS quotes (
        name TEXT NOT NULL,
        quote TEXT NOT NULL,
        description TEXT NOT NULL
        )''')
    for k_dct, k_author in zip(sorted(dct_quote), sorted(author_information)):
        cur.execute(f'''INSERT INTO quotes (name, quote, description)
            VALUES (?, ?, ?)
            ''', (k_dct, str(dct_quote[k_dct]), author_information[k_author]))