import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class AutTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = 'http://localhost:4444'

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        url = os.environ.get('URL')

        self.browser.get(url)
        self.browser.save_screenshot('screenshot.png')
        expected_result = "Welcome back, Guest!"      
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')

        self.assertIn(expected_result, actual_result.text)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'],verbosity=2,warnings='ignore')

