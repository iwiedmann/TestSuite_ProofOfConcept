"""
Test for the Sunverge "ABOUT US" page.
"""

import pytest

from TestSuite_ProofOfConcept.pages.about_us_page import AboutUsPage


# fixtures

@pytest.fixture
def setup_about_us_page(selenium):
    """
    Setup fixture to directly navigate to the "ABOUT US" page.
    :return: about_us_pg: object for the "ABOUT US" page
    """
    about_us_pg = AboutUsPage(selenium)
    about_us_pg.go_to_about_us_page()
    return about_us_pg


# tests

def test_sub_menu_navigation_bar(setup_about_us_page):
    """
    Parameterized test to test all the links in the green sub menu navigation bar.  Each link is clicked and then it is
    checked that all the sections are still visible.
    TODO: A better test might check that the page scrolled to the correct section after clicking each link; however,
    this test could be fragile.
    """
    about_us_pg = setup_about_us_page
    visibility_results = about_us_pg.are_all_sections_visible()
    for locator_name, is_visible in visibility_results.iteritems():
        assert is_visible, "{locator} is not visible".format(locator=locator_name)
    #TODO: finish this test
