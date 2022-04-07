from bs4 import BeautifulSoup
import re
import requests

session = requests.session()
url = 'https://kovalut.ru/kurs/samara/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

res = session.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)

# ourText = soup.findAll('div', class_='th-title')
# for item in ourText:
#     print(item.text)
