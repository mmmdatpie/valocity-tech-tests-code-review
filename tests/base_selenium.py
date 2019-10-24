import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tests import config


class SeleniumWebDriver(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SeleniumWebDriver, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        options = Options()
        self.profile = webdriver.FirefoxProfile()
        self.browser = webdriver.Firefox(options=options)


class SeleniumCase(unittest.TestCase):
    """
    Base Selenium Class
    """
    browser = None

    base_url = config.TEST_ADDRESS
    automation_bug_list = []

    @classmethod
    def setUpClass(cls):
        super(SeleniumCase, cls).setUpClass()
        cls.browser = SeleniumWebDriver().browser

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(SeleniumCase, cls).tearDownClass()
