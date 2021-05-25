# 2:
# Amazon logo, use Xpath: "//i[@class = 'a-icon a-icon-logo']"
# Continue button, search by id, "continue"
# Need help link, search by xpath: "//span[@class = 'a-expander-prompt']"
# Forgot your password link, search by id, "auth-fpp-link-bottom"
# Other issue with sign in issue, search by id, "ap-other-signin-issues-link"
# Create your amazon account, search by id, "createAccountSubmit"
# Condition link,xpath, "//div[@id = 'legalTextRow']//a[contains(@href, 'ap_signin_notification_condition_of_use')]"
# Privacy, xpath, "//div[@id = 'legalTextRow']//a[contains(@href, 'ap_signin_notification_privacy_notice')]"

# 3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path="C:/Users/trang/OneDrive - Texas State University/Automation/Github/automation_jobeasy/python-selenium-automation/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.amazon.com/gp/help/customer/display.html')

search_field = driver.find_element(By.ID, 'helpsearch')
search_field.send_keys("Cancel order")
search_field.send_keys(Keys.ENTER)
actual_result = driver.find_element(By.XPATH, "//div[@class = 'help-content']//h1['Cancel Items or Orders']").text

expected_result = 'Cancel Items or Orders'

assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'

driver.quit()



