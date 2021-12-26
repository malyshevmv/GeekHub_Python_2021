import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

#lst_href = soup.attrs['href']
#print(lst_href)

div = soup.find_all('div', class_='col-md-8')[1]
lst_author = div.select('a[href*="/author/"]')
lst_link_aut = []
for i in lst_author:
    lst_link_aut.append(i.attrs['href'])

print(lst_link_aut)
author_information = {}
for link in lst_link_aut:
    url = 'http://quotes.toscrape.com'
    r = requests.get(url + link)
    soup = BeautifulSoup(r.text, 'lxml')
    h3 = soup.find('h3', class_='author-title')
    name = h3.text.strip()
    print(name)
    div = soup.find('div', class_='author-description')
    des = div.text.strip()
    print(des)
    if name not in author_information:
        author_information[name] = des

print(author_information)