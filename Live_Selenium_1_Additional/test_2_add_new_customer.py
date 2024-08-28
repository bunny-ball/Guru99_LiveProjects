'''
Key Point: How to pass value between two test cases.
'''
import pytest
from selenium import webdriver  
from selenium.webdriver.common.by import By
import time
from conftest import ValueStorage
from datetime import date

new_customer_info = {
                'Customer Name':'tbbssasaatt',
                'Gender':'male',
                'Birthdate':'2013-11-04',
                'Address':'Jamnagar',
                'City':'Jamnagar',
                'State':'Gujarat',
                'Pin':'567321',
                'Mobile No':'8000439021',
                'Email':'test5676@test.com'
}
new_customer_pwd = '1234@1234'

new_account_info = {
                    'Account Type':'Savings',
                    'Current Amount':'500'
}

@pytest.mark.usefixtures("driver")
class Test_add_new_customer():


    def test_SM4(self,driver):
        
        driver.find_element(By.LINK_TEXT, "New Customer").click()
        
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(new_customer_info['Customer Name'])
        driver.find_element(By.XPATH ,"//input[@value='m']").click()
        driver.find_element(By.XPATH, "//input[@type='date']").send_keys("11042013")
        driver.find_element(By.XPATH, "//textarea").send_keys(new_customer_info['Address'])
        driver.find_element(By.XPATH, "//input[@name='city']").send_keys(new_customer_info['City'])
        driver.find_element(By.XPATH, "//input[@name='state']").send_keys(new_customer_info['State'])
        driver.find_element(By.XPATH, "//input[@name='pinno']").send_keys(new_customer_info['Pin'])
        driver.find_element(By.XPATH, "//input[@name='telephoneno']").send_keys(new_customer_info['Mobile No'])
        driver.find_element(By.XPATH, "//input[@name='emailid']").send_keys(new_customer_info['Email'])
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(new_customer_pwd)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@name='sub']").click()
        time.sleep(0.5)

        ValueStorage.customer_id = driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[4]//td[2]").text
        
        actual_name = driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[5]//td[2]").text
        assert actual_name == new_customer_info['Customer Name']
        actual_gender = driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[6]//td[2]").text
        assert actual_gender == new_customer_info['Gender']
        acutal_birthdate = driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[7]//td[2]").text
        assert acutal_birthdate == new_customer_info['Birthdate']
        actual_address = driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[8]//td[2]").text
        assert actual_address == new_customer_info['Address']
        actual_city = driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[9]//td[2]").text
        assert actual_city == new_customer_info['City']
        actual_state = driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[10]//td[2]").text
        assert actual_state == new_customer_info['State']
        acutal_pin = driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[11]//td[2]").text
        assert acutal_pin == new_customer_info['Pin']
        actual_mobileno = driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[12]//td[2]").text
        assert actual_mobileno == new_customer_info['Mobile No']
        actual_email = driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[13]//td[2]").text
        assert actual_email == new_customer_info['Email']
        
        driver.find_element(By.XPATH, "//table[@name='customer']//tbody//tr[14]//td/a").click()
        time.sleep(1)
    
    def test_SM5(self,driver):
        
        driver.find_element(By.LINK_TEXT, 'New Account').click()
        
        driver.find_element(By.XPATH, "//input[@name='cusid']").send_keys(ValueStorage.customer_id)
        driver.find_element(By.XPATH, "//input[@name='inideposit']").send_keys(new_account_info['Current Amount'])
        driver.find_element(By.XPATH, "//input[@name='button2']").click()
        time.sleep(1)
        
        ValueStorage.account_id = driver.find_element(By.XPATH, "//table[@name='account']//tbody//tr[4]//td[2]").text

        actual_customerid = driver.find_element(By.XPATH, "//table[@name='account']//tbody//tr[5]//td[2]").text
        assert actual_customerid == ValueStorage.customer_id
        actual_customer_name = driver.find_element(By.XPATH, "//table[@name='account']//tbody//tr[6]//td[2]").text
        assert actual_customer_name == new_customer_info['Customer Name']
        actual_email = driver.find_element(By.XPATH, "//table[@name='account']//tbody//tr[7]//td[2]").text
        assert actual_email == new_customer_info['Email']
        actual_type = driver.find_element(By.XPATH, "//table[@name='account']//tbody//tr[8]//td[2]").text
        assert actual_type == new_account_info['Account Type']
        actual_opening_date = driver.find_element(By.XPATH, "//table[@name='account']//tbody//tr[9]//td[2]").text
        assert actual_opening_date == date.today().strftime('%Y-%m-%d')
        actual_curr_amount = driver.find_element(By.XPATH, "//table[@name='account']//tbody//tr[10]//td[2]").text
        assert actual_curr_amount == new_account_info['Current Amount']
        
        
if __name__ == '__main__':
    pytest.main(['test_2_add_new_customer.py'])