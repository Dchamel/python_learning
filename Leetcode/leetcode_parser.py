# 'https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/'

import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import codecs
import html
import re

# URL = 'https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/'
URL = 'https://leetcode.com/problems/sort-the-people'


# # Run Scrapper
# service = Service(executable_path=r'C:\Chrome\chromedriver.exe')
# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# driver = webdriver.Chrome(service=service, options=options)
# driver.get(URL)
# html = driver.page_source
#
# completeName = os.path.join('', 'tmp.html')
# file_object = codecs.open(completeName, "w", "utf-8")
# file_object.write(html)
#
# driver.quit()

# Parse data from RAW html

def parse_html(html):
    elem = BeautifulSoup(html, features="html.parser")
    text = ''
    for e in elem.descendants:
        if isinstance(e, str):
            text += e.strip()
        elif e.name in ['br', 'p', 'h1', 'h2', 'h3', 'h4', 'tr', 'th']:
            text += '\n'
        elif e.name == 'li':
            text += '\n- '
    return text


with open("tmp.html", "r", encoding='utf-8') as f:
    html_data = f.read()

soup = BeautifulSoup(html_data, "lxml")
script = soup.find('script', {'id': '__NEXT_DATA__'}).text
data = json.loads(script)
# data = json.dumps(data, indent=4, sort_keys=True)
# with open('tmp.json', 'w') as f:
# json.dump(data, f)

task_num = data['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['question'][
    'questionFrontendId']
task_title = data['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['question'][
    'title']
task_content = data['props']['pageProps']['dehydratedState']['queries'][6]['state']['data']['question']['content']


def main_text_split(task_content: str) -> str:
    main_text_finished = ''
    task_content_unescape = html.unescape(task_content)
    task_content_unescape = task_content_unescape.replace('<code>', '<')
    task_content_unescape = task_content_unescape.replace('</code>', '>')
    elem = BeautifulSoup(task_content_unescape, features="html.parser")
    examples = elem.find_all('pre')
    # print(examples)
    for s in elem.select('div', {'class': 'example'}):
        s.extract()
    print(elem)

    # Preparing all examples for split
    raw_examples_list = []
    for raw_example in examples:
        raw_examples_list.append(raw_example.text)
    # print(raw_examples_list)

    # Splitting Examples and putting them to final list
    examples_list_splitted = []
    for raw_example in raw_examples_list:
        examples_list_splitted.append(raw_example.split('\n'))
    examples_list_4_vars = []
    for example in examples_list_splitted:
        example_str_list = [i for i in example if i]
        example_str_list2 = []
        for string in example_str_list:
            match string:
                case string if string.startswith('Input: '):
                    example_str_list2.append(string.replace('Input: ', ''))
                case string if string.startswith('Output: '):
                    example_str_list2.append(string.replace('Output: ', ''))
        examples_list_4_vars.append(example_str_list2)
    # print(examples_list_4_vars)
    main_text_finished = task_content_unescape
    # print(main_text_finished)
    return main_text_finished, examples_list_4_vars


main_text_split(task_content)
# print(example_input[1].replace('Input: ', ''))
# print(example_input[2].replace('Output: ', ''))
# print(example_input[3].replace('Explanation: ', ''))

# q = parse_html(task_content_unescape)
# print(task_num)
# print(task_title)
# print(task_content_unescape)
# print(q)

# soup = BeautifulSoup(html, "html.parser")
# script = soup.find('script', {'id': '__NEXT_DATA__'})
# data = json.loads(script.get_text(strip=True))

# # Write it to the file
# with open("tmp.json", "w") as f:
#     json.dump(data, f)

# with open('tmp.json', 'r') as f:
#     x = json.load(f)
#
# print(x)
