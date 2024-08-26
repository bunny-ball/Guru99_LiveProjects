'''
Verify the product review mechanism

Test Steps:	
1. Go to http://live.techpanda.org/.
2. Go To Link - http://live.techpanda.org/index.php/review/product/list/id/1/
3. Fill the required review and submit it
4.Go to http://live.techpanda.org/index.php/backendlogin
5.Login as with credentials provided
6. Go to Catalogue -> Reviews and Ratings -> Customer Reviews ->Pending Reviews Menu
7.Sort table by Id and select comment then click on Edit link
8.Change status to 'Approved' and click "Save Review"
9.Go to http://live.techpanda.org/. Click Mobile Menu
10. Click on Sony Xperia image.
11. In detail page click on Review tab at bottom of page
12. Verify the review comment is shown  --> Review is approved and shown

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

class Testdata:
    def __init__(self):
        self.id = 'user01'
        self.pwd = 'guru99com'
        self.msg_thoughts = "This is an input box to input the thoughts. Just for testing."
        self.msg_review = "This is an input box to input the summary of review"
        self.msg_name = 'Nickname'

def capture_screen(driver, name : str):
    allure.attach(driver.get_screenshot_as_png(),name=name,attachment_type=allure.attachment_type.PNG)

def test_case2():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)

    with allure.step("Step 1: Go to http://live.techpanda.org/"):
        driver.get("http://live.techpanda.org/")
        time.sleep(1)
        
    with allure.step("Step 2: Go To Link - http://live.techpanda.org/index.php/review/product/list/id/1/"):
        driver.get("http://live.techpanda.org/index.php/review/product/list/id/1/")
        time.sleep(1)
        
    with allure.step("Step 3: Fill the required review and submit it"):
        driver.find_element(By.XPATH, "//input[@id='Quality 1_4']").click()
        driver.find_element(By.XPATH, "//textarea").send_keys(Testdata().msg_thoughts)
        driver.find_element(By.XPATH, "//input[@id='summary_field']").send_keys(Testdata().msg_review)
        driver.find_element(By.XPATH, "//input[@id='nickname_field']").send_keys(Testdata().msg_name)
        driver.find_element(By.XPATH, "//button[@title='Submit Review']").click()
    
    with allure.step("Step 4: Go to http://live.techpanda.org/index.php/backendlogin"):
        driver.get("http://live.techpanda.org/index.php/backendlogin")
    
    with allure.step("Step 5: Login the credentials provided"):
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys('user01')
        driver.find_element(By.XPATH, "//input[@id='login']").send_keys('guru99com')
        driver.find_element(By.XPATH, "//input[@title='Login']").click()
        # close Imcoming Message dialog
        driver.find_element(By.XPATH, "//a[@title='close']").click()
        
    with allure.step("Step 6: Go to Catalogue -> Reviews and Ratings -> Customer Reviews ->Pending Reviews Menu"):
        catalog = driver.find_element(By.XPATH, "//span[contains(text(),'Catalog')]")
        review_rating = driver.find_element(By.XPATH, "//span[contains(text(),'Reviews and Ratings')]")
        cus_review = driver.find_element(By.XPATH, "//span[contains(text(),'Customer Reviews')]")
        pending_review = driver.find_element(By.XPATH, "//span[contains(text(),'Pending Reviews')]")  
        ActionChains(driver).move_to_element(catalog).move_to_element(review_rating).move_to_element(cus_review).move_to_element(pending_review).click().perform()
        time.sleep(2)
    
    with allure.step("Step 7: Sort table by Id and select comment then click on Edit link"):
        driver.find_element(By.XPATH, "//a[@name='review_id']").click() # sort asc
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@name='review_id']").click() # sort desc
        time.sleep(1)
        capture_screen(driver, "step 7")
        driver.find_element(By.XPATH, "//a[contains(text(),'Edit')]").click()
    
    with allure.step("Step 8: Change status to 'Approved' and click 'Save Review'"):
        select_status = driver.find_element(By.XPATH, "//select[@id='status_id']")
        Select(select_status).select_by_visible_text("Approved")
        driver.find_element(By.XPATH, "//div[@id='anchor-content']//button[@title='Save Review']").click()
        time.sleep(2)
    
    with allure.step("Step 9: Go to http://live.techpanda.org/. Click Mobile Menu"):
        driver.get("http://live.techpanda.org/")
        driver.find_element(By.LINK_TEXT, 'MOBILE').click()
    
    with allure.step("Step 10: Click on Sony Xperia image"):
        driver.find_element(By.XPATH, "//img[@alt='Xperia']").click()
        time.sleep(1)
    
    with allure.step("Step 11: In detail page click on Review tab at bottom of page"):
        driver.find_element(By.XPATH, "//div[@class='product-collateral toggle-content tabs']//li[@class='last']").click()
        time.sleep(1)
        
    with allure.step("Step 12: Verify the review comment is shown"):
        capture_screen(driver, 'step 12')    
        actual_review_title = driver.find_element(By.XPATH, "//div[@id='customer-reviews']//dl/dt[1]").text
        actual_review_content = driver.find_element(By.XPATH, "//div[@id='customer-reviews']//dl/dd[1]").text
        assert Testdata().msg_review.lower() == actual_review_title.lower()
        assert Testdata().msg_thoughts.lower() in actual_review_content.lower()
        assert Testdata().msg_name.lower() in actual_review_content.lower()
    
    driver.quit()
    
if __name__ =='__main__':
    test_case2()