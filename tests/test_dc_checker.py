import requests
import unittest
from unittest.mock import Mock, patch
from sample.site_checker import (
    SiteChecker, DCGBChecker, DCItemChecker
)
from sample.exceptions import ItemContentError


class TestSiteChecker(unittest.TestCase):

    def test_init(self):
        site_checker = SiteChecker(
            url='https://example.com'
        )
        self.assertEqual(
            site_checker.url,
            'https://example.com'
        )

    def test_page(self):
        site_checker = SiteChecker(
            url='https://example.com'
        )
        self.assertEqual(
            site_checker.page.status_code,
            200
        )

    def test_get_latest_content(self):
        site_checker = SiteChecker(
            url='https://example.com'
        )
        with self.assertRaises(NotImplementedError):
            site_checker.get_latest_content()


class TestDCGBChecker(unittest.TestCase):

    def test_page(self):
        dc_checker = DCGBChecker()
        self.assertEqual(
            dc_checker.page.status_code,
            200
        )

    def test_get_latest_content(self):
        dc_checker = DCGBChecker()
        self.assertEqual(
            len(dc_checker.get_latest_content()),
            5
        )


class TestDCItemChecker(unittest.TestCase):

    def test_page(self):
        item_checker = DCItemChecker()
        self.assertEqual(
            item_checker.page.status_code,
            200
        )

    def test_get_latest_content(self):
        item_checker = DCItemChecker()
        self.assertIsNotNone(
            item_checker.get_latest_content()
        )

    def test_get_item_availability(self):
        item_checker = DCItemChecker()
        self.assertIsNotNone(
            item_checker.get_item_availability()
        )

    def test_get_latest_content_items(self):
        item_checker = DCItemChecker()
        item = item_checker.get_latest_content_items()
        self.assertIsInstance(
            item['title'], str
        )
        self.assertIsInstance(
            item['price'], str
        )
        self.assertIsInstance(
            item['availability'], str
        )

    @patch.object(
        DCItemChecker, 'get_latest_content'
    )
    def test_get_latest_content_items_raises_error(
            self, mock_content):
        mock_content.return_value = None
        item_checker = DCItemChecker()
        with self.assertRaises(ItemContentError):
            item_checker.get_latest_content_items()


if __name__ == '__main__':
    unittest.main()
