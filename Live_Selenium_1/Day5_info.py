from selenium import webdriver

class Info():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://www.demo.guru99.com/V4/'