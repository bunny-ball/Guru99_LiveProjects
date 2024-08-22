'''Purchase Products
Verify user is able to purchase product using registered email id

Test Steps: 
1.Go to http://live.techpanda.org/ 
2.Click on my account link 
3.Login in application using previously created credential 
4.Click on MY WISHLIST link 
5.In next page, Click ADD TO CART link 
6.Click PROCEED TO CHECKOUT 2) Shipping 
7. Enter Shipping Information Information 
8. Click Estimate  
9. Verify Shipping cost generated  --> Flat Rate Shipping of S5 is generated 
10. Select Shipping Cost
***These steps provided by Guru99 DO NOT match up with the website***
11. Verify shipping cost is added to total  --> Shipping cost is added to total product cost
12. Click "Proceed to Checkout'
13. Enter Billing Information 
14. In Shipping Method, Click Continue  
15. In Payment Information select the 'Check/Money Order' radio button. Click Continue 
16.Click 'PLACE ORDER' button  --> Oder is placed. Order number is generated


Test Data:
email = 
pwd =  
(Created in Day5.py)
Shipping Information: 
Country = United States
State = New York
Zip = 542896 
Address = ABC
City = New York
Telephone = 12345678
'''
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from test_Day5 import Data

class Ship_info:
    def __init__(self):
        self.country = 'United States'
        self.state = 'New York'
        self.zip = '542896'
        self.address = 'ABC'
        self.city = 'New York'
        self.tel = '12345678'

def check_out(driver):
    with allure.step("Step 2: click my account link"):
        driver.find_element(By.XPATH, "//div[@class='footer-container']//a[@title='My Account']").click()
    
    with allure.step("Step 3: login in using previously created credential"):
        driver.find_element(By.XPATH, "//input[@title='Email Address']").send_keys(Data().email)
        driver.find_element(By.XPATH, "//input[@title='Password']").send_keys(Data().pwd)
        driver.find_element(By.XPATH, "//button[@title='Login']").click()
    
    with allure.step("Step 4: click on my wishlist link"):
        driver.find_element(By.XPATH, "//div[@class='block-content']//a[text()='My Wishlist']").click()
        allure.attach(driver.get_screenshot_as_png(),name='wishlist',attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 5: click add to cart link"):
        driver.find_element(By.XPATH, "//button[@title='Add to Cart']").click()
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(),name='add to cart',attachment_type=allure.attachment_type.PNG)

   
    with allure.step("Step 6: click proceed to checkout"):
        driver.find_element(By.XPATH, "//ul[@class='checkout-types top']//button[@title='Proceed to Checkout']").click()
        time.sleep(0.5)
        allure.attach(driver.get_screenshot_as_png(),name='checkout',attachment_type=allure.attachment_type.PNG)

def place_order(driver):
    # Billing Information
    with allure.step("Step 7: enter billing information"):
        driver.find_element(By.XPATH, "//div[@id='checkout-step-billing']//input[@title='Street Address']").send_keys(Ship_info().address)
        driver.find_element(By.XPATH, "//div[@id='checkout-step-billing']//input[@title='City']").send_keys(Ship_info().city)
        select_state = Select(driver.find_element(By.XPATH, "//div[@id='checkout-step-billing']//select[@title='State/Province']"))
        select_state.select_by_value("43")
        driver.find_element(By.XPATH, "//div[@id='checkout-step-billing']//input[@title='Zip']").send_keys(Ship_info().zip)
        select_state = Select(driver.find_element(By.XPATH, "//div[@id='checkout-step-billing']//select[@title='Country']"))
        select_state.select_by_visible_text("United States")
        driver.find_element(By.XPATH, "//div[@id='checkout-step-billing']//input[@title='Telephone']").send_keys(Ship_info().tel)
        driver.find_element(By.XPATH, "//div[@id='billing-buttons-container']//button").click()
        
    # Shipping Information
    #driver.find_element(By.XPATH, "//div[@id='shipping-buttons-container']//button").click()
    # Shipping Method
    with allure.step("Step 8: verify shipping cost generated, click continue"):
        actual_flat_rate_ship_price = driver.find_element(By.XPATH, "//div[@id='checkout-step-shipping_method']//span[@class='price']").text
        driver.find_element(By.XPATH, "//div[@id='shipping-method-buttons-container']//button").click()
        allure.attach(driver.get_screenshot_as_png(),name='shipping cost generated',attachment_type=allure.attachment_type.PNG)
        assert '$5' == actual_flat_rate_ship_price[0:2]


    # Payment Information
    with allure.step("Step 9: select check/money order, click continue"):
        driver.find_element(By.XPATH, "//input[@id='p_method_checkmo']").click()
        driver.find_element(By.XPATH, "//div[@id='payment-buttons-container']//button").click()

    # Order Review
    with allure.step("Step 10: verify shippihng coast is added to total cost"):
        actual_subtotal = driver.find_element(By.XPATH, "//td[contains(text(),'Subtotal')]//following-sibling::td/span").text
        actual_shipping_fee = driver.find_element(By.XPATH, "//td[contains(text(),'Shipping & Handling (Flat Rate - Fixed)')]//following-sibling::td/span").text
        actual_grand_total = driver.find_element(By.XPATH, "//strong[contains(text(),'Grand Total')]//ancestor::td//following-sibling::td//span").text
        allure.attach(driver.get_screenshot_as_png(),name='review order',attachment_type=allure.attachment_type.PNG)
        assert actual_shipping_fee == actual_flat_rate_ship_price
        assert float(actual_subtotal[1:]) + float(actual_shipping_fee[1:]) == float(actual_grand_total[1:])
   
    with allure.step("Step 11: click place order"):
        driver.find_element(By.XPATH, "//button[@title='Place Order']").click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),name='place order',attachment_type=allure.attachment_type.PNG)


    with allure.step("Step 12: verify order is generated."):
        allure.attach(driver.get_screenshot_as_png(),name='order placed',attachment_type=allure.attachment_type.PNG)
        expect_order_suc = 'your order has been received.'
        actual_order_suc = driver.find_element(By.XPATH, "//h1").text.lower()
        assert actual_order_suc == expect_order_suc
        order_no = driver.find_element(By.XPATH, "//*[contains(text(), 'Your order #')]//a").text
        assert order_no is not None
    
def test_day6():
    driver = webdriver.Chrome()
    with allure.step("Step 1: go to page"):
        driver.get(Data().url)
        driver.maximize_window
        driver.implicitly_wait(3)
    check_out(driver)
    place_order(driver)
    driver.quit()
    

if __name__ == '__main__':
    pytest.main(['test_Day6.py'])