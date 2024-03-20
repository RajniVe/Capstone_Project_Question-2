import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from checkbox_helper import is_checkbox_checked

@pytest.fixture(scope="module")
def browser():
    # Setup
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()

def test_verify_homepage_title(browser):
    browser.get("http://the-internet.herokuapp.com/")
    assert "The Internet" in browser.title

def test_verify_checkboxes_page(browser):
    browser.find_element(By.LINK_TEXT, "Checkboxes").click()
    assert "Checkboxes" in browser.find_element(By.TAG_NAME, "h3").text

def test_verify_checkboxes_state(browser):
    assert not is_checkbox_checked(browser, 1)
    assert is_checkbox_checked(browser, 2)

def test_verify_file_upload_page(browser):
    browser.find_element(By.LINK_TEXT, "Home").click()
    browser.find_element(By.LINK_TEXT, "File Upload").click()
    assert "File Uploader" in browser.find_element(By.TAG_NAME, "h3").text

def test_file_upload(browser):
    browser.find_element(By.ID, "file-upload").send_keys("C:\file.txt")
    browser.find_element(By.ID, "file-submit").click()
