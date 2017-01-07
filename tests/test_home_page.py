"""
Test for the Sunverge corporate home page.
"""

from TestSuite_ProofOfConcept.pages.home_page import HomePage


def test_sunverge_logo(selenium):
    """
    Test that the Sunverge logo is visible.
    """
    home_pg = HomePage(selenium)
    home_pg.go_to_home_page()
    assert home_pg.is_sunverge_logo_visible()


def test_navigate_to_about_us_page(selenium):
    """
    Test that you can navigate to the "ABOUT US" page through the link.
    """
    home_pg = HomePage(selenium)
    home_pg.go_to_home_page()
    about_us_pg = home_pg.go_to_about_us_page()
    about_us_pg.check_page_title()
