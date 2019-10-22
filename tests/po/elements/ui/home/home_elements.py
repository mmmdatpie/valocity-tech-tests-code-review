"""
Home Elements
"""

from tests.po.elements.async_elements import AsyncElement
from tests.po.elements.base_elements import ElementCollection


class HomeElements(ElementCollection):

    def __init__(self):
        self.search_text = AsyncElement('input[aria-label="Search"]')
        self.search_button = AsyncElement('input[aria-label="Google Search"]')
