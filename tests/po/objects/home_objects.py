from tests.base_page import BasePage
from tests.po.elements.ui.home.home_elements import HomeElements


class HomeObjects(BasePage):

    """
    HomeObjects class which is an object that is used to represent a page with a search bar
    """

    # modified the home class so it can have different search buttons and search text

    def __init__(self, browser, search_button, search_text):
        """
        :param browser: selenium webdriver browser that is to be set
        :param search_button: name of the search button
        :param search_text: title of the search area
        """
        self.home = HomeElements(search_text, search_button)
        self.set_browser(browser)

    def open_url(self, url):  # changed function. Takes the url as a paramater and passes it to go_to_url function
        """
        opens the url
        :param url: string which is the address of a page to be opened
        """
        self.go_to_url(url)
        self.home.search_button()

    ###
    # Logic
    ###

    def search_key_word(self, key_word):
        """
        enters keyword into the search field and clicks search button
        :param key_word: string to be entered into the search field
        """
        self.fill_search_text(key_word)
        self.click_search_button()

    ###
    # Page Actions
    ###

    def fill_search_text(self, value=None):
        """
        enters the given value into the field
        :param value: value to be entered into field, defaults to none
        """
        self.home.search_text.fill_field(value)

    def click_search_button(self):
        """
        clicks the search button
        """
        self.home.search_button.click_field(index=1)
