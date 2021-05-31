from selenium.webdriver.common.by import By
from behave import given, when, then




@when('Click on amazon cart icon')
def amazon_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#nav-cart").click()



@then('Verify amazon cart is empty')
def verify_amazon_cart(context):
    actual_ = context.driver.find_element(By.CSS_SELECTOR, "h2.sc-your-amazon-cart-is-empty").text
    expected_ = 'Your Amazon Cart is empty'
    assert expected_ == actual_, f'Expected {expected_}, but got {actual_}'
