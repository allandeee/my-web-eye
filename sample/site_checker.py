import requests
from bs4 import BeautifulSoup


class SiteChecker(object):

    def __init__(self, url):
        self.url = url

    @property
    def page(self):
        return requests.get(self.url)

    def get_latest_content(self):
        raise NotImplementedError


class DCGBChecker(SiteChecker):

    def __init__(self, *args):
        super().__init__(
            'https://dailyclack.com/collections/group-buys'
        )

    def get_latest_content(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')

        results = soup.find_all('div', class_='product-card__info')

        return results[:5]

    def get_latest_content_items(self):
        result = []
        for r in self.get_latest_content():
            item_name = r.find('div', class_='product-card__name')
            item_availability = r.find(
                'div', class_='product-card__availability')
            item_price = r.find('div', class_='product-card__price')
            print(item_name.text)
            if item_price and not item_availability:
                result.append((item_name.text, item_price.text.strip()))
            elif item_availability:
                result.append((item_name.text, item_availability.text.strip()))
        return result
