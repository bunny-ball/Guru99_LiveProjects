import pytest
import allure
from Day2_info import Info
from selenium import webdriver
from selenium.webdriver.common.by import By
import time   

def login(driver,url,userId,pwd):
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
        show_msg =  driver.find_element(By.XPATH, '//tr[@class=\'heading3\']').text
        assert  Info().userId  in show_msg
    #driver.quit()

def test_day2():
    driver = Info().driver
    driver.maximize_window()
    driver.implicitly_wait(3)
    login(driver, Info().url, Info().userId, Info().pwd)
    
    
if __name__ == '__main__':
    pytest.main(['test_Day2.py'])
    # test_day1(init_chrome)