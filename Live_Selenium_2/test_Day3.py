import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_day3():
    url = 'http://live.techpanda.org/'
    driver = webdriver.Chrome()
    
    with allure.step("Step 1: go to homepage"):
        driver.get(url)
        time.sleep(1)
    
    with allure.step("Step 2: click on 'MOBILE' menu"):
        driver.find_element(By.LINK_TEXT, 'MOBILE').click()
        
    with allure.step("Step 3: in the list of all mobile, click on 'ADD TO CART' for Sony Xperia mobile"):
        driver.find_element(By.XPATH,'//*[@class=\'product-info\']//a[@title=\'Sony Xperia\']//ancestor::h2//following-sibling::div[@class=\'actions\']//button').click()
        time.sleep(0.5)
        
    with allure.step("Step 4: change 'QTY' value to 1000 and click 'UPDATE' button"):
        driver.find_element(By.XPATH, "//a[@title='Sony Xperia']//ancestor::td//following-sibling::td[@class='product-cart-actions']//input").send_keys('1000')
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//a[@title='Sony Xperia']//ancestor::td//following-sibling::td[@class='product-cart-actions']//button").click()
        time.sleep(0.5)
        
    with allure.step("Step 5: verify the error message"):
        # the error message is different between the test case send by mail and the actural website
        actual_errmessage=driver.find_element(By.XPATH, "//*[@class='item-msg error']").text
        expect_errmessage='* The maximum quantity allowed for purchase is 500.  '
        allure.attach(driver.get_screenshot_as_png(), name = 'error message', attachment_type=allure.attachment_type.PNG)
        assert actual_errmessage in expect_errmessage
        
    with allure.step("Step 6: click 'EMPTY CART' link in the footer of list of all mobiiles"):
        driver.find_element(By.XPATH,'//button[@title="Empty Cart"]').click()
    
    with allure.step("Step 7: verify cart is empty"):
        actual_emptymsg = driver.find_element(By.XPATH, '//h1').text
        expect_emptymsg = 'SHOPPING CART IS EMPTY'
        allure.attach(driver.get_screenshot_as_png(), name = 'empty cart', attachment_type=allure.attachment_type.PNG)
        assert actual_emptymsg in expect_emptymsg
        
if __name__ == '__main__':
    test_day3()