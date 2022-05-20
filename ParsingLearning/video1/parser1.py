# https://yandex.ru/news
# https://www.saskatoonpublicschools.ca/program/online/About/Pages/Calendar.aspx
import re

from bs4 import BeautifulSoup

with open('test.html') as file:
    file = file.read()

soup = BeautifulSoup (file, 'lxml')

title = soup.title
print(title.text)
print(title.string)

pageH1 = soup.find('h1').text
print(pageH1)

pageH1all = soup.findAll('h1')
print(pageH1all)
for item in pageH1all:
    print(item.text.strip())

data1 = soup.find('div', class_='names').find('a')
print(data1.text)

data2 = soup.findAll('td', {'class':'hidden-xs'})
data3 = data2[2].findNext('span').text
print(data3)

data4 = soup.find('td', {'class':'hidden-xs', 'id':'aaa'}).text
print(data4)

allSpans = soup.find('body').find_all('span')
print(allSpans)
print('')
for item in allSpans:
    print(item.text)

linksAll = soup.findAll('a')
for item in linksAll:
    url = item.get('href')
    print(f'http://www.pipiko.com{url}')

print('')
dataDiv = soup.find(class_='fs-2222').find_parent()
print(dataDiv)

print('')
nextElement = soup.find(class_='names').next_element
print(nextElement)

print('')
nextElement = soup.find(class_='names').find_next()
print(nextElement)

print('')
sibling1 = soup.find(class_='names').find_next_sibling()
print(sibling1)

print('')
sibling2 = soup.find(class_='namesData').find_previous_sibling()
print(sibling2)

print('')
spanishe = soup.find(class_='odd').find_previous_sibling().find_next('span').text
print(spanishe)

print('')
links = soup.find(class_='someLinks').find_all('a')
for link in links:
    linkHref = link.get('href')
    linkAttr = link.get('data-attr')
    linkAttr2 = link['data-attr']
    print(linkHref,'-',linkAttr)
    print(linkAttr2)

print('')
findByText = soup.find('a', text=re.compile('Radios'))
print(findByText)

print('')
findAllThings = soup.find_all(text=re.compile('([Rr]adios)'))
print(findAllThings)