import pytest
from selenium import webdriver  
from selenium.webdriver.common.by import By
from conftest import Password, Info
import time

new_pwd = '123123!'

@pytest.mark.usefixtures("driver")
class Test_change_pwd():     
    def test_SM1(self,driver):

        
        driver.find_element(By.LINK_TEXT, "Change Password").click()
        driver.find_element(By.XPATH, "//input[@name='oldpassword']").send_keys("abc")        
        driver.find_element(By.XPATH, "//input[@name='newpassword']").send_keys(new_pwd)
        driver.find_element(By.XPATH, "//input[@name='confirmpassword']").send_keys(new_pwd)        
        driver.find_element(By.XPATH, "//input[@name='sub']").click()
        time.sleep(0.5)
        
        alert = driver.switch_to.alert
        
        assert alert.text.lower() == 'Old password is incorrect'.lower()
        alert.accept()
        time.sleep(0.5)
        assert driver.find_element(By.XPATH, "//p[@class='heading3']").text == 'Change Password'
        
    def test_SM2(self,driver):

        
        driver.find_element(By.LINK_TEXT, "Change Password").click()        
        driver.find_element(By.XPATH, "//input[@name='oldpassword']").send_keys(Password.current_pwd)
        driver.find_element(By.XPATH, "//input[@name='newpassword']").send_keys(new_pwd)
        driver.find_element(By.XPATH, "//input[@name='confirmpassword']").send_keys(new_pwd)
        
        driver.find_element(By.XPATH, "//input[@name='sub']").click()
        time.sleep(0.5)
        
        alert = driver.switch_to.alert
        
        assert alert.text.lower() == 'Password is changed'.lower()
        Password.current_pwd = new_pwd
        alert.accept()
        time.sleep(1)
        assert driver.find_element(By.XPATH, "//h2").text == 'Guru99 Bank'   

    def test_SM3(self,driver):
        
        driver.find_element(By.XPATH, "//input[@name='uid']").send_keys(Info().user)   
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(Password.current_pwd)
        driver.find_element(By.XPATH,"//input[@value='LOGIN']").click()
        show_msg =  driver.find_element(By.XPATH, '//tr[@class=\'heading3\']').text
        assert Info().user  in show_msg
    
if __name__ == '__main__':
    pytest.main(['-sv','test_1_change_password.py'])