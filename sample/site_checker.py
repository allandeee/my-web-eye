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
