from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignIn(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, "div.a-box-inner.a-padding-extra-large h1.a-spacing-small")

    def verify_sign_in(self, expected_text):

        self.verify_text(expected_text, *self.SIGN_IN_TEXT)