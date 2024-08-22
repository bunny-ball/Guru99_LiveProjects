'''PDF
Verify that you will be able to save previously placed order as a pdf file

Test Steps:
1. Go to http://llive.techpanda.org/ 
2. Click on My Account link 
3. Login in application using previously created credential 
4. Click on 'My Orders' 
***steps 5/6 provided by Guru99 need to be switched - the orders table and status are showing in the My Order page***
5. Click on 'View Order' 
6. Verify the previously created order is displayed in 'RECENT ORDERS' table and status is Pending 
7. Click on 'Print Order' link (Note: This will open up the Print dialog for chrome, and afterwards 
                                will open up a system dialog, selenium could not interact with it, so use
                                pyautogui to control the system dialog)
8. Verify Order is saved as PDF 

Test Data:
password, email, Order No are generated previously (test_Day6.py)
'''
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from test_Day5 import Data
import time

def capture_screen(driver, name : str):
    allure.attach(driver.get_screenshot_as_png(),name=name,attachment_type=allure.attachment_type.PNG)
    

def test_day7(): 
    driver_op = webdriver.ChromeOptions()
    driver_op.add_argument("--start-maximized") # same as driver.maximize_window
    driver_op.add_argument("--disable-print-proview")
    driver = webdriver.Chrome(options=driver_op)

    #driver.maximize_window
    driver.implicitly_wait(3)
    with allure.step("Step 1: Go to http://llive.techpanda.org/ "): 
        driver.get(Data().url)
    check_order(driver)
    print_order(driver)
    driver.quit()
    
def check_order(driver):
    with allure.step("Step 2: Click on My Account link "):
        driver.find_element(By.XPATH, "//div[@class='footer']//a[@title='My Account']").click()
    with allure.step("Step 3: Login in application using previously created credential"):
        driver.find_element(By.XPATH, "//input[@title = 'Email Address']").send_keys(Data().email)
        driver.find_element(By.XPATH, "//input[@title = 'Password']").send_keys(Data().pwd)
        driver.find_element(By.XPATH, "//button[@title= 'Login']").click()
        
    with allure.step("Step 4: Click on 'My Orders'"):
        driver.find_element(By.XPATH, "//div[@class='block block-account']//*[contains(text(),'My Orders')]").click()
   
    with allure.step("Step 5: Verify the previously created order is displayed in 'RECENT ORDERS' table and status is Pending"):
        capture_screen(driver, 'recent order')
        acutal_status = driver.find_element(By.XPATH, "//td[@class='status']").text.lower()
        expect_status = 'pending'
        assert acutal_status == expect_status
        actual_order_no = acutal_status = driver.find_element(By.XPATH, "//td[@class='number']").text
        expect_order_no = ''
        assert expect_order_no in actual_order_no

    with allure.step("Step 6: Click on 'View Order'"):
        driver.find_element(By.XPATH, "//a[contains(text(),'View Order')]").click()
        time.sleep(0.2)
        capture_screen(driver, 'view order')
        
def print_order(driver):
    with allure.step("Step 7: Click on 'Print Order' link"):
        driver.find_element(By.XPATH, "//a[@class='link-print']").click()
        time.sleep(1)
        # system diaglog popup
        pyautogui.press('enter')
        time.sleep(1)
        
        file_name = 'test_' + str(int(time.time()*1000))
        pyautogui.write(file_name)
        time.sleep(0.5)

        pyautogui.press('enter')
        time.sleep(4)
           
if __name__ == '__main__':
    pytest.main(['test_Day7.py'])