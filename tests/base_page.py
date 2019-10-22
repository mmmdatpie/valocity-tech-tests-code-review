from tests import config
from tests.po.elements.base_elements import BrowserObject, ElementCollection


class BasePage(BrowserObject):
    """
    Base class to initialize the base page
    """
    view_name = None
    browser = None

    def set_browser(self, browser):
        self.browser = browser
        for elements in self.__dict__.values():
            if isinstance(elements, ElementCollection):
                elements.set_browser(browser)

    def go_to_url(self):
        """
        make a get request
        """
        url = config.TEST_ADDRESS
        self.browser.get(url)

    def get_current_url(self):
        """
        Get current url.
        """
        return self.browser.current_url
