# 'https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/'

import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import codecs
import html
from re import search

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

def parse_html(html: str) -> str:
    """Converting HTML -> Text"""

    elem = BeautifulSoup(html, features="html.parser")
    text = ''
    for e in elem.descendants:
        if isinstance(e, str):
            text += e.strip()
        elif e.name in ['br', 'p', 'h1', 'h2', 'h3', 'h4', 'tr', 'th']:
            text += '\n'
        elif e.name == 'li':
            text += '\n- '
        elif e.name == 'sup':
            text += '^'
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
task_code_func = data['props']['pageProps']['dehydratedState']['queries'][10]['state']['data']['question'][
    'codeSnippets'][3]['code']
task_code_func = task_code_func[task_code_func.index('def'):].strip()
task_code_func_name = search(r'\s([a-zA-Z0-9]*)\(', task_code_func).groups()[0]


def main_text_split(task_content: str) -> tuple:
    """Split content to two lists
    main_text - commented text at the beginning
    examples_list_4_vars - examples list with vars for Task"""

    # print(task_content)
    task_content_unescape = html.unescape(task_content)
    task_content_unescape = task_content_unescape.replace('<code>', '{')
    task_content_unescape = task_content_unescape.replace('</code>', '}')
    # task_content_unescape = task_content_unescape.replace('<strong>', ' ')
    # task_content_unescape = task_content_unescape.replace('</strong>', ' ')
    # print(task_content_unescape)

    main_text = BeautifulSoup(task_content_unescape, features="html.parser")

    examples = main_text.find_all('pre')

    for s in main_text.select('strong.example'):
        s.extract()
    for s in main_text.select('pre'):
        s.extract()
    for s in main_text.select('p'):
        if len(s.text.strip()) == 0:
            s.extract()

    for s in main_text.select('strong'):
        s.unwrap()
    for s in main_text.select('em'):
        s.unwrap()

    main_text = parse_html(str(main_text))
    # print(main_text)

    # Preparing all examples for split
    raw_examples_list = []
    for raw_example in examples:
        raw_examples_list.append(raw_example.text)

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

    return main_text, examples_list_4_vars


main_text, examples_list_4_vars = main_text_split(task_content)

template = f'''import unittest
from time import perf_counter

t1 = perf_counter()

"""
{task_num}
{main_text}
"""


{task_code_func}
    return


print({task_code_func_name}({examples_list_4_vars[0][0]})


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests'''

for i, example in enumerate(examples_list_4_vars):
    template += f'''
    def test0{i}_{task_code_func_name}(self):
        expected = {example[1]}
        actual = {task_code_func_name}({example[0]})
        self.assertEqual(expected, actual)
    '''

template += '''
t2 = perf_counter()
print(f'{{t2 - t1:.5f}} sec')
'''

with open(f'task00_{task_num}.py', 'w') as f:
    f.write(template)

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
