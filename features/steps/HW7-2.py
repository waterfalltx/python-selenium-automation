from selenium.webdriver.common.by import By
from behave import given, when, then

@when ('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()

@then("Verify 'Your Amazon Cart is empty.' text present")
def verify_text_in_cart_present(context):
    context.app.search_results_page.verify_text_present('Your Amazon Cart is empty')