from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click Amazon Orders link')
def click_orders_icon(context):
    context.app.header.click_orders_icon()

@then('Verify Sign In page  is opened')
def verify_SignIn_page(context):
    context.app.sign_in.verify_sign_in("Sign-In")