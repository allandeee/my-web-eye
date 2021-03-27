#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = 'https://dailyclack.com/collections/group-buys'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_='product-card__info')

for r in results[:4]:
    item_name = r.find('div', class_='product-card__name')
    item_availability = r.find('div', class_='product-card__availability')
    item_price = r.find('div', class_='product-card__price')
    print(item_name.text)
    if item_price and not item_availability:
        print(item_price.text.strip())
    elif item_availability:
        print(item_availability.text.strip())
