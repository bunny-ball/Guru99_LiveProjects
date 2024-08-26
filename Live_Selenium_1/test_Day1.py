'''
Verify the Login Section

Test Step:
1. Go to http://www.demo.guru99.com/V4/
2. Enter valid UserId
3. Enter valid Password
4. Click Login

Test Data:
UserId
Password

Expected Result: Login successful
'''
import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://www.demo.guru99.com/V4/'
driver = webdriver.Chrome()

userId = 'mngr586608'
pwd = 'yqUnuje'

def test_day1():
    with allure.step("Step 1: goto website page"):
        driver.get(url)

    with allure.step("Step 2: enter valid UserID"):
        driver.find_element(By.XPATH, "//input[@name='uid']").send_keys(userId)
        
    with allure.step("Step 3: enter valid Password"):
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)
        allure.attach(driver.get_screenshot_as_png(),name='input userid and pwd', attachment_type=allure.attachment_type.PNG)
        
    with allure.step("Step 4: click Login"):
        # how to check login successful?
        driver.find_element(By.XPATH,"//input[@value='LOGIN']").click()
        allure.attach(driver.get_screenshot_as_png(),name='login page',attachment_type=allure.attachment_type.PNG)
        show_msg = driver.find_element(By.XPATH, '//tr[@class=\'heading3\']').text
        assert userId  in show_msg
    driver.quit()

if __name__ == '__main__':
    test_day1()