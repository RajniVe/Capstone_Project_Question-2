# checkbox_helper.py
from selenium.webdriver.common.by import By

def is_checkbox_checked(browser, checkbox_index):
    checkbox = browser.find_element(By.XPATH, f"//input[@type='checkbox'][{checkbox_index}]")
    return checkbox.is_selected()
