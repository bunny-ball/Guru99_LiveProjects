import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestData():
    def __init__(self):
        self.firstname = "Test"
        self.lastname = "Tester"
        self.email = ''
        self.pwd = ''
        self.url = 'http://live.techpanda.org/'
        self.message = 'share to you'
        

def verify_create_account(driver, firstname, lastname, email, pwd):
    driver.find_element(By.XPATH, "//div[@class='footer-container']//a[@title='My Account']").click()
    
    driver.find_element(By.XPATH, "//a[@title='Create an Account']").click()
    
    driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys(firstname)
    
    driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys(lastname)
    
    driver.find_element(By.XPATH, "//input[@id='email_address']").send_keys(email)

    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(pwd)
    
    driver.find_element(By.XPATH, "//input[@id='confirmation']").send_keys(pwd)
    
    driver.find_element(By.XPATH, "//button[@title='Register']").click()
    
    actual_msg = driver.find_element(By.XPATH, "//li[@class='success-msg']//span").text
    expect_msg = 'Thank you for registering with Main Website Store.'
    assert actual_msg in expect_msg

def verify_share_wishlist(driver,email,message):
    driver.find_element(By.XPATH, '//li[@class="level0 nav-1 first"]').click()

    driver.find_element(By.XPATH, "//h2/a[@title='LG LCD']//ancestor::h2//following-sibling::div[@class='actions']//a[@class='link-wishlist']").click()
    
    driver.find_element(By.XPATH, "//button[@title='Share Wishlist']").click()
    
    driver.find_element(By.XPATH, "//textarea[@id='email_address']").send_keys(email)
    
    driver.find_element(By.XPATH, "//textarea[@id='message']").send_keys(message)
    
    driver.find_element(By.XPATH, "//button[@title='Share Wishlist']").click()
    
    actual_msg = driver.find_element(By.XPATH, "//li[@class='success-msg']//span").text
    expect_msg = "Your Wishlist has been shared."
    assert actual_msg in expect_msg
    
def test_day5():
    testdata = TestData()
    driver = webdriver.Chrome()
    driver.get(testdata.url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    verify_create_account(driver, testdata.firstname, testdata.lastname, testdata.email, testdata.pwd)
    verify_share_wishlist(driver, testdata.email, testdata.message)
    
if __name__ == '__main__':
    test_day5()
    