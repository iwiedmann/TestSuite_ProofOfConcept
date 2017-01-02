"""
Base class for webpage classes using the page object model.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from globals import MAX_WAIT_TIME, BASE_URL


class Page(object):
    """
    Base class for all webpages.
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
        Check the webpage title if a child webpage class title is defined.
        """
        if self._page_title:
            # TODO: finish this
            pass

#########################TODO remove this when done above
    @property
    def page_title(self):
        """
        Grab the webpage title.
        """
        # implicit waits don't work for page titles so use an explicit wait
        WebDriverWait(self.selenium, MAX_WAIT_TIME).until(EC.ti)
        return self.selenium.title

    @property
    def is_the_current_page(self):
        if self._page_title:
            page_title = self.page_title
            assert self._page_title in page_title

