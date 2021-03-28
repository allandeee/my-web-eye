import requests
import unittest
from unittest.mock import Mock, patch
from sample.site_checker import SiteChecker, DCGBChecker


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

    @unittest.mock
if __name__ == '__main__':
    unittest.main()
