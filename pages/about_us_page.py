"""
Web page module for the Sunverge about us page.
"""

from copy import deepcopy

from selenium.webdriver.common.by import By

from TestSuite_ProofOfConcept.globals import BASE_URL
from TestSuite_ProofOfConcept.page import Page


class AboutUsPage(Page):
    """
    Page class for the about us page.
    """

    _about_us_url = BASE_URL + 'about-us/'
    _page_title = 'Sunverge Energy | About us'

    # locators

    # groups of locators
    _all_sections_locators = {
        "vision_section_locator": (By.ID, 'top-section'),
        "management_section_locator": (By.ID, 'xecutive-team'),
        "directors_section_locator": (By.ID, 'boardsec'),
        "investors_section_locator": (By.ID, 'nvestors')
    }

    def go_to_about_us_page(self):
        """
        Navigate to the about us page
         directly.
        """
        self.selenium.get(self._about_us_url)
        self.check_page_title()

    @property
    def expect_all_sections_visible(self):
        """
        Get the expected visibility results for all the about us page sections.
        :return: expected_visibility_results: expect that all sections should be visible
        """
        expected_visibility_results = deepcopy(self._all_sections_locators)
        for locator_name, locator in self._all_sections_locators.iteritems():
            expected_visibility_results[locator_name] = "is visible"
        return expected_visibility_results

    def are_all_sections_visible(self):
        """
        Checks that all the sections on the page are visible or not.
        :return: visibility_results: a dictionary with showing which locators were visible
        """
        visibility_results = deepcopy(self._all_sections_locators)
        for locator_name, locator in self._all_sections_locators.iteritems():
            if self.is_element_visible(*locator):
                visibility_results[locator_name] = "is visible"
            else:
                visibility_results[locator_name] = "is not visible"
        return visibility_results
