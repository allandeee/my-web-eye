import unittest
from sample.site_checker import SiteChecker


class TestSiteChecker(unittest.TestCase):

    def test_init(self):
        site_checker = SiteChecker(
            url='https://example.com'
        )
        self.assertEqual(
            site_checker.url,
            'https://example.com'
        )

    def test_get_latest_content(self):
        site_checker = SiteChecker(
            url='https://example.com'
        )
        with self.assertRaises(NotImplementedError):
            site_checker.get_latest_content()


if __name__ == '__main__':
    unittest.main()
