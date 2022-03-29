from bs4 import BeautifulSoup
import requests

# Sending header for web-site. Simple protection if request blocking by site.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

res = requests.get('https://www.bookvoed.ru/author?id=153717', headers=headers)

soup = BeautifulSoup(res.text, 'lxml')
# ourHeader = soup.find('h2', class_='QT')
ourText = soup.find('div', class_='GT')

spisok = []
for eachPart in ourText:
    spisok.append(eachPart.get_text(strip=True))
spisok = list(filter(None, spisok))

print(spisok)