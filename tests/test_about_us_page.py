"""
Tests for the Sunverge about us page.
"""

import pytest
import testfixtures

from TestSuite_ProofOfConcept.pages.about_us_page import AboutUsPage


# fixtures

@pytest.fixture
def setup_about_us_page(selenium):
    """
    Setup fixture to directly navigate to the about us page and check that it loaded correctly.
    :param selenium: pytest-selenium fixture
    :return: about_us_pg: object for the about us page
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
    expected_visibility_results = about_us_pg.expect_all_sections_visible
    visibility_results = about_us_pg.are_all_sections_visible()
    testfixtures.compare(
        expected_visibility_results, visibility_results, prefix="The following about us page sections are not visible"
    )
    #TODO: finish this test
