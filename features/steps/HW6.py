from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

@given('Open Amazon T&C page')
def open_condition_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_window (context):
    context.original_window = context.driver.current_window_handle

@when('Click on Amazon Privacy Notice link')
def privacy_notice (context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href *= 'https://www.amazon.com/privacy']").click()

@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)

@then ('Verify Amazon Privacy Notice page is opened')
def verify_new_page_open(context):
    assert 'https://www.amazon.com/gp/help/customer' in context.driver.current_url, f'Url https://www.amazon.com/gp/help/customer not in {context.driver.current_url}'

@then('User can close new window and switch back to original')
def close_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)