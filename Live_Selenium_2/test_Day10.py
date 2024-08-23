'''Emails
Export all Orders in csv file and display these information in console and you are able to send this file to another email id as attachment 
1.Go to http://live.techpanda.org/index.php/backendlogin/
2.Login the credentials provided 
3.Go to Sales-> Orders menu 
4.Select 'CSV' in Export To dropdown and click Export button. 
5.Read downloaded file and display all order information in console windows 
6. Attach this exported file and email to another email id 

Expect:
1) Console displays all order information 
2) Email is sent successfully 

Test Data: 
id = "user01"
pass = "guru99com"

NOTE:
1. When click the export button, there will be an error.
2. This case provide a way to practice the hover menu clicking using ActionChains.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_day10():
    driver = webdriver.Chrome()
    driver.maximize_window
    driver.implicitly_wait(30)
    driver.get("http://live.techpanda.org/index.php/backendlogin/")

    driver.find_element(By.XPATH, "//input[@id='username']").send_keys('user01')
    driver.find_element(By.XPATH, "//input[@id='login']").send_keys('guru99com')
    driver.find_element(By.XPATH, "//input[@title='Login']").click()

    driver.find_element(By.XPATH, "//a[@title='close']").click()
# the method how to click an element when this element only appears the cursor hover another element
    orders_menu = driver.find_element(By.XPATH, "//*[@id=\"nav\"]/li[1]/ul/li[1]/a")
    sales_menu = driver.find_element(By.XPATH, '//*[@id="nav"]/li[1]/a')
    ActionChains(driver).move_to_element(sales_menu).perform()
    time.sleep(1)
    ActionChains(driver).move_to_element(orders_menu).click(orders_menu).perform()
    time.sleep(2)
    driver.quit()
    
if __name__ =='__main__':
    test_day10()
