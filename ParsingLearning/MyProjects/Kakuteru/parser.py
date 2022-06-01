from bs4 import BeautifulSoup
import requests
import random

import csv
import time

url = 'https://www.kakuteru.ru/'
headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

# req = requests.get(url, headers=headers)
# content = req.text

# with open('index.html', 'w', encoding="utf-8") as file:
#     file.write(content)

with open('index.html', encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, 'lxml')
allUrlTags = soup.find_all('a')
cleanUrl = []
for item in allUrlTags:
    if item.find("kakuteru") != None:
        cleanUrl.append(str(item.get('href')))
cleanUrl = list(set(cleanUrl))
cleanUrl.sort(key=len)
print(cleanUrl)
# for item in cleanUrl:
#     with open('list.csv', 'a', encoding='utf-8') as file:
#         writer = csv.writer(file, delimiter=',', lineterminator='\n')
#         writer.writerow(('URL', item))

