"""
hogwarts 
yejq
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from homework6.page.basepage import Base


class EditPage(Base):
    _EDITNAME = (MobileBy.ID, "com.tencent.wework:id/b09")
    _EDITNUM = (MobileBy.ID, "com.tencent.wework:id/f7y")
    _SAVE = (MobileBy.ID, "com.tencent.wework:id/ad2")

    # def __init__(self,driver: WebDriver):
    #     #实例化一个driver,将上个页面的driver传过来。
    #     #继承Base后，这里的init方法就不需要了
    #     self.driver = driver

    def edit_member(self, name, phonumber):
        from homework6.page.adresspage import AdressPage
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b09").send_keys(name)
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f7y").send_keys(phonumber)
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ad2").click()
        self.find_and_sendkeys(*self._EDITNAME,name)
        self.find_and_sendkeys(*self._EDITNUM,phonumber)
        self.find_and_click(*self._SAVE)

        return AdressPage(self.driver)