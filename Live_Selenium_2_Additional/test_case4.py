'''
 
 	
Verify Search Functionality

Test Steps:
 
 	
1. Go to http://live.techpanda.org/index.php/
2. Click on Advance Search
3. In Price field enter range 0-150. Click Search
4. Note the Price and Product Name in the result. Print on console  --> Product names & price are fetched
5. Again, In Price field enter range 151-1000. Click Search
6. Note the Price and Product Name in the result. Print on console  --> Product names & price are fetched
 
'''

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_case4():
    driver = webdriver.Chrome()
    driver.maximize_window
    driver.implicitly_wait(3)
    with allure.step("Step 1: Go to http://live.techpanda.org/index.php/"):
        driver.get("http://live.techpanda.org/index.php/")

    with allure.step("Step 2: Click on Advance Search"):
        driver.find_element(By.XPATH,"//a[@title='Advanced Search']").click()

    with allure.step("Step 3: In Price field enter range 0-150. Click Search"):
        driver.find_element(By.XPATH, "//input[@name='price[from]']").send_keys('0')
        driver.find_element(By.XPATH, "//input[@name='price[to]']").send_keys('150')
        driver.find_element(By.XPATH, "//div[@class='buttons-set']//button[@title='Search']").click()

    with allure.step("Step 4: Note the Price and Product Name in the result. Print on console"):
        products_prices_150 = driver.find_elements(By.XPATH, "//h2[@class='product-name'] | //div[@class='product-info']//p[@class='special-price']//span[@class='price'] | //div[@class='product-info']//span[@class='regular-price']//span")
        print("The product names and prices between $0 - $150:")   
        for i in products_prices_150:
            print(i.text)
     
    with allure.step("Step 5: Again, In Price field enter range 151-1000. Click Search") :
        driver.find_element(By.LINK_TEXT, "Modify your search").click()
        
        driver.find_element(By.XPATH, "//input[@name='price[from]']").clear()
        driver.find_element(By.XPATH, "//input[@name='price[from]']").send_keys('151')
        driver.find_element(By.XPATH, "//input[@name='price[to]']").clear()
        driver.find_element(By.XPATH, "//input[@name='price[to]']").send_keys('1000')
        driver.find_element(By.XPATH, "//div[@class='buttons-set']//button[@title='Search']").click()
    
    with allure.step("Step 6: Note the Price and Product Name in the result. Print on console"):
        products_prices_1000 = driver.find_elements(By.XPATH, "//h2[@class='product-name'] | //div[@class='product-info']//p[@class='special-price']//span[@class='price'] | //div[@class='product-info']//span[@class='regular-price']//span")
        print("The product names and prices between $151 - $1000:")
        for i in products_prices_1000:
            print(i.text)
     
if __name__ == '__main__':
    pytest.main(['test_case4.py'])