"""
Home Elements
"""

from tests.po.elements.async_elements import AsyncElement
from tests.po.elements.base_elements import ElementCollection


class HomeElements(ElementCollection):

    def __init__(self, search_text, search_button):  # removed the hard coded strings
        self.search_text = AsyncElement(search_text)
        self.search_button = AsyncElement(search_button)
