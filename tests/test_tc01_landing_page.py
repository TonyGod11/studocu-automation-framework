from pages.landing_page import Landing_Page
from playwright.sync_api import Page, expect
import re


# Test Cases for Landing Page
class TestLandingPage:

    def test_landing_page(self, page):
        landing_page = Landing_Page(page)
        landing_page.navigate_to_application()
        expect(page).to_have_url(re.compile(r"localhost:8000/"))
        landing_page.is_landing_page(page)
