"""
Test for the Sunverge "ABOUT US" page.
"""

import pytest
from TestSuite_ProofOfConcept.globals import BASE_URL

def test_open_about_us_page(selenium):
    selenium.get(BASE_URL)
