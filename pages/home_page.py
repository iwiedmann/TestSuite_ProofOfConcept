"""
Web page module for the Sunverge home page.
"""

from selenium.webdriver.common.by import By

from TestSuite_ProofOfConcept.page import Page
from about_us_page import AboutUsPage


class HomePage(Page):
    """
    Page class for the Sunverge home page.
    """

    _page_title = 'Sunverge Energy | Home'

    # locator building blocks
    _row_header_xpath = '/html/body/div[1]/div/div[2]'

    # locators
    _sunverge_logo_locator = (By.XPATH, _row_header_xpath + '/div/a/img')
    _about_us_link_locator = (By.XPATH, _row_header_xpath + '/nav[1]/ul/li[3]/a')

    def go_to_home_page(self):
        """
        Navigate to the home page directly.
        """
        self.selenium.get(self.base_url)
        self.check_page_title()

    def go_to_about_us_page(self):
        """
        Navigate to the about us page through the "ABOUT US" link.
        :return: object for the "ABOUT US" page
        """
        self.selenium.find_element(*self._about_us_link_locator).click()
        return AboutUsPage(self.selenium)

    def is_sunverge_logo_visible(self):
        """
        Check if the Sunverge logo is visible.
        :return: boolean of whether the element is visible
        """
        return self.is_element_visible(*self._sunverge_logo_locator)
