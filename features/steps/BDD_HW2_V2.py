from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given ('Open amazon help page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when ('Input Cancel order in search field')
def help_search_amazon(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order', Keys.ENTER)


@then ('Verify help search work')
def search_work_verification(context):
    actual_result1 = context.driver.find_element(By.XPATH, "//div[@class = 'help-content']//h1").text
    expected_result1 = 'Cancel Items or Orders'
    assert expected_result1 == actual_result1, f'Expected {expected_result1}, but got {actual_result1}'