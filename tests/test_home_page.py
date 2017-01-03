"""
Test for the Sunverge corporate home page.
"""

from TestSuite_ProofOfConcept.webpages.home_page import HomePage


def test_navigate_to_about_us_page(selenium):
    """
    Test that you can navigate to the "ABOUT US" page through the link.
    """
    home_pg = HomePage(selenium)
    home_pg.go_to_home_page()
    # TODO: finish this test
