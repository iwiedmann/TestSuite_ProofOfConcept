"""
Base module for web page classes using the page object model.
"""

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from globals import MAX_WAIT_TIME, BASE_URL


class Page(object):
    """
    Base class for all pages.
    """

    def __init__(self, selenium):
        """
        Initialize pytest-selenium and set an implicit wait.
        :param selenium: pytest-selenium fixture
        """
        self.selenium = selenium
        self.base_url = BASE_URL
        self.selenium.implicitly_wait(MAX_WAIT_TIME)

    def check_page_title(self):
        """
        Check the page title if a child class webpage title is defined.
        """
        if self._page_title:
            # implicit waits don't work for page titles so use an explicit wait
            wait = WebDriverWait(self.selenium, MAX_WAIT_TIME)
            try:
                wait.until(EC.title_contains(self._page_title))
            except TimeoutException:
                pytest.fail("Webpage title '{title}' was not found".format(title=self._page_title))
