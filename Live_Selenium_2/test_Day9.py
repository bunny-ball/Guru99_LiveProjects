'''Discount Coupon
Verify Discout Coupon works correctly

Test Steps:
1.Go to http://live.techpanda.org/ 
2.Go to Mobile and add IPHONE to cart 
3.Enter Coupon Code  
4. Verify the discount generated. --> Price is discounted by 5% 
***after applying the discount code, the grand total price is incorrect***

Test Data:
Coupon Code: GURU50 

'''

import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def capture_screen(driver, name : str):
    allure.attach(driver.get_screenshot_as_png(),name=name,attachment_type=allure.attachment_type.PNG)

def test_day9():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    url = 'http://live.techpanda.org/'
    with allure.step("Step 1: Go to http://live.techpanda.org/"):
        driver.get(url)
    with allure.step("Step 2: Go to Mobile and add IPHONE to cart "):
        driver.find_element(By.XPATH, "//a[contains(text(),'Mobile')]").click()

        driver.find_element(By.XPATH, "//h2[@class='product-name']//a[@title='IPhone']//ancestor::h2//following-sibling::div[@class='actions']//button").click()
        time.sleep(1)
    with allure.step("Step 3: Enter Coupon Code"):
        capture_screen(driver, 'before applying coupon')
        init_price = float(driver.find_element(By.XPATH, "//strong//span[@class='price']").text[1:])

        coupon_code = 'GURU50'

        driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys(coupon_code)
        driver.find_element(By.XPATH, "//button[@title='Apply']").click()
        time.sleep(0.5)
    with allure.step("Step 4: Verify the discount generated"):
        capture_screen(driver, "after applying coupon")
        discount_amount = float(driver.find_element(By.XPATH, "//table[@id='shopping-cart-totals-table']//*[contains(text(),'Discount')]//following-sibling::td").text[2:])
        assert init_price * 0.05 == discount_amount
        after_grand_total = float(driver.find_element(By.XPATH, "//strong//span[@class='price']").text[1:])
        assert after_grand_total == init_price - discount_amount
    driver.quit()
if __name__ =='__main__':
    pytest.main(['test_Day9.py'])