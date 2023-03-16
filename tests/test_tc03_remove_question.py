from pages.landing_page import Landing_Page
from playwright.sync_api import Page, expect, sync_playwright
import pytest
import re


# Test Cases for Landing Page
class TestRemoveQuestions:

    def test_add_question(self, page):
        landing_page = Landing_Page(page)
        landing_page.navigate_to_application()
        expect(page).to_have_url(re.compile(r"localhost:8000/"))
        landing_page.remove_questions(page)
