import pytest

from tests.base_selenium import SeleniumCase
from tests.po.objects.home_objects import HomeObjects


@pytest.mark.readonly
class HomeTest(SeleniumCase):

    def setUp(self):
        self.home = HomeObjects(self.browser)
        self.home.open_url()

    def test_searching_the_key_word(self):
        self.home.search_key_word('Valocity')
