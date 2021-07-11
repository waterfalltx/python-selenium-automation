from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SEARCH_FIELD = (By.ID, "twotabsearchtextbox")
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS_ICON = (By.CSS_SELECTOR, "#nav-tools #nav-orders .nav-line-2 ")
    CART_ICON = (By.CSS_SELECTOR, "#nav-cart-count-container .nav-cart-icon.nav-sprite ")
    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders_icon(self):
        self.click(*self.ORDERS_ICON)

    def click_cart_icon (self):
        self.click(*self.CART_ICON)
