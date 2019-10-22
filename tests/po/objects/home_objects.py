from tests.base_page import BasePage
from tests.po.elements.ui.home.home_elements import HomeElements


class HomeObjects(BasePage):

    def __init__(self, browser):
        self.home = HomeElements()
        self.set_browser(browser)

    def open_url(self):
        self.go_to_url()
        self.home.search_button()

    ###
    # Logic
    ###
    def search_key_word(self, key_word):
        self.fill_search_text(key_word)
        self.click_search_button()

    ###
    # Page Actions
    ###
    def fill_search_text(self, value=None):
        self.home.search_text.fill_field(value)

    def click_search_button(self):
        self.home.search_button.click_field(index=1)
