from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path="C:/Users/trang/OneDrive - Texas State University/Automation/Github/automation_jobeasy/python-selenium-automation/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.amazon.com/")

search_field = driver.find_element(By.ID, "twotabsearchtextbox")
search_field.send_keys('Table')

search_icon = driver.find_element(By.ID, 'nav-search-submit-button')
search_icon.click()

actual_result = driver.find_element(By.XPATH, "//span[@class= 'a-color-state a-text-bold']").text

expected_result = '"Table"'

assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
driver.quit()
