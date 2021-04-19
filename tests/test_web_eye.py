import unittest
from unittest.mock import call, Mock, patch
from sample.web_eye import WebEye
from sample.site_checker import DCGBChecker, DCSevenVChecker


class TestWebEye(unittest.TestCase):

    @patch('builtins.print')
    @patch.object(
        DCSevenVChecker, 'print_content'
    )
    @patch.object(
        DCGBChecker, 'print_content'
    )
    def test__reader(self, mock_dc_cont, mock_seven_cont, mock_print):
        WebEye._reader()
        mock_dc_cont.assert_called_once()
        mock_seven_cont.assert_called_once()
        mock_print.assert_has_calls([call('==='), call('===')])
