import sys

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

scraped_files_dir = './webpages/'


def convert(s):
    str1 = ""
    return (str1.join(s))


search_string = sys.argv[1:]

search_string = convert(search_string)

search_string = search_string.replace(' ', '+')

browser = webdriver.Chrome()  # './chromedriver'

suchwort = 'NLP'

test = browser.get("https://medium.com/tag/" + suchwort + "/archive")

res = browser.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res, 'lxml')

links = []
for my_tag in soup.find_all(class_="button button--smaller button--chromeless u-baseColor--buttonNormal"):
    print(my_tag.get('href'))
    links.append(my_tag.get('href'))

print(links)
content_dict = {}
for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    content = soup.prettify()
    content_dict[link] = content

    # table = soup.findAll('h1', attrs = {'class':'content-heading'})

# content_dict.to_csv('Medium.csv', sep='|', encoding='latin1', index=False)
import json

with open('Medium_' + suchwort + '.txt', 'w') as file:
    file.write(json.dumps(content_dict))
