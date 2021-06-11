from selenium.webdriver.common.by import By
from behave import given, when, then

@given ('Open Amazon Bestsellers page')
def open_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@when('Verify {links_count} links are displayed')
def verify_links(context, links_count):
    link_count = context.driver.find_elements(By.CSS_SELECTOR, "div#zg_tabs a")
    print('\n Count_number:', len(link_count))
    assert len(link_count) == int(links_count), f'Expected {links_count}, but got {len(link_count)}'
