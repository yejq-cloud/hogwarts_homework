"""
hogwarts 
yejq
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from homework6.page.basepage import Base
from homework6.page.informpage2 import InformPage2


class InformPage(Base):
    _THREE = (MobileBy.ID, "com.tencent.wework:id/hc9")
    def click_three(self):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hc9").click()
        self.find_and_click(*self._THREE)
        return InformPage2(self.driver)