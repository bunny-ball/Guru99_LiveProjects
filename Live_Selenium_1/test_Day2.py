'''
Verify the Login Section

Test Step:
1. Go to http://www.demo.guru99.com/V4/
2. Enter valid UserId
3. Enter valid Password
4. Click Login
5. Verify the oupput

Test Data:
UserId
Password

Expected Result: 
1. Login successful
2. Verify Title of the HomePage
'''

import pytest
import allure
from Day2_info import Info
from selenium import webdriver
from selenium.webdriver.common.by import By


def login(driver,url,userId,pwd):
    with allure.step("Step 1: goto website page"):
        driver.get(url)

    with allure.step("Step 2: enter valid UserID"):
        driver.find_element(By.XPATH, "//input[@name='uid']").send_keys(userId)
        
    with allure.step("Step 3: enter valid Password"):
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)
        allure.attach(driver.get_screenshot_as_png(),name='input userid and pwd', attachment_type=allure.attachment_type.PNG)
        
    with allure.step("Step 4: click Login"):
        driver.find_element(By.XPATH,"//input[@value='LOGIN']").click()
        allure.attach(driver.get_screenshot_as_png(),name='login page',attachment_type=allure.attachment_type.PNG)
        title =  driver.title
        assert  title in ' Guru99 Bank Manager HomePage '
    driver.quit()

def test_day2():
    driver = Info().driver
    driver.maximize_window()
    driver.implicitly_wait(3)
    login(driver, Info().url, Info().userId, Info().pwd)
    
    
if __name__ == '__main__':
    pytest.main(['test_Day2.py'])
