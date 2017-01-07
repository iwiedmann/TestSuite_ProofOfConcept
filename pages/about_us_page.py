"""
Web page module for the Sunverge "ABOUT US" page.
"""

from TestSuite_ProofOfConcept.globals import BASE_URL
from TestSuite_ProofOfConcept.page import Page


class AboutUsPage(Page):
    """
    Page class for the "ABOUT US" page.
    """

    _about_us_url = BASE_URL + "about-us/"
    _page_title = "Sunverge Energy | About us"

    def go_to_about_us_page(self):
        """
        Navigate to the about us page directly.
        """
        self.selenium.get(self._about_us_url)
        self.check_page_title()
