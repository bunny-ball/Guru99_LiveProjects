
'''
Excute same test case steps but with different test data stored in MS Excel file.

Test Step:
1. Go to http://www.demo.guru99.com/V4/
2. Enter valid UserId
3. Enter valid Password
4. Click Login
5. Verify the oupput

Test Data:
1. Enter in valid user and valid pwd
2. Enter in invalid user and valid pwd
3. Enter in valid user and invalid pwd
4. Enter in invalid user and invalid pwd
'''
import pytest
import allure
from Day3_info import Info
from selenium import webdriver
from selenium.webdriver.common.by import By
import time   
import pandas as pd


# check if there's an alert exists
def is_alert_present(driver):
    try:
        driver.switch_to.alert
        return True
    except:
        return False
    
def login_verify(user,pwd):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    correct_u = "valid"
    correct_p = "valid"
    if user == correct_u:
        v_u = "valid"
    else:
        v_u = "invalid"
    step2 = "Step 2: enter " + v_u + " UserID"
    if pwd == correct_p:
        v_p = 'valid'
    else:
        v_p = "invalid"
    step3 = "Step 3: enter " + v_p + " Password"
    with allure.step("Step 1: goto website page"):
        driver.get(Info().url)
    with allure.step(step2):
        driver.find_element(By.XPATH, "//input[@name='uid']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@name='uid']").send_keys(user)
        time.sleep(0.5)
        # print("User: ", user)
    with allure.step(step3):
        driver.find_element(By.XPATH, "//input[@name='password']").clear()
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)
        time.sleep(0.5)
        # print("Password : ", pwd)
    with allure.step("Step 4: click Login"):

        driver.find_element(By.XPATH,"//input[@value='LOGIN']").click()
        time.sleep(0.5)
    
    with allure.step("Step 5: Verify the output"):
    # method 1: using alert exits to check login successful or failed
        # if is_alert_present(driver):
        #     # print("Invalid User or Password")
        #     assert driver.switch_to.alert.text == 'User or Password is not valid'
        # else:
        #     # print("Valid User and Password")
        #     show_msg =  driver.find_element(By.XPATH, '//tr[@class=\'heading3\']').text
        #     assert  user  in show_msg
    # method 2: using correct password and username to check successful or failed.
        if v_p == 'valid' and v_u == 'valid':  # login should be successful,
            show_msg =  driver.find_element(By.XPATH, '//tr[@class=\'heading3\']').text
            assert user  in show_msg
        else:
            alert = driver.switch_to.alert
            assert alert.text == 'User or Password is not valid'
            alert.accept()
            time.sleep(0.5)
            
    driver.quit()


def test_day3():
    excelData = pd.read_excel(r"C:\Users\Nemo\Documents\Automation_Testing_Learning\Guru99_LiveProjects\Live_Selenium_1\Day3.xlsx")

    for row in range(0,4):   
        user = excelData.iloc[row][0]
        pwd = excelData.iloc[row][1]
        login_verify(user,pwd)
        

if __name__ == '__main__':
    pytest.main(['test_Day3.py'])
