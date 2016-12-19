"""
Test for the Sunverge "ABOUT US" page.
"""

import pytest
#import globals

def test_open_about_us_page(selenium):
    selenium.get("http://www.sunverge.com/")
