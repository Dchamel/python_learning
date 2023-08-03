# 'https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/'

import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import codecs

URL = 'https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/'

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
with open("tmp.html", "r", encoding='utf-8') as f:
    html = f.read()

    soup = BeautifulSoup(html, "lxml")
    script = soup.find('script', {'id': '__NEXT_DATA__'}).text
    data = json.loads(script)
    # data = json.dumps(data, indent=4, sort_keys=True)
    # with open('tmp.json', 'w') as f:
    # json.dump(data, f)

    print(data['props']['pageProps']['dehydratedState'])

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
