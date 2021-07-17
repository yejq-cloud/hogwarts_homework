"""
hogwarts 
yejq
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from homework6.page.basepage import Base
from homework6.page.contactpage import ContactPage


class MainPage(Base):
    _CON_ELE = (MobileBy.XPATH," //* [@text='通讯录']")
    # def __init__(self,driver: WebDriver):
    #     #实例化一个driver,将上个页面的driver传过来。
          #继承Base后，这里的init方法就不需要了
    #     self.driver = driver

    def click_contact(self):
        # self.driver.find_element(MobileBy.XPATH," //* [@text='通讯录']").click()
        #替换成封装的方法，并将需要传的数据提去出去
        self.find_and_click(*self._CON_ELE)
        return ContactPage(self.driver)