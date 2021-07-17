"""
hogwarts 
yejq
"""
# from _pytest import logging
import logging

from appium.webdriver.webdriver import WebDriver


class Base():

    def __init__(self,driver: WebDriver = None):
        self.driver = driver

    def log_info(self,message):
        logging.info(message)

    def find(self,locator, value):
        self.log_info("find")
        self.log_info(locator)
        self.log_info(value)
        #查找元素，并将其返回去
        return self.driver.find_element(locator, value)

    def find_and_click(self,locator,value):
        self.log_info('find_and_click')
        #查找元素之后点击
        self.find(locator,value).click()

    def find_and_sendkeys(self,locator,value,text):
        self.log_info('find_and_sendkeys')
        self.find(locator,value).send_keys(text)

    #老师自己封装了自己的滑动查找，我这里没有，理解之后再加入自己封装的滑动查找。

    def get_toast_text(self):
        self.log_info('get_toast_text')
        result = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").get_attribute('text')
        return result