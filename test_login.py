import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import openpyxl
#Utility to read excel data
def read_credentials_from_excel(file_path):
    workbook=openpyxl.load_workbook(file_path)
    sheet=workbook.active
    credentials=[]
    for row in sheet.iter_rows(min_row=2, values_only=True): #skip header
        credentials.append((row[0], row[1]))
    return credentials
# pytest function with parameterization
@pytest.mark.parametrize("username,password", read_credentials_from_excel("F:\\SeleniumPython\\python.xlsx"))
def test_orangehrm_login(username,password):

    #step 1 open chrom browser
    driver=webdriver.Chrome()
    #step 2 get web url
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    #driver.set_page_load_timeout(10)
    #driver.implicitly_wait(10)
    time.sleep(5)
    try:
        #time.sleep(10)
        #step 3 input username and password
        driver.find_element(By.NAME,"username").send_keys(username)
       # time.sleep(5)
        driver.find_element(By.NAME,"password").send_keys(password)
        time.sleep(5)
        #step 4 click on login button
        driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        time.sleep(10)

        if username=="Admin" and password=="admin123":
            #except successful login check of url have "dashboard" text
            #
            assert "dashboard" in driver.current_url.lower(), f" login failed for {username}"
            print(f" [Success] logged in as {username}")
        else:
            #except error message for wrong credentials
            error=driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

            assert error.is_displayed(),"error msg not displayed for wrong credentials"
            print(f"[Failed] expected failure for {username} got {error.text}")
    finally:

        #quit browser
        driver.quit()