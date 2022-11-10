from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.contrib.auth.models import User
from django.test import TestCase

class AuthenticationTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_open_a_log_in_page(self):
        self.browser.get('http://localhost:8000/accounts/login')
        self.assertIn('Executive Whitening - Login', self.browser.title)

    if __name__ == '__main__':
        unittest.main(warnings='ignore')

