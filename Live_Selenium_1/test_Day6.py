
'''
Excute same test case steps but with different test data, instead of Excel, using pytest.mark.parametrize

Test Step:
1. Go to http://www.demo.guru99.com/V4/
2. Enter valid UserId
3. Enter valid Password
4. Click Login
5. Verify ManagerID shown in shown
6. take screenshot of the o/p

Test Data:
1. Enter in valid user and valid pwd
2. Enter in invalid user and valid pwd
3. Enter in valid user and invalid pwd
4. Enter in invalid user and invalid pwd
'''
import pytest
import allure
from Day5_info import Info
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

   
@pytest.mark.parametrize("user,pwd", [("valid","valid"),("invalid","valid"),
                                      ("valid","invalid"),("mngr58081","invalid")])

def test_day3(user,pwd):

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
        if v_p == 'valid' and v_u == 'valid':  # login should be successful
            allure.attach(driver.get_screenshot_as_png(),name="Login Successful",attachment_type=allure.attachment_type.PNG)
            show_msg =  driver.find_element(By.XPATH, '//tr[@class=\'heading3\']').text
            assert user  in show_msg
        else:
            alert = driver.switch_to.alert
            assert alert.text == 'User or Password is not valid'
            alert.accept()
            time.sleep(0.5)
            
    driver.quit()

if __name__ == '__main__':
    pytest.main(['test_Day6.py'])
