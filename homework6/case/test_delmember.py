"""
hogwarts 
yejq
"""
import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


@allure.feature("通讯录")
class TestAddMember:
    @allure.story("第一步：打开应用app")
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appActivity": ".launch.WwMainActivity",
            "appPackage": "com.tencent.wework",
            "noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)
    @allure.story("关闭应用app")
    def teardown(self):
        self.driver.quit()

    @allure.story("测试删除成员")
    def test_del_member(self):
        with allure.step("点击通讯录"):
            self.driver.find_element(MobileBy.XPATH, "//* [@text='通讯录']").click()
        with allure.step("找到成员,并点击。"):
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '唐旭')]").click()
        with allure.step("点击右上角'...'"):
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hc9").click()
        with allure.step("点击编辑成员"):
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b5r").click()
        with allure.step("滑动，点击删除成员"):
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().scrollable(true).\
                                     instance(0)).scrollIntoView(new UiSelector().\
                                     text("删除成员").instance(0));').click()
        with allure.step("点击确定"):
            self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/bg8").click()