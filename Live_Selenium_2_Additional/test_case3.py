'''
 
 	
Verify Sort is working correctly

Test Steps:
1.Go to http://live.techpanda.org/index.php/backendlogin
 2.Login with credentials provided
 3.Go to Sales Invoice
 4.Sort Invoice Date Column in ascending and descending order
 5.Verify the sort is working as expected  --> Sort functionality works as expected
 
'''


import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

def capture_screen(driver, name : str):
    allure.attach(driver.get_screenshot_as_png(),name=name,attachment_type=allure.attachment_type.PNG)

def change_time_to_timestamp(data : str, timeformat):
    return time.mktime(time.strptime(data, timeformat))

def test_case3():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)

    with allure.step("Step 1: Go to http://live.techpanda.org/index.php/backendlogin"):
        driver.get("http://live.techpanda.org/index.php/backendlogin")  
    
    with allure.step("Step 2: Login the credentials provided"):
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys('user01')
        driver.find_element(By.XPATH, "//input[@id='login']").send_keys('guru99com')
        driver.find_element(By.XPATH, "//input[@title='Login']").click()
        # close Imcoming Message dialog
        driver.find_element(By.XPATH, "//a[@title='close']").click()

    with allure.step("Step 3: Go to Sales Invoice"):
        sales_menu = driver.find_element(By.XPATH, '//*[@id="nav"]/li[1]/a')
        ActionChains(driver).move_to_element(sales_menu).perform()
        orders_menu = driver.find_element(By.XPATH, "//li[@class='  last level1']")
        ActionChains(driver).move_to_element(orders_menu).click(orders_menu).perform()
        time.sleep(1)
        
    with allure.step("Step 4: Sort Invoice Date Column in descending order and verify sort is working"):
        invoice_date_desc_elements = driver.find_elements(By.XPATH, "//table[@id='sales_invoice_grid_table']//tbody//td[3]")
        date_format = '%b %d, %Y %I:%M:%S %p'
        
        actual_data_desc = []
        for element in invoice_date_desc_elements:
            # change date time to timestamp
            element_timestamp = change_time_to_timestamp(element.text, date_format)
            actual_data_desc.append(element_timestamp)
        
        expect_data_desc = actual_data_desc.copy()
        expect_data_desc.sort(reverse=True)
        assert expect_data_desc == actual_data_desc
    
    with allure.step("Step 5: Sort Invoice Date Column in ascending order and verify sort is working"):
        driver.find_element(By.XPATH, "//tr[@class='headings']//a[@name='created_at']").click()
        time.sleep(1)
        invoice_date_asc_elements = driver.find_elements(By.XPATH, "//table[@id='sales_invoice_grid_table']//tbody//td[3]")
        
        actual_data_asc = []
        for element in invoice_date_asc_elements:
            # change date time to timestamp
            element_timestamp = change_time_to_timestamp(element.text, date_format)
            actual_data_asc.append(element_timestamp)
        
        expect_data_asc = actual_data_asc.copy()
        expect_data_asc.sort()
        assert expect_data_asc == actual_data_asc    
        

if __name__ == '__main__':
    test_case3()
    