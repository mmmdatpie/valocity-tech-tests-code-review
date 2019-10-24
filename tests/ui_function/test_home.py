import pytest

from tests import config
from tests.base_selenium import SeleniumCase
from tests.po.objects.home_objects import HomeObjects


@pytest.mark.readonly
class HomeTest(SeleniumCase):

    def setUp(self):
        self.home = HomeObjects(self.browser, config.SEARCH_BUTTON, config.SEARCH_TEXT)
        self.home.open_url(config.TEST_ADDRESS)

    def test_searching_the_key_word(self):
        self.home.search_key_word(config.SEARCHING_KEY)  # replaced string literal with config value
