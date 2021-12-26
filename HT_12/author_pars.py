import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/author/Albert-Einstein/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
h3 = soup.find('h3', class_='author-title')
name = h3.text
print(name)
div = soup.find('div', class_='author-description')
des = div.text
print(des.strip())