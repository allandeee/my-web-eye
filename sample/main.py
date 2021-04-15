#! /usr/bin/python3

from site_checker import DCGBChecker, DCSevenVChecker

dc_checker = DCGBChecker()
dc_checker.print_content()

print('===')

seven_v = DCSevenVChecker()
seven_v.print_content()

print('===')
