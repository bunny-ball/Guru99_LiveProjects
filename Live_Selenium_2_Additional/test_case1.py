'''
Verify invoice can be printed

Test Steps: 
1.Go to http://live.techpanda.org/index.php/backendlogin
2.Login the credentials provided
3.Go to Sales-> Orders menu
4.In the status field select "Canceled". Click Search
5.Select the checkbox next to first order
6.In Actions, select "Print Invoices". Click Submit
7.Verify the error message --> Error message "There are no printable documents related to selected orders" is shown
8.In the status field select "Complete". Click Search
9.Select the checkbox next to first order
10.In Actions, select "Print Invoices". Click Submit
11. Verify invoice is downloaded  --> Invoice is downloaded
 

Test Data: 
id = "user01"
pass = "guru99com"

'''

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import os
import tempfile
import glob
import fnmatch

def test_case1():
    
    temp_download_dir = tempfile.mkdtemp() # set the temp download directory folder
    
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": temp_download_dir  # set the Chrome download dir to temp folder
    })
    driver = webdriver.Chrome(options=chrome_options)
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

    with allure.step("Step 3: Go to Sales"):
        sales_menu = driver.find_element(By.XPATH, '//*[@id="nav"]/li[1]/a')
        ActionChains(driver).move_to_element(sales_menu).perform()
        orders_menu = driver.find_element(By.XPATH, "//li[@class='  level1']")
        ActionChains(driver).move_to_element(orders_menu).click(orders_menu).perform()
        time.sleep(1)

    with allure.step("Step 4: In the status field select 'Canceled'. Click Search"):
        select_status = driver.find_element(By.XPATH, '//*[@id="sales_order_grid_filter_status"]')
        select = Select(select_status)
        select.select_by_visible_text('Canceled')
        search_button = driver.find_element(By.XPATH, "//button[@title='Search']")
        ActionChains(driver).click(search_button).perform()
        time.sleep(2)
        
    with allure.step("Step 5: Select the checkbox next to first order"):
        driver.find_element(By.XPATH, "//input[@name='order_ids']").click()
        time.sleep(1)
        
    with allure.step("Step 6: In Actions, select 'Print Invoices'. Click Submit"):
        select_actions = driver.find_element(By.XPATH, "//select[@id='sales_order_grid_massaction-select']")
        Select(select_actions).select_by_visible_text("Print Invoices")
        driver.find_element(By.XPATH, "//button[@title='Submit']").click()
        time.sleep(1)
        
    with allure.step("Step 7:Verify the error message"):
        expect_err_msg = "There are no printable documents related to selected orders."
        actual_err_msg = driver.find_element(By.XPATH, "//li[@class='error-msg']").text
        assert expect_err_msg == actual_err_msg
        time.sleep(2)
        
    with allure.step("Step 8: In the status field select 'Complete'. Click Search"):
        select_status1 = driver.find_element(By.XPATH, '//*[@id="sales_order_grid_filter_status"]')
        Select(select_status1).select_by_visible_text('Complete')
        driver.find_element(By.XPATH, "//button[@title='Search']").click()
        time.sleep(2)
    
    with allure.step("Step 9: Select the checkbox next to first order"):
        driver.find_element(By.XPATH, "//input[@name='order_ids']").click()
        time.sleep(2)
        
    with allure.step("Step 10: In Actions, select 'Print Invoices'. Click Submit"):
        select_actions1 = driver.find_element(By.XPATH, "//select[@id='sales_order_grid_massaction-select']")
        Select(select_actions1).select_by_visible_text("Print Invoices")             
        driver.find_element(By.XPATH, "//button[@title='Submit']").click()
        time.sleep(3)
        
    with allure.step("Step 11: Verify invoice is downloaded"):
    # print(os.listdir(temp_download_dir))
    # Method 1: use fnmatch to check the download file name contains the key string in the temp dir 
    #           download folder
        for file in os.listdir(temp_download_dir):
            assert fnmatch.fnmatch(file, "invoice*.*")

                
    # Method 2: use glob to find and use os.rename to rename the latest download file to a specified filename,
    #           then verify the specified file exist
            
    # path_a = temp_download_dir + "/*"
    # list_of_files = glob.glob(path_a)
    # lastest_file = max(list_of_files, key = os.path.getctime)
    # new_file = os.path.join(temp_download_dir, "test.pdf")
    # print(lastest_file)
    # os.rename(lastest_file, new_file)
    # print(os.listdir(temp_download_dir))
    
    # assert "test.pdf" in os.listdir(temp_download_dir)
    
    driver.quit()
    
    
    
if __name__ =='__main__':
    test_case1()