from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

@given('Open Amazon product B08FYFW51V page')
def open_amazon_product(context):
    context.driver.get('https://www.amazon.com/dp/B08FYFW51V')

@then('Verify user can click through colors')
def verify_thru_colors(context):
    expected_colors = ['Black', 'Gray', 'Green', 'Red Wine', 'White']
    colors = context.driver.find_elements(By.CSS_SELECTOR, "#twisterContainer .imgSwatch")

    for i in range (len(colors)):
        colors[i].click()
        actual_text = context.driver.find_element(By.CSS_SELECTOR,"#variation_color_name .selection").text
        assert actual_text ==expected_colors [i], f'Error, color is {actual_text}, but expected {expected_colors}'


