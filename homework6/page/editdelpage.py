"""
hogwarts 
yejq
"""
from appium.webdriver.common.mobileby import MobileBy
from homework6.page.basepage import Base


class EditDelPage(Base):
    def click_delmember(self):
        _DELMUN = (MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).\
                                 instance(0)).scrollIntoView(new UiSelector().\
                                 text("删除成员").instance(0));')
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().scrollable(true).\
        #                          instance(0)).scrollIntoView(new UiSelector().\
        #                          text("删除成员").instance(0));').click()

        self.find_and_click(*self._DELMUN)
        return self

    def click_confirm(self):
        _CONFORM = (MobileBy.ID, "com.tencent.wework:id/bg8")
        from homework6.page.contactpage import ContactPage
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bg8").click()
        self.find_and_click(*self._CONFORM)

        return ContactPage(self.driver)