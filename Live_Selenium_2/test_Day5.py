'''Account Creation
Verify you can create account in E-commerce site and can share wishlist to other people using email.

Test Steps:
1. Go to http://live.techpanda.org/ 
2. Click on my account link
3. Click Create Account link and fill New User information except Email ID 
4. Click Register 
5. Verify Registration is done  --> Account Registration done
6. Go to TV menu 
7. Add product in your wish list 
8. Click SHARE WISHLIST 
9. In next page enter Email and a message and click SHARE WISHLIST 
10. Check wishlist is shared  -->  Wishlist Shared Successfully 

Test Data: 
product = LG LCD 
First Name = Test
Last Name = Tester
email = 
pwd = 
share_message = 
'''

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Data:
    def __init__(self):
        self.firstname = "Test"
        self.lastname = "Tester"
        self.email = '123333@123123123.com'
        self.pwd = '123123'
        self.url = 'http://live.techpanda.org/'
        self.message = 'share to you'
        

def verify_create_account(driver, firstname, lastname, email, pwd):
    with allure.step('Step 2: click on my account link'):
        driver.find_element(By.XPATH, "//div[@class='footer-container']//a[@title='My Account']").click()
    
    with allure.step('Step 3: click create account link and fill new user information'):
        driver.find_element(By.XPATH, "//a[@title='Create an Account']").click()
        driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys(firstname)
        driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys(lastname)        
        driver.find_element(By.XPATH, "//input[@id='email_address']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(pwd)        
        driver.find_element(By.XPATH, "//input[@id='confirmation']").send_keys(pwd)
    
    with allure.step('Step 4: click register button'):
        driver.find_element(By.XPATH, "//button[@title='Register']").click()
    
    with allure.step('Step 5: verify registration is done'):
        actual_msg = driver.find_element(By.XPATH, "//li[@class='success-msg']//span").text
        expect_msg = 'Thank you for registering with Main Website Store.'
        allure.attach(driver.get_screenshot_as_png(),name='registration',attachment_type=allure.attachment_type.PNG)
        assert actual_msg in expect_msg

def verify_share_wishlist(driver,email,message):
    with allure.step('Step 6: go to TV menu'):
        driver.find_element(By.XPATH, '//li[@class="level0 nav-2 last"]').click()
        time.sleep(1)
        
    with allure.step('Step 7: add LG LCD in wish list'):
        driver.find_element(By.XPATH, "//h2/a[@title='LG LCD']//ancestor::h2//following-sibling::div[@class='actions']//a[@class='link-wishlist']").click()
        time.sleep(1)
    
    with allure.step('Step 8: click share wishlist'):
        driver.find_element(By.XPATH, "//button[@title='Share Wishlist']").click()
        
    with allure.step('Step 9: enter email and a message and click share wishlist'):
        driver.find_element(By.XPATH, "//textarea[@id='email_address']").send_keys(email)    
        driver.find_element(By.XPATH, "//textarea[@id='message']").send_keys(message)        
        driver.find_element(By.XPATH, "//button[@title='Share Wishlist']").click()
        
    with allure.step('Step 10: verify wishlist is shared'):
        actual_msg = driver.find_element(By.XPATH, "//li[@class='success-msg']//span").text
        expect_msg = "Your Wishlist has been shared."
        allure.attach(driver.get_screenshot_as_png(),name='share wishlist',attachment_type=allure.attachment_type.PNG)

        assert actual_msg in expect_msg
    
def test_day5():
    testdata = Data()
    driver = webdriver.Chrome()
    with allure.step("Step 1: go to page"):
        
        driver.get(testdata.url)
        driver.maximize_window()
        driver.implicitly_wait(3)
    verify_create_account(driver, testdata.firstname, testdata.lastname, testdata.email, testdata.pwd)
    verify_share_wishlist(driver, testdata.email, testdata.message)
    driver.quit()
    
if __name__ == '__main__':
    pytest.main(['test_Day5.py'])
    