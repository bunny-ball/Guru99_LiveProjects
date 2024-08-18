'''handling popup windows'''

import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_day4():
    
    url = 'http://live.techpanda.org/'
    driver = webdriver.Chrome()
    phone1 = 'Sony Xperia'
    phone2 = 'IPhone'
    driver.maximize_window()
    
    
    with allure.step("Step 1: goto live.techpanda.org"):
        driver.get(url)
        time.sleep(0.5)
        
    with allure.step("Step 2: click on MOBILE menu"):
        driver.find_element(By.LINK_TEXT, 'MOBILE').click()
        time.sleep(1)
        
    with allure.step("Step 3: click ADD TO COMPARE for Sony Xperia and Iphone"):
        phone1XPATH = '//h2[@class="product-name"]/a[@title="' + phone1 + '"]//ancestor::h2//following-sibling::div[@class="actions"]//a[@class="link-compare"]'
        driver.find_element(By.XPATH,phone1XPATH).click()
        time.sleep(0.3)
        phone2XPATH = '//h2[@class="product-name"]/a[@title="' + phone2 + '"]//ancestor::h2//following-sibling::div[@class="actions"]//a[@class="link-compare"]'
        driver.find_element(By.XPATH,phone2XPATH).click()
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(),name='add to compare',attachment_type=allure.attachment_type.PNG)
    
    with allure.step("Step 4: click on COMPARE button"):
        driver.find_element(By.XPATH, '//button[@title="Compare"]').click()
        time.sleep(1)
        
        
    with allure.step("Step 5: verify the pop-up window and check the products are reflected in it"):
        all_windows = driver.window_handles
        # verify a new window popup
        assert len(all_windows) == 2 
        # change to a new window
        for window in all_windows:
            if window != driver.current_window_handle:
                driver.switch_to.window(window)
                break
        allure.attach(driver.get_screenshot_as_png(),name='compare window',attachment_type=allure.attachment_type.PNG)
        # verify popup window content
        expect_window_title = 'compare products'
        actual_new_window_title = str(driver.find_element(By.XPATH, '//h1').text).lower()
        assert actual_new_window_title == expect_window_title
        
        phone1_new_window = driver.find_element(By.XPATH, "//h2[@class='product-name']/a[@title='Sony Xperia']").text
        assert phone1_new_window.lower() == phone1.lower()
        phone2_new_window = driver.find_element(By.XPATH, "//h2[@class='product-name']/a[@title='IPhone']").text
        assert phone2_new_window.lower() == phone2.lower()    
    
    
    with allure.step("Step 6: close the popup window"):
        driver.find_element(By.XPATH, "//button[@title='Close Window']").click()
        #driver.close()
        # verify the popup window closed and remain only one window
        assert len(driver.window_handles)==1
        
if __name__ == '__main__':
    test_day4()