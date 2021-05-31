# 1 Find locators
# Logo, use CSS: "div.a-section.a-spacing-medium.a-text-center i[class = 'a-icon a-icon-logo']"
# Create Account, use CSS class: "h1.a-spacing-small"
# Your name, use CSS ID: "#ap_customer_name"
# Email, use CSS ID: "#ap_email"
# Password, use CSS ID: "#ap_password"
# Re-Enter Password, use CSS ID: "#ap_password_check"
# Create your amazon account, use CSS ID: "#continue"
# Continue of Use, use CSS: "div#legalTextRow a[href *='ap_register_notification_condition_of_use']"
# Privacy Notice, use CSS: "div#legalTextRow a[href *='ap_register_notification_privacy_notice']"
# SIgn in , use CSS: "div.a-row a[href *= 'ap/signin?openid.pape.max_auth_age']"

#3
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path="C:/Users/trang/OneDrive - Texas State University/Automation/Github/automation_jobeasy/python-selenium-automation/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.amazon.com/")
driver.find_element(By.CSS_SELECTOR, "#nav-cart").click()

actual_ = driver.find_element(By.CSS_SELECTOR, "h2.sc-your-amazon-cart-is-empty").text

expected_ = 'Your Amazon Cart is empty'

assert expected_ == actual_, f'Expected {expected_}, but got {actual_}'
driver.quit()