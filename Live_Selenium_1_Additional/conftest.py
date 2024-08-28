import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Info():
    def __init__(self):
        self.url = "http://www.demo.guru99.com/V4/"
        self.user = "mngr586608"
        self.old_pwd = "123!!123"
        #self.current_pwd = '123!123'
        
class Password:
    current_pwd = '123123!!'
        
        
class ValueStorage:
    customer_id = None
    account_id = None
    
@pytest.fixture(scope='module')
def driver():
    # options = Options()
    # options.add_experimental_option("detach", True)
    _driver = webdriver.Chrome()
    # cdriver.maximize_window()
    _driver.implicitly_wait(10)
    _driver.get(Info().url)
    _driver.find_element(By.XPATH, "//input[@name='uid']").send_keys(Info().user)   
    _driver.find_element(By.XPATH, "//input[@name='password']").send_keys(Password.current_pwd)
    _driver.find_element(By.XPATH,"//input[@value='LOGIN']").click()
    yield _driver
    _driver.quit()