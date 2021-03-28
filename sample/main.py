#! /usr/bin/python3

from site_checker import DCGBChecker

dc_checker = DCGBChecker()

for r in dc_checker.get_latest_content():
    item_name = r.find('div', class_='product-card__name')
    item_availability = r.find('div', class_='product-card__availability')
    item_price = r.find('div', class_='product-card__price')
    print(item_name.text)
    if item_price and not item_availability:
        print(item_price.text.strip())
    elif item_availability:
        print(item_availability.text.strip())
