"""
Web page module for the Sunverge home page.
"""

from TestSuite_ProofOfConcept.page import Page


class HomePage(Page):
    """
    Page class for the Sunverge home page.
    """

    _page_title = 'Sunverge Energy | Home'

    def go_to_home_page(self):
        """
        Navigate to the home page.
        """
        self.selenium.get(self.base_url)
        self.check_page_title()
