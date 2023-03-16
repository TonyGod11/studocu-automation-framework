from playwright.sync_api import Page, expect
import logging
import pages.application_constants as constants
from pages.utils import create_question_and_answer




class Landing_Page:
    _page_title = "The awesome Q/A tool"
    _created_questions = "Created questions"
    _sort_questions_button = "Sort questions"
    _remove_questions_button = "Remove questions"
    _create_question_button = "Create question"

    def __init__(self, page):
        self.page = page

    def navigate_to_application(self):
        self.page.goto(constants.APPLICATION_URL)

    def is_landing_page(self, page: Page):
        logging.info("Verifying Title of the page")
        page.get_by_role(constants.ROLE_HEADING, name=self._page_title).is_visible()
        logging.info("Verifying created question title in the page ")
        page.get_by_role(constants.ROLE_HEADING, name=self._created_questions).is_visible()
        logging.info("Verifying the first question is present ")
        page.get_by_text("How to add a question?Just use the form below!").is_visible()
        logging.info("Verifying the question text box is present")
        page.get_by_label("Question").is_visible()
        logging.info("Verifying the answer text box is present")
        page.get_by_label("Answer").is_visible()

    def add_question(self, page: Page):
        logging.info("Adding a new question")
        question = create_question_and_answer.generate_random_question()
        answer = create_question_and_answer.generate_random_answer()
        page.get_by_label("Question").fill(question)
        logging.info("Adding an answer")
        page.get_by_label("Answer").fill(answer)
        logging.info("Click on Create question button")
        page.get_by_role(constants.ROLE_BUTTON, name=self._create_question_button).click()
        logging.info("Verifying new question is added")
        page.get_by_text(question).click()
        expect(page.get_by_text(question)).to_be_visible()

    def remove_questions(self, page: Page):
        logging.info("Clicking on Remove questions")
        page.get_by_role(constants.ROLE_BUTTON, name=self._remove_questions_button).click()
        logging.info("Clicked on Remove questions")
        return expect(page.get_by_text("No questions yet :-(")).to_be_visible()
