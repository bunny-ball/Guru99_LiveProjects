from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


import pytest
import time
import allure


def test_day1():
    with allure.step("Step 1: Go to http://live.techpanda.org/index.php/"):
    #Step 1: Go to http://live.techpanda.org/index.php/
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://live.techpanda.org/index.php')
    
    with allure.step("Step 2: Verify test \"THIS IS DEMO SITE\" shown in home page"):
    #Step 2: Verify test "THIS IS DEMO SITE" shown in home page.
        homepagetitle = driver.find_element(By.XPATH,'//h2')
        assert 'THIS IS DEMO SITE' in homepagetitle.text
    
    with allure.step("Step 3: Click on the mobile menu"):    
    #Step 3: Click on the mobile menu
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'MOBILE').click()
    
    with allure.step("Step 4: Verify title \"MOBILE\" is shown on mobile list page."):    
    #Step 4: Verify title "MOBILE" is shown on mobile list page.
        mobilepagetitle = driver.find_element(By.XPATH, '//h1')
        assert 'MOBILE' in mobilepagetitle.text
    
    with allure.step("Step 5: select \"SORT BY\" dropdown as 'name'"):
    #Step 5: select "SORT BY" dropdown as 'name'.
        select_element = driver.find_element(By.XPATH, '//select[@title=\'Sort By\']')
        select = Select(select_element)
        select.select_by_visible_text('Name')
        time.sleep(1)
        #driver.save_screenshot('mobiles are sorted.png')
        
    with allure.step("Step 6: Verify all products are sorted by name"):
    #Step 6: Verify all products are sorted by name
        items = driver.find_elements(By.XPATH, '//h2/a')
        item_name = []
        for item in items:
            item_name.append(item.text)
        assert sorted(item_name) == item_name
        #take screenshot and attach to allure report
        allure.attach(driver.get_screenshot_as_png(),name = 'mobiles are sorted', attachment_type=allure.attachment_type.PNG)
        
    