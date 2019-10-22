from selenium.webdriver.support.ui import WebDriverWait
from tests.po.elements.base_elements import BaseElement


class AsyncElement(BaseElement):
    """
    Base element for those elements which definitely need to be waited.
    """
    def __call__(self, value=None, visible_filter=False):
        WebDriverWait(self.browser, 10).until(
            lambda driver: len([e for e in driver.find_elements_by_css_selector(self.locator) if e.is_displayed()]
                               if visible_filter else driver.find_elements_by_css_selector(self.locator)),
            "URL: {0} | Waiting for {1}, but didn't show up in time".format(
                self.browser.current_url, self.locator
            )
        )
        return super(AsyncElement, self).__call__(value, visible_filter)
