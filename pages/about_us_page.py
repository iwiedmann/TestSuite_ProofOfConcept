"""
Web page module for the Sunverge "ABOUT US" page.
"""

from copy import deepcopy

from selenium.webdriver.common.by import By

from TestSuite_ProofOfConcept.globals import BASE_URL
from TestSuite_ProofOfConcept.page import Page


class AboutUsPage(Page):
    """
    Page class for the "ABOUT US" page.
    """

    _about_us_url = BASE_URL + 'about-us/'
    _page_title = 'Sunverge Energy | About us'

    # locators

    # collections of locators
    _all_sections_locators = {
        "vision_section_locator": (By.ID, 'top-section'),
        "management_section_locator": (By.ID, 'executive-team'),
        "directors_section_locator": (By.ID, 'boardsec'),
        "investors_section_locator": (By.ID, 'investors')
    }

    def go_to_about_us_page(self):
        """
        Navigate to the about us page
         directly.
        """
        self.selenium.get(self._about_us_url)
        self.check_page_title()

    def are_all_sections_visible(self):
        """
        Checks that all the sections on the page are visible.
        :return: visibility_results: a dictionary with showing which locators were visible
        """
        visibility_results = deepcopy(self._all_sections_locators)
        for locator_name, locator in self._all_sections_locators.iteritems():
            if self.is_element_visible(*locator):
                visibility_results[locator_name] = True
            else:
                visibility_results[locator_name] = False
        return visibility_results
