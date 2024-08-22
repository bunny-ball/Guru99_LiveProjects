'''
Verify that cost of product in list page and details page are equal.

Test Steps:
1. Goto http://live.techpanda.org/ 
2. Click on 'MOBILE' menu.
3. In the list of all mobile , read the cost of Sony Xperia mobile). Note this value 
4. Click on Sony Xperia mobile.
5. Read the Sony Xperia mobile from detail page. 
6. Compare value in Step 3 & Step 5. --> Product Value in list and details page should be equal ($100) 
'''
import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_day2():
    url = 'http://live.techpanda.org/'
    driver = webdriver.Chrome()
    driver.maximize_window()
    with allure.step("Step 1: Goto http://live.techpanda.org"):
        driver.get(url)
        
    with allure.step("Step 2: click on 'MOBILE' menu"):
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'MOBILE').click()
        time.sleep(1)
        
    with allure.step("Step 3: read and note the cost of Sony Xperia mobile"):
        price1 = driver.find_element(By.XPATH, '//span[@id="product-price-1"]').text
        allure.attach(driver.get_screenshot_as_png(),name = 'price in step3', attachment_type=allure.attachment_type.PNG)
        
        
    with allure.step('Step 4: click on Sony Xperia mobile'):
        driver.find_element(By.LINK_TEXT, "SONY XPERIA").click()
        time.sleep(1)
    
    with allure.step('Step 5: read the Sony Xperia mobile from detail page'):
        price2 = driver.find_element(By.XPATH, '//span[@id="product-price-1"]').text
        allure.attach(driver.get_screenshot_as_png(),name = 'price in step5', attachment_type=allure.attachment_type.PNG)
        
    with allure.step("Step6: compare value in step 3 and step 5"):
        assert price1 == price2
    driver.quit()
if __name__ == '__main__':
    test_day2()