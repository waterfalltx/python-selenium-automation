from pages.header import Header
from pages.main_page import Main
from pages.search_results_page import SearchResults
from pages.sign_in import SignIn


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = Main(self.driver)
        self.header = Header(self.driver)
        self.search_results_page= SearchResults(self.driver)
        self.sign_in = SignIn(self.driver)
