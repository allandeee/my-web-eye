import requests
from bs4 import BeautifulSoup
from sample.exceptions import ItemContentError


class SiteChecker(object):

    TITLE = ''

    def __init__(self, url):
        self.url = url

    @property
    def page(self):
        return requests.get(self.url)

    def get_latest_content(self):
        raise NotImplementedError

    def get_latest_content_items(self):
        raise NotImplementedError

    def print_content(self):
        print()
        print(self.TITLE)
        print(self.get_latest_content_items())
        print()


class DCGBChecker(SiteChecker):

    TITLE = 'DailyClack Groupbuy Check'

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
            if item_price and not item_availability:
                result.append((item_name.text, item_price.text.strip()))
            elif item_availability:
                result.append((item_name.text, item_availability.text.strip()))
        return result


class DCItemChecker(SiteChecker):

    TITLE = 'DailyClack 7V Check'

    def __init__(self, *args):
        super().__init__(
            'https://dailyclack.com/collections/pcbs-kits/products/7v-extras'
        )

    def get_latest_content(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        return soup.find('div', class_='product-single__meta')

    def get_item_availability(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        button = soup.find('div', class_='product-form__item--submit')
        avail = button.find(
            'span', {'id': 'AddToCartText-product-template'}
        ).text.strip()
        if avail.lower() != 'sold out':
            return 'Available'
        return avail

    def get_latest_content_items(self):
        elem = self.get_latest_content()
        if elem:
            item_title = elem.find(
                'h1', class_='product-single__title'
            ).text
            item_price = elem.find(
                'span', class_='product-single__price'
            ).text.strip()
            return {
                'title': item_title,
                'price': item_price,
                'availability': self.get_item_availability()
            }
        raise ItemContentError()


class DCSevenVChecker(DCItemChecker):
    pass
