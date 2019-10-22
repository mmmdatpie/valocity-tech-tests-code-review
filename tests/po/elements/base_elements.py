from selenium.common.exceptions import TimeoutException, InvalidElementStateException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class BrowserObject(object):
    """
    Base Browser class
    """
    browser = None

    def set_browser(self, browser):
        self.browser = browser


class BaseElement(BrowserObject):
    """
    Base Element Class
    """
    locator = None

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, value=None, visible_filter=False):
        WebDriverWait(self.browser, 1).until(
            lambda driver: len(driver.find_elements_by_css_selector(self.locator)),
            "URL: {0} | Waiting for {1}, but didn't show up in time".format(self.browser.current_url, self.locator)
        )
        elements = self.browser.find_elements_by_css_selector(self.locator)
        return [e for e in elements if e.is_displayed()] if visible_filter else elements

    # -------- action method  --------#
    def click_field(self, index=0):
        """
        find a field on the page to click.
        :param index: which field you want to fill
        """
        try:
            element = self()[index]
            self.browser.execute_script('arguments[0].scrollIntoView(false)', element)
            self.browser.execute_script("window.scrollBy(0,250)", "")
            element.click()
        except TimeoutException:
            raise TimeoutException

    def fill_field(self, value, index=0):
        """
        find a field on the page to input value.
        :param index: which field you want to fill
        :param value: value to be filled into the field
        """
        try:
            field = self()[index]
            field.clear()
            field.send_keys(value)
            self.key_down(Keys.TAB)
            return field
        except TimeoutException:
            raise TimeoutException
        except InvalidElementStateException:
            raise InvalidElementStateException

    def key_down(self, key):
        """
        Key down action on website
        :param key: Key
        """
        actions = ActionChains(self.browser)
        actions.key_down(key)
        actions.perform()


class ElementCollection(BrowserObject):
    """
    Base page class
    """

    def set_browser(self, browser):
        self.browser = browser
        for elements in self.__dict__.values():
            if isinstance(elements, BaseElement):
                elements.set_browser(browser)
