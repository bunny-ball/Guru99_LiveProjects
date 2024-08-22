'''Re-order
Verify you are able to change or reorder previously added product 

Test Steps:
1.Go to http://live.techpanda.org/
2.Click on my account link 
3.Login in application using previously created credential 
4.Click on 'REORDER' link, change QTY & click Update 
5. Verify Grand Total is changed  --> Grand Total is Changed 
6. Complete Billing & Shipping Information 
7. Verify order is generated and note the order number --> Order number is generated 

Test Data:
QTY = 10 
password and email are generated previously (test_Day6.py)
'''

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from test_Day5 import Data



def capture_screen(driver, name : str):
    allure.attach(driver.get_screenshot_as_png(),name=name,attachment_type=allure.attachment_type.PNG)
    
def test_day8():
    driver = webdriver.Chrome()
    driver.maximize_window
    driver.implicitly_wait(3)
    with allure.step("Step 1: Go to http://live.techpanda.org/"):
        driver.get(Data().url)
    
    with allure.step("Step 2: Click on My Account link "):
        driver.find_element(By.XPATH, "//div[@class='footer']//a[@title='My Account']").click()
    
    with allure.step("Step 3: Login in application using previously created credential"):
        driver.find_element(By.XPATH, "//input[@title = 'Email Address']").send_keys(Data().email)
        driver.find_element(By.XPATH, "//input[@title = 'Password']").send_keys(Data().pwd)
        driver.find_element(By.XPATH, "//button[@title= 'Login']").click()
    
    with allure.step("Step 4: Click on 'REORDER' link, change QTY & click Update'"):
        driver.find_element(By.XPATH, "//a[contains(text(),'Reorder')]").click()
        init_price = float(driver.find_element(By.XPATH, "//strong//span[@class='price']").text[1:].replace(',',''))
        capture_screen(driver, 'before updating qty')
        qty = 10
        driver.find_element(By.XPATH, "//input[@title='Qty']").clear()
        driver.find_element(By.XPATH, "//input[@title='Qty']").send_keys(qty)
        driver.find_element(By.XPATH, "//button[@title='Update']").click()
        capture_screen(driver, 'after udpating qty')
        updated_price = float(driver.find_element(By.XPATH, "//strong//span[@class='price']").text[1:].replace(',',''))
        assert updated_price == init_price * qty
    
    with allure.step("Step 5: Click Proceed to CheckOut and Complete Billing & Shipping Information"):
        driver.find_element(By.XPATH, "//div[@class='cart-totals-wrapper']//button").click()
        driver.find_element(By.XPATH, "//div[@id='billing-buttons-container']/button[@title='Continue']").click()
        driver.find_element(By.XPATH, "//div[@id='shipping-method-buttons-container']//button").click()
        driver.find_element(By.XPATH, "//input[@value = 'checkmo']").click()
        driver.find_element(By.XPATH, "//div[@id='payment-buttons-container']//button").click()
   
    with allure.step("Step 6: place order and verify order is generated and note the order number"):
        driver.find_element(By.XPATH, "//button[@title= 'Place Order']").click()
        time.sleep(2)
        capture_screen(driver, 'order placed')
        expect_order_suc = 'your order has been received.'
        actual_order_suc = driver.find_element(By.XPATH, "//h1").text.lower()
        assert actual_order_suc == expect_order_suc
        order_no = driver.find_element(By.XPATH, "//*[contains(text(), 'Your order #')]//a").text
        assert order_no is not None

    driver.quit()


   