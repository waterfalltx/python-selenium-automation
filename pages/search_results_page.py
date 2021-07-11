from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class = 'a-color-state a-text-bold']")
    TEXT_RESULT = (By.CSS_SELECTOR, "h2")

    def verify_search_worked(self, expected_text):
        # actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
        # expected_result = '"Table"'
        # assert expected_result == actual_result, f'Expected{expected_result}, but got {actual_result}'
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_text_present(self, expected_text):
        self.verify_text(expected_text, *self.TEXT_RESULT)