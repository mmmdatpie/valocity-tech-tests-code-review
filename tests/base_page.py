from tests.po.elements.base_elements import BrowserObject, ElementCollection


class BasePage(BrowserObject):
    """
    Base class to initialize the base page
    """
    view_name = None
    browser = None

    def set_browser(self, browser):
        """
        Sets attribute browser to the give paramater browser
        :param browser: selenium webdriver browser that is to be set
        """
        self.browser = browser
        for elements in self.__dict__.values():
            if isinstance(elements, ElementCollection):
                elements.set_browser(browser)

    def go_to_url(self, url):
        """
        Makes a get request to the provided url
        :param url: string which is the address of a page to make the get request to
        """
        self.browser.get(url)


# removed function that was never used
