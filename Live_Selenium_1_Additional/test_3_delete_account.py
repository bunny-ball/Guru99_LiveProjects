# 19230

import pytest
from selenium import webdriver  
from selenium.webdriver.common.by import By
import time
from conftest import ValueStorage


@pytest.mark.usefixtures("driver")   
class Test_delete_account:

    def test_SM6(self,driver):
  
        driver.find_element(By.LINK_TEXT, "Delete Account").click()
        time.sleep(0.5)
        
        driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(ValueStorage.account_id)
        
        driver.find_element(By.XPATH, "//input[@name='AccSubmit']").click()
        
        alert = driver.switch_to.alert
        
        assert alert.text.lower() in 'Do you really want to delete this account?'.lower()
        
        alert.dismiss()
        time.sleep(1)
        
    
    def test_SM7(self,driver):
        
        
        driver.find_element(By.LINK_TEXT, "Delete Account").click()
        
        driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(ValueStorage.account_id)
        
        driver.find_element(By.XPATH, "//input[@name='AccSubmit']").click()
        
        alert1 = driver.switch_to.alert
                
        alert1.accept()
        
        alert2 = driver.switch_to.alert
        
        assert alert2.text.lower() in "Account deleted successfully".lower()
        
        alert2.accept()
        #back to delete account page
        show_msg =  driver.find_element(By.XPATH, "//tr//p[@class='heading3']").text
        assert "Delete Account Form" ==  show_msg
        time.sleep(1)
    
    def test_SM8(self, driver):
        driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(ValueStorage.account_id)
        driver.find_element(By.XPATH, "//input[@name='AccSubmit']").click()
        alert = driver.switch_to.alert
        assert alert.text in "Account does not exist"
        alert.accept()
        time.sleep(.5)
        assert driver.find_element(By.XPATH, "//tr//td/p[@class='heading3']").text == 'Mini Statement Form'
        
    def test_SM9(self, driver):
        driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(ValueStorage.account_id)
        driver.find_element(By.XPATH, "//input[@name='AccSubmit']").click()
        alert = driver.switch_to.alert
        assert alert.text in "Account does not exist"
        alert.accept()
        time.sleep(.5)
        assert driver.find_element(By.XPATH, "//tr//td/p[@class='heading3']").text == 'Balance Enquiry Form'
    
    def test_SM11(self,driver):
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(ValueStorage.account_id)
        driver.find_element(By.XPATH, "//input[@name='AccSubmit']").click()
        alert = driver.switch_to.alert
        assert alert.text in "Account does not exist"
        alert.accept()
        time.sleep(.5)
        assert driver.find_element(By.XPATH, "//tr//td/p[@class='heading3']").text == 'Customized Statement Form'
                      
if __name__ == '__main__':
    pytest.main(['test_3_delete_account.py'])
        
        