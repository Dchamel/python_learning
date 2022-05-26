import json
import csv
import random
import time

import requests
from bs4 import BeautifulSoup

# url = 'https://health-diet.ru/table_calorie/'
#
headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
# req = requests.get(url, headers=headers)
# src = req.text

# with open('index.html', 'w', encoding="utf-8") as file:
#     file.write(src)

# with open('index.html', encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_prod_hrefs = soup.findAll(class_='mzr-tc-group-item-href')
#
# all_categories_dict = {}
# for item in all_prod_hrefs:
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item.get('href')
#     # print(f'https://health-diet.ru{item_href}', item_text )
#     all_categories_dict[item_text] = item_href
#
# with open('all_categories_dect.json', 'w', encoding="utf-8") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open('all_categories_dect.json', encoding="utf-8") as file:
    all_categories = json.load(file)

iteration_count=int(len(all_categories))-1
count = 0
print(f'All Iterations: {iteration_count}')

for cat_name, cat_href in all_categories.items():

    rep = [',',' ','-','\'']
    for item in rep:
        if item in cat_name:
            cat_name = cat_name.replace(item, '_')

    req = requests.get(url=cat_href, headers=headers)
    src = req.text

    with open(f'data/{count}_{cat_name}.html', 'w', encoding="utf-8") as file:
        file.write(src)

    with open(f'data/{count}_{cat_name}.html', encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    # check website page for product table
    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue

    #table headers
    table_header = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
    product = table_header[0].text
    calories = table_header[1].text
    proteins = table_header[2].text
    fats = table_header[3].text
    carbohydrates = table_header[4].text

    with open(f'data/{count}_{cat_name}.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', lineterminator='\n')
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )

    #collect product data
    products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

    products_info = []

    for item in products_data:
        prod_info = item.find_all('td')
        title = prod_info[0].find('a').text
        calories = prod_info[1].text
        proteins = prod_info[2].text
        fats = prod_info[3].text
        carbohydrates = prod_info[4].text

        products_info.append(
            {
                'Title': title,
                'Calories' : calories,
                'Proteins' : proteins,
                'Fats' : fats,
                'Carbohydrates' : carbohydrates
            }
        )

        with open(f'data/{count}_{cat_name}.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
    with open(f'data/{count}_{cat_name}.json', 'a', encoding='utf-8') as file:
        json.dump(products_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f'# Iteration {iteration_count} finished. Category: {cat_name}')
    iteration_count -=1

    if iteration_count == 0:
        print('Job is finished')
        break

    print(f'Iterations left: {iteration_count}')
    time.sleep(random.randrange(2, 4))