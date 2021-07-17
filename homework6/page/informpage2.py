"""
hogwarts 
yejq
"""
from appium.webdriver.common.mobileby import MobileBy
from homework6.page.basepage import Base
from homework6.page.editdelpage import EditDelPage


class InformPage2(Base):
    _EDITMUM = (MobileBy.ID, "com.tencent.wework:id/b5r")
    def click_edit(self):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b5r").click()
        self.find_and_click(*self._EDITMUM)
        return EditDelPage(self.driver)