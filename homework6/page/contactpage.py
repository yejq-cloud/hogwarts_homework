"""
hogwarts 
yejq
"""
from time import sleep

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from homework6.page.adresspage import AdressPage
from homework6.page.basepage import Base
from homework6.page.informpage import InformPage


class ContactPage(Base):
    _ADDMEMBER = (MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).\
                                 instance(0)).scrollIntoView(new UiSelector().\
                                 text("添加成员").instance(0));')
    _FINDMEMBER = (MobileBy.XPATH, "//*[contains(@text, '何凤兰')]")
    # def __init__(self,driver: WebDriver):
    #     #实例化一个driver,将上个页面的driver传过来。
    #     #继承Base后，这里的init方法就不需要了
    #     self.driver = driver

    def click_addmember(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().scrollable(true).\
        #                          instance(0)).scrollIntoView(new UiSelector().\
        #                          text("添加成员").instance(0));').click()
        # 替换成封装的方法，并将需要传的数据提去出去
        self.find_and_click(*self._ADDMEMBER)
        return AdressPage(self.driver)

    def find_member(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '刘红梅')]").click()
        self.find_and_click(*self._FINDMEMBER)
        return InformPage(self.driver)
