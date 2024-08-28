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
        # driver.quit()
        
    
    # def test_SM7(ddriver):
        
        
    #     # driver = Info().driver
    #     # driver.maximize_window()
    #     # driver.implicitly_wait(3)
        
    #     # driver.get(Info().url)
    #     # driver.find_element(By.XPATH, "//input[@name='uid']").send_keys(Info().user)   
    #     # driver.find_element(By.XPATH, "//input[@name='password']").send_keys(Info().new_pwd)
    #     # driver.find_element(By.XPATH,"//input[@value='LOGIN']").click()
        
    #     ddriver.find_element(By.LINK_TEXT, "Delete Account").click()
        
    #     ddriver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(ValueStorage.account_id)
        
    #     ddriver.find_element(By.XPATH, "//input[@name='AccSubmit']").click()
        
    #     alert1 = ddriver.switch_to.alert
                
    #     alert1.accept()
        
    #     alert2 = ddriver.switch_to.alert
        
    #     assert alert2.text.lower() in "Account deleted successfully".lower()
        
    #     alert2.accept()
    #     #back to delete account page
    #     show_msg =  ddriver.find_element(By.XPATH, "//tr//p[@class='heading3']").text
    #     assert "Delete Account Form" ==  show_msg
    #     time.sleep(3)  
    #     # driver.quit()      
        
        
if __name__ == '__main__':
    pytest.main(['test_3_delete_account.py'])
        
        