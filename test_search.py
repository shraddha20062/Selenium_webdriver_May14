import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
 #global variable and value is initialize to none
url="https://www.google.com/"
@pytest.fixture(scope="module")
def init_driver():
    global driver
    print("-------Set up ------------")
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    yield
    print("------------------tear down---------------post condition")
    driver.quit()
def test_google(init_driver):
    assert driver.title=="Google"
def test_about_click(init_driver):
    driver.find_element(By.LINK_TEXT,"About").click()
    time.sleep(2)
    assert "about" in driver.title
def test_google_search(init_driver):
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys("ice cream")
    search_box.submit()


